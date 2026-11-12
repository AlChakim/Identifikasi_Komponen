import os
import requests

# Konfigurasi URL dan API_KEY untuk flow ElectroVision LangFlow
URL = "http://localhost:7860/api/v1/run/c0f7d697-82dc-46de-9af9-3406398319b0"
API_KEY = os.environ.get("LANGFLOW_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GEMINI_NODE = "ext:google:GoogleGenerativeAIComponent@official-bvb8u"  # Sesuaikan jika ID komponen berbeda

def tanya(pesan, sesi="user_iot"):
    payload = {
        "input_value": pesan,
        "input_type": "chat",
        "output_type": "chat",
        "session_id": sesi,
        "tweaks": {GEMINI_NODE: {"api_key": GOOGLE_API_KEY}}
    }
    r = requests.post(URL, json=payload, headers={"x-api-key": API_KEY}, timeout=120)
    r.raise_for_status()
    for keluaran in r.json()["outputs"][0]["outputs"]:
        pesan_keluar = (keluaran.get("results") or {}).get("message") or {}
        teks = (pesan_keluar.get("data") or {}).get("text") or pesan_keluar.get("text")
        if teks:
            return teks
    return "Tidak ada jawaban."

if __name__ == "__main__":
    print(tanya("Apa fungsi dari komponen ESP32?"))

