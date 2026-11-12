import io
import os
import time
import tempfile
import asyncio
from typing import Optional
from pydantic import BaseModel

# Konfigurasi direktori cache sementara sebelum import library agar tidak error izin folder
_mpl_dir = os.path.join(tempfile.gettempdir(), "matplotlib")
_yolo_dir = os.path.join(tempfile.gettempdir(), "ultralytics")
os.makedirs(_mpl_dir, exist_ok=True)
os.makedirs(_yolo_dir, exist_ok=True)
os.environ["MPLCONFIGDIR"] = _mpl_dir
os.environ["YOLO_CONFIG_DIR"] = _yolo_dir

from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
from ultralytics import YOLO

import components_data
from gemini_langflow_IoT import tanya

app = FastAPI(
    title="ElectroVision AI - Smart Electronics Recognition",
    description="Computer Vision & AI Dashboard untuk Identifikasi 65 Komponen Elektronika dengan YOLO11s",
    version="2.0.0"
)

# 1. Mount Static Files (CSS, JS) dan Templates (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 2. Muat Model YOLO Komponen Elektronika
MODEL_PATH = "model/my_model.pt"
print(f"Loading YOLO model from {MODEL_PATH}...")
model = YOLO(MODEL_PATH)
print("Model loaded successfully!")
print(f"Loaded {len(model.names)} electronic component classes.")

def format_label(label: str) -> str:
    """Format nama kelas ke nama ramah pengguna."""
    comp = components_data.get_component(label)
    if comp:
        return comp["name"]
    formatted = label.replace("-", " ")
    formatted = formatted.replace("1 5 Volt", "1.5V").replace("3 3 Volt", "3.3V").replace("9 Volt", "9V")
    return formatted

# Model Skema Request untuk Chatbot AI
class ChatMessage(BaseModel):
    message: str
    context: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    """Endpoint utama untuk menampilkan dashboard ElectroVision AI."""
    all_components = components_data.get_all_components()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "total_classes": len(model.names),
        "categories_count": len(components_data.CATEGORIES),
        "categories": components_data.CATEGORIES,
        "components": all_components
    })

@app.get("/components-list")
async def get_components_list():
    """Endpoint kompatibilitas untuk mendapatkan daftar ringkas komponen."""
    classes_list = [
        {
            "id": class_id,
            "raw_name": raw_name,
            "display_name": format_label(raw_name)
        }
        for class_id, raw_name in sorted(model.names.items())
    ]
    return JSONResponse(content={
        "status": "success",
        "total": len(classes_list),
        "components": classes_list
    })

@app.get("/api/components")
async def api_get_components():
    """Endpoint API untuk mendapatkan seluruh katalog 65 komponen dengan kategori dan spesifikasinya."""
    return JSONResponse(content={
        "status": "success",
        "total": len(components_data.COMPONENTS_DATA),
        "categories": components_data.CATEGORIES,
        "components": components_data.get_all_components()
    })

@app.get("/api/components/{component_key}")
async def api_get_component_detail(component_key: str):
    """Endpoint API untuk mendapatkan rincian spesifik dari satu komponen elektronika."""
    comp = components_data.get_component(component_key)
    if not comp:
        raise HTTPException(status_code=404, detail="Komponen tidak ditemukan")
    return JSONResponse(content={
        "status": "success",
        "component": comp
    })

@app.get("/api/stats")
async def api_get_stats():
    """Endpoint API status sistem dan model."""
    return JSONResponse(content={
        "status": "online",
        "model_architecture": "YOLO11s",
        "total_classes": len(model.names),
        "categories_count": len(components_data.CATEGORIES),
        "engine": "PyTorch + Ultralytics + FastAPI",
        "input_resolution": "640x640",
        "latency_target": "< 60ms"
    })

@app.post("/api/chat")
async def api_chat(chat_data: ChatMessage):
    """
    Endpoint AI Assistant yang terintegrasi dengan LangFlow API.
    Menerima payload JSON: message (input pengguna) dan context (nama komponen yang sedang dideteksi).
    Menggunakan fungsi tanya(pesan) dari gemini_langflow_IoT.py sebagai pemroses utama (LLM).
    """
    query = chat_data.message.strip()
    if not query:
        return JSONResponse(content={
            "status": "error",
            "reply": "Pesan tidak boleh kosong."
        })
    
    # Injeksi Konteks:
    # Jika parameter context tersedia, gabungkan: "Pengguna sedang melihat komponen: {context}. Pertanyaan pengguna: {message}"
    # Jika tidak ada konteks, langsung kirim message.
    if chat_data.context and chat_data.context.strip():
        prompt = f"Pengguna sedang melihat komponen: {chat_data.context.strip()}. Pertanyaan pengguna: {query}"
    else:
        prompt = query
    
    try:
        # Panggil fungsi tanya() dari gemini_langflow_IoT secara asynchronous via thread pool
        jawaban = await asyncio.to_thread(tanya, prompt)
    except Exception as e:
        print(f"Error calling LangFlow API: {e}")
        jawaban = f"Terjadi kesalahan saat menghubungi LangFlow: {str(e)}"
    
    return JSONResponse(content={
        "status": "success",
        "reply": jawaban,
        "component": chat_data.context,
        "source": "langflow"
    })

@app.post("/detect")
async def detect_components(file: UploadFile = File(...)):
    """
    Endpoint pemroses frame gambar (dari webcam atau upload gambar).
    Menerima frame gambar, menjalankan inferensi YOLO11s, dan mengembalikan data deteksi lengkap.
    """
    try:
        image_bytes = await file.read()
        if not image_bytes:
            return JSONResponse(
                status_code=400,
                content={"status": "error", "message": "Frame gambar kosong"}
            )

        start_time = time.perf_counter()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Jalankan inferensi YOLO11s
        results = model.predict(source=image, conf=0.45, imgsz=640, verbose=False)
        inference_time_ms = round((time.perf_counter() - start_time) * 1000, 1)

        detections = []
        counts = {}

        for result in results:
            boxes = result.boxes
            for box in boxes:
                xyxy = box.xyxy[0].tolist()
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                raw_label = model.names[class_id]
                
                comp_info = components_data.get_component(raw_label)
                display_label = comp_info["name"] if comp_info else format_label(raw_label)
                category = comp_info["category"] if comp_info else "Electronics"
                short_desc = comp_info["short_desc"] if comp_info else ""

                counts[display_label] = counts.get(display_label, 0) + 1

                detections.append({
                    "box": [round(coord, 2) for coord in xyxy],
                    "label": display_label,
                    "raw_label": raw_label,
                    "confidence": round(confidence * 100, 1),
                    "category": category,
                    "short_desc": short_desc
                })

        # Urutkan deteksi berdasarkan confidence tertinggi
        detections.sort(key=lambda x: x["confidence"], reverse=True)

        primary_component = detections[0]["label"] if detections else None
        primary_raw = detections[0]["raw_label"] if detections else None
        primary_confidence = detections[0]["confidence"] if detections else None
        primary_category = detections[0]["category"] if detections else None

        summary = [{"name": name, "count": count} for name, count in counts.items()]
        summary.sort(key=lambda x: x["count"], reverse=True)

        return JSONResponse(content={
            "status": "success",
            "detected_count": len(detections),
            "unique_types_count": len(counts),
            "primary_component": primary_component,
            "primary_raw": primary_raw,
            "primary_confidence": primary_confidence,
            "primary_category": primary_category,
            "inference_time_ms": inference_time_ms,
            "summary": summary,
            "detections": detections
        })

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )
