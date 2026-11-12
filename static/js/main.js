/**
 * ElectroVision AI — Core Interactive Application
 * Integrates Computer Vision (YOLO11s), WebRTC, Component Catalog & AI Assistant
 */

document.addEventListener("DOMContentLoaded", () => {
    // ==========================================
    // 1. ELEMEN DOM & STATE
    // ==========================================
    const webcamElement = document.getElementById("webcam");
    const canvasElement = document.getElementById("overlay");
    const scannerLaser = document.getElementById("scannerLaser");
    const liveIndicator = document.getElementById("liveDetectionIndicator");
    const cameraOffOverlay = document.getElementById("cameraOffOverlay");
    const cameraSelect = document.getElementById("cameraSelect");

    // Tombol Kontrol Scanner
    const btnToggleCamera = document.getElementById("btnToggleCamera");
    const btnStartOverlay = document.getElementById("btnStartOverlay");
    const btnUploadOverlay = document.getElementById("btnUploadOverlay");
    const btnUploadImage = document.getElementById("btnUploadImage");
    const imageFileInput = document.getElementById("imageFileInput");
    const btnCaptureSnapshot = document.getElementById("btnCaptureSnapshot");
    const toggleIcon = document.getElementById("toggleIcon");
    const toggleText = document.getElementById("toggleText");

    // HUD & Status Meta
    const hudStatusBadge = document.getElementById("hudStatusBadge");
    const hudStatusText = document.getElementById("hudStatusText");
    const hudLatencyBadge = document.getElementById("hudLatencyBadge");

    // Panel Hasil Deteksi
    const statusBanner = document.getElementById("detectionStatusBanner");
    const statusIndicatorIcon = document.getElementById("statusIndicatorIcon");
    const statusIndicatorTitle = document.getElementById("statusIndicatorTitle");
    const statusIndicatorDesc = document.getElementById("statusIndicatorDesc");
    const detectionCountBadge = document.getElementById("detectionCountBadge");

    // Primary Result Card
    const primaryComponentName = document.getElementById("primaryComponentName");
    const primaryConfidenceBadge = document.getElementById("primaryConfidenceBadge");
    const primaryMetaRow = document.getElementById("primaryMetaRow");
    const primaryCategoryText = document.getElementById("primaryCategoryText");
    const primarySpeedText = document.getElementById("primarySpeedText");
    const primaryShortDesc = document.getElementById("primaryShortDesc");
    const primaryActions = document.getElementById("primaryActions");
    const btnOpenPrimaryDetail = document.getElementById("btnOpenPrimaryDetail");
    const btnAskAIPrimary = document.getElementById("btnAskAIPrimary");

    // Stream Detections List
    const listBadgeCount = document.getElementById("listBadgeCount");
    const detectionsStreamList = document.getElementById("detectionsStreamList");

    // Component Explorer / Catalog Elements
    const componentSearchInput = document.getElementById("componentSearchInput");
    const btnClearSearch = document.getElementById("btnClearSearch");
    const categoryFilterPills = document.getElementById("categoryFilterPills");
    const componentsGrid = document.getElementById("componentsGrid");
    const emptySearchState = document.getElementById("emptySearchState");
    const btnResetSearch = document.getElementById("btnResetSearch");

    // Modal Detail Komponen
    const componentModal = document.getElementById("componentModal");
    const btnModalClose = document.getElementById("btnModalClose");
    const btnModalDismiss = document.getElementById("btnModalDismiss");
    const btnModalAskAI = document.getElementById("btnModalAskAI");
    const modalCompCategory = document.getElementById("modalCompCategory");
    const modalCompTitle = document.getElementById("modalCompTitle");
    const modalCompRawName = document.getElementById("modalCompRawName");
    const modalCompDesc = document.getElementById("modalCompDesc");
    const modalCompFunction = document.getElementById("modalCompFunction");
    const modalCompWorking = document.getElementById("modalCompWorking");
    const modalCompPinout = document.getElementById("modalCompPinout");
    const modalCompUsage = document.getElementById("modalCompUsage");
    const modalCompApplication = document.getElementById("modalCompApplication");

    // Snapshot Modal
    const snapshotModal = document.getElementById("snapshotModal");
    const btnSnapshotClose = document.getElementById("btnSnapshotClose");
    const btnSnapshotDismiss = document.getElementById("btnSnapshotDismiss");
    const snapshotImage = document.getElementById("snapshotImage");
    const btnDownloadSnapshot = document.getElementById("btnDownloadSnapshot");
    const snapshotStatsBox = document.getElementById("snapshotStatsBox");

    // AI Chatbot Assistant Elements
    const floatingAiBtn = document.getElementById("floatingAiBtn");
    const btnNavAssistant = document.getElementById("btnNavAssistant");
    const chatDrawerOverlay = document.getElementById("chatDrawerOverlay");
    const btnCloseChat = document.getElementById("btnCloseChat");
    const btnClearChat = document.getElementById("btnClearChat");
    const chatContextBar = document.getElementById("chatContextBar");
    const chatContextComponentName = document.getElementById("chatContextComponentName");
    const btnClearContext = document.getElementById("btnClearContext");
    const chatMessagesScroll = document.getElementById("chatMessagesScroll");
    const chatTypingIndicator = document.getElementById("chatTypingIndicator");
    const chatInputForm = document.getElementById("chatInputForm");
    const chatInput = document.getElementById("chatInput");
    const chatSuggestionsChips = document.getElementById("chatSuggestionsChips");

    // Mobile Navbar
    const btnMobileMenu = document.getElementById("btnMobileMenu");
    const navLinks = document.getElementById("navLinks");

    // ==========================================
    // 2. STATE APLIKASI
    // ==========================================
    let activeStream = null;
    let frameLoopTimer = null;
    let isProcessing = false;
    let isCameraRunning = false;
    let cameraRequestId = 0;
    let currentPrimaryComponent = null;
    let activeChatContext = null;
    let cachedComponents = {};

    const context = canvasElement.getContext("2d");

    const ICON_PLAY = `
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <polygon points="5 3 19 12 5 21 5 3"></polygon>
        </svg>
    `;
    const ICON_STOP = `
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <rect x="5" y="5" width="14" height="14" rx="2"></rect>
        </svg>
    `;

    // ==========================================
    // 3. KAMERA & SIKLUS HIDUP WEBRTC
    // ==========================================
    async function loadCameras() {
        try {
            if (!navigator.mediaDevices?.enumerateDevices) {
                setHUDStatus("Akses media tidak didukung", "error");
                return;
            }

            const devices = await navigator.mediaDevices.enumerateDevices();
            const cameras = devices.filter(d => d.kind === "videoinput");

            cameraSelect.replaceChildren();
            cameras.forEach((cam, idx) => {
                const opt = document.createElement("option");
                opt.value = cam.deviceId;
                opt.textContent = cam.label || `Kamera ${idx + 1}`;
                cameraSelect.appendChild(opt);
            });

            if (cameras.length === 0) {
                const defaultOpt = document.createElement("option");
                defaultOpt.value = "";
                defaultOpt.textContent = "Kamera Default";
                cameraSelect.appendChild(defaultOpt);
            }

            setHUDStatus("Kamera Siap", "normal");
        } catch (err) {
            console.error("Gagal membaca daftar kamera:", err);
            setHUDStatus("Perangkat kamera belum siap", "warning");
        }
    }

    async function startCamera(deviceId = null) {
        const requestId = ++cameraRequestId;
        clearTimeout(frameLoopTimer);

        if (activeStream) {
            activeStream.getTracks().forEach(track => track.stop());
            activeStream = null;
        }

        if (!navigator.mediaDevices?.getUserMedia) {
            setHUDStatus("Browser tidak mendukung WebRTC", "error");
            alert("Browser Anda tidak mendukung akses kamera langsung.");
            return;
        }

        setHUDStatus("Menghubungkan...", "warning");

        const targetDeviceId = deviceId || cameraSelect.value || undefined;
        const constraints = {
            video: {
                deviceId: targetDeviceId ? { exact: targetDeviceId } : undefined,
                width: { ideal: 640 },
                height: { ideal: 480 },
                facingMode: "environment"
            }
        };

        try {
            const stream = await navigator.mediaDevices.getUserMedia(constraints);
            if (requestId !== cameraRequestId) {
                stream.getTracks().forEach(track => track.stop());
                return;
            }

            activeStream = stream;
            webcamElement.srcObject = stream;

            webcamElement.onloadedmetadata = () => {
                if (requestId !== cameraRequestId) return;

                canvasElement.width = webcamElement.videoWidth;
                canvasElement.height = webcamElement.videoHeight;

                isCameraRunning = true;
                cameraOffOverlay.style.display = "none";
                liveIndicator.style.display = "inline-flex";
                scannerLaser.classList.add("active");

                btnToggleCamera.classList.add("running");
                toggleIcon.innerHTML = ICON_STOP;
                toggleText.innerText = "Matikan Kamera";
                btnCaptureSnapshot.disabled = false;

                setHUDStatus("Live Streaming", "live");
                setDetectionBannerStatus("detecting");

                loadCamerasWithoutRestart();
                processFrameLoop(requestId);
            };

            stream.getVideoTracks()[0].onended = () => {
                stopCamera();
            };

        } catch (error) {
            console.error("Akses webcam gagal:", error);
            isCameraRunning = false;
            let errMsg = "Akses Kamera Ditolak";
            if (error.name === "NotFoundError" || error.name === "DevicesNotFoundError") {
                errMsg = "Kamera Tidak Ditemukan";
            }
            setHUDStatus(errMsg, "error");
            alert(`${errMsg}. Mohon izinkan akses kamera di pengaturan browser Anda.`);
        }
    }

    function stopCamera() {
        cameraRequestId++;
        clearTimeout(frameLoopTimer);

        if (activeStream) {
            activeStream.getTracks().forEach(track => track.stop());
            activeStream = null;
        }

        webcamElement.srcObject = null;
        context.clearRect(0, 0, canvasElement.width, canvasElement.height);

        isCameraRunning = false;
        cameraOffOverlay.style.display = "flex";
        liveIndicator.style.display = "none";
        scannerLaser.classList.remove("active");

        btnToggleCamera.classList.remove("running");
        toggleIcon.innerHTML = ICON_PLAY;
        toggleText.innerText = "Nyalakan Kamera";
        btnCaptureSnapshot.disabled = true;

        resetDetectionResults();
        setHUDStatus("Kamera Nonaktif", "normal");
        setDetectionBannerStatus("waiting");
    }

    async function loadCamerasWithoutRestart() {
        try {
            const devices = await navigator.mediaDevices.enumerateDevices();
            const cameras = devices.filter(d => d.kind === "videoinput");
            if (cameras.length > 0 && cameras[0].label) {
                const currentVal = cameraSelect.value;
                cameraSelect.replaceChildren();
                cameras.forEach((cam, idx) => {
                    const opt = document.createElement("option");
                    opt.value = cam.deviceId;
                    opt.textContent = cam.label || `Kamera ${idx + 1}`;
                    if (cam.deviceId === currentVal) opt.selected = true;
                    cameraSelect.appendChild(opt);
                });
            }
        } catch (e) {
            // diamkan
        }
    }

    function setHUDStatus(message, state = "normal") {
        hudStatusText.innerText = message;
        hudStatusBadge.className = "badge-hud";
        if (state === "live") {
            hudStatusBadge.classList.add("live");
        }
    }

    // ==========================================
    // 4. FRAME EXTRACTION & INFERENSI YOLO11s
    // ==========================================
    async function processFrameLoop(requestId) {
        if (requestId !== cameraRequestId || !isCameraRunning) return;

        if (!isProcessing && webcamElement.readyState === 4) {
            isProcessing = true;
            try {
                await sendFrameToBackend(requestId);
            } catch (err) {
                console.error("Frame inference error:", err);
            } finally {
                isProcessing = false;
            }
        }

        if (requestId === cameraRequestId && isCameraRunning) {
            // Interval ~75ms (~13-15 FPS) seimbang antara responsivitas dan utilisasi CPU
            frameLoopTimer = setTimeout(() => processFrameLoop(requestId), 75);
        }
    }

    async function sendFrameToBackend(requestId) {
        const offCanvas = document.createElement("canvas");
        offCanvas.width = canvasElement.width;
        offCanvas.height = canvasElement.height;
        const offCtx = offCanvas.getContext("2d");
        if (!offCtx) return;

        offCtx.drawImage(webcamElement, 0, 0, offCanvas.width, offCanvas.height);

        const blob = await new Promise(resolve => {
            offCanvas.toBlob(resolve, "image/jpeg", 0.72);
        });

        if (!blob || requestId !== cameraRequestId) return;

        const formData = new FormData();
        formData.append("file", blob, "frame.jpg");

        const response = await fetch("/detect", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const data = await response.json();
        if (requestId === cameraRequestId && isCameraRunning) {
            updateDetectionUI(data);
        }
    }

    // ==========================================
    // 5. RENDERING HASIL DETEKSI & HUD OVERLAY
    // ==========================================
    function setDetectionBannerStatus(state) {
        statusBanner.className = "detection-status-banner";
        if (state === "detected") {
            statusBanner.classList.add("detected");
            statusIndicatorIcon.innerText = "⚡";
            statusIndicatorTitle.innerText = "Objek Terdeteksi";
            statusIndicatorDesc.innerText = "Komponen dikenali oleh model";
        } else if (state === "detecting") {
            statusIndicatorIcon.innerText = "🔍";
            statusIndicatorTitle.innerText = "Sedang Memindai...";
            statusIndicatorDesc.innerText = "Mencari komponen dalam frame";
        } else {
            statusIndicatorIcon.innerText = "⏳";
            statusIndicatorTitle.innerText = "Menunggu Objek";
            statusIndicatorDesc.innerText = "Arahkan komponen ke kamera";
        }
    }

    function resetDetectionResults() {
        primaryComponentName.innerText = "Belum Ada Objek";
        primaryComponentName.classList.add("placeholder");
        primaryConfidenceBadge.style.display = "none";
        primaryMetaRow.style.display = "none";
        primaryActions.style.display = "none";
        primaryShortDesc.innerText = "Posisikan komponen elektronik di depan lensa kamera dengan pencahayaan yang cukup untuk melihat hasil identifikasi instan.";

        detectionCountBadge.innerText = "0 Objek";
        listBadgeCount.innerText = "0";
        hudLatencyBadge.innerText = "0 ms";

        detectionsStreamList.replaceChildren();
        const emptyState = document.createElement("li");
        emptyState.className = "empty-stream-state";
        emptyState.innerHTML = `
            <div class="empty-stream-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <rect x="2" y="7" width="20" height="14" rx="2"></rect>
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                </svg>
            </div>
            <p>Belum ada komponen elektronika yang terdeteksi.<br>Dekatkan komponen ke depan kamera.</p>
        `;
        detectionsStreamList.appendChild(emptyState);
    }

    function updateDetectionUI(data) {
        context.clearRect(0, 0, canvasElement.width, canvasElement.height);

        const detections = data.detections || [];
        const latency = data.inference_time_ms || 0;
        hudLatencyBadge.innerText = `${latency} ms`;
        detectionCountBadge.innerText = `${detections.length} Objek`;
        listBadgeCount.innerText = detections.length;

        if (detections.length === 0) {
            setDetectionBannerStatus(isCameraRunning ? "detecting" : "waiting");
            primaryComponentName.innerText = isCameraRunning ? "Memindai Objek..." : "Belum Ada Objek";
            primaryComponentName.classList.add("placeholder");
            primaryConfidenceBadge.style.display = "none";
            primaryMetaRow.style.display = "none";
            primaryActions.style.display = "none";
            primaryShortDesc.innerText = "Arahkan komponen elektronika lebih dekat ke lensa kamera dengan pencahayaan yang cukup.";
            currentPrimaryComponent = null;

            detectionsStreamList.replaceChildren();
            const emptyState = document.createElement("li");
            emptyState.className = "empty-stream-state";
            emptyState.innerHTML = `
                <div class="empty-stream-icon">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                        <rect x="2" y="7" width="20" height="14" rx="2"></rect>
                        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                    </svg>
                </div>
                <p>Belum ada komponen elektronika yang terdeteksi.<br>Dekatkan komponen ke depan kamera.</p>
            `;
            detectionsStreamList.appendChild(emptyState);
            return;
        }

        // Status Ditemukan
        setDetectionBannerStatus("detected");

        // Objek Utama (Tertinggi Confidence)
        const primary = detections[0];
        currentPrimaryComponent = primary;
        primaryComponentName.innerText = primary.label;
        primaryComponentName.classList.remove("placeholder");

        primaryConfidenceBadge.innerText = `${primary.confidence}% Akurasi`;
        primaryConfidenceBadge.style.display = "inline-flex";

        primaryCategoryText.innerText = primary.category || "Electronics";
        primarySpeedText.innerText = `${latency} ms latensi`;
        primaryMetaRow.style.display = "flex";

        if (primary.short_desc) {
            primaryShortDesc.innerText = primary.short_desc;
        }
        primaryActions.style.display = "flex";

        // Sinkronisasi konteks ke AI Chatbot
        updateChatContext(primary.label, primary.raw_label);

        // Render List Objek
        detectionsStreamList.replaceChildren();

        detections.forEach((item, idx) => {
            const [x1, y1, x2, y2] = item.box;
            const width = x2 - x1;
            const height = y2 - y1;

            // Gambar Bounding Box di Canvas Overlay
            const isTop = idx === 0;
            const boxColor = isTop ? "#20D3F2" : "#168BFF";

            context.strokeStyle = boxColor;
            context.lineWidth = isTop ? 3.5 : 2.5;
            context.strokeRect(x1, y1, width, height);

            // Corner Accents pada box
            const cornerLen = Math.min(16, width / 4, height / 4);
            context.strokeStyle = "#FFFFFF";
            context.lineWidth = isTop ? 4 : 3;
            // TL
            context.beginPath(); context.moveTo(x1, y1 + cornerLen); context.lineTo(x1, y1); context.lineTo(x1 + cornerLen, y1); context.stroke();
            // TR
            context.beginPath(); context.moveTo(x2 - cornerLen, y1); context.lineTo(x2, y1); context.lineTo(x2, y1 + cornerLen); context.stroke();
            // BL
            context.beginPath(); context.moveTo(x1, y2 - cornerLen); context.lineTo(x1, y2); context.lineTo(x1 + cornerLen, y2); context.stroke();
            // BR
            context.beginPath(); context.moveTo(x2 - cornerLen, y2); context.lineTo(x2, y2); context.lineTo(x2, y2 - cornerLen); context.stroke();

            // Label Tag
            const labelText = `${item.label} ${item.confidence}%`;
            context.font = "bold 13px -apple-system, BlinkMacSystemFont, sans-serif";
            const tagMetrics = context.measureText(labelText);
            const tagH = 24;
            const tagW = tagMetrics.width + 16;

            let tagY = y1 - tagH;
            let textY = y1 - 7;
            if (tagY < 0) {
                tagY = y1;
                textY = y1 + 17;
            }

            context.fillStyle = isTop ? "rgba(11, 18, 32, 0.9)" : "rgba(20, 36, 58, 0.85)";
            context.fillRect(x1, tagY, tagW, tagH);

            context.strokeStyle = boxColor;
            context.lineWidth = 1.2;
            context.strokeRect(x1, tagY, tagW, tagH);

            context.fillStyle = "#FFFFFF";
            context.fillText(labelText, x1 + 8, textY);

            // Tambahkan ke List Card HTML
            const rowItem = document.createElement("li");
            rowItem.className = "detection-item-row";
            rowItem.title = "Klik untuk melihat detail spesifikasi";

            rowItem.innerHTML = `
                <div class="detection-item-left">
                    <span class="item-icon-tag">⚙️</span>
                    <div class="item-name-group">
                        <strong>${item.label}</strong>
                        <span>${item.category || 'Komponen Elektronik'}</span>
                    </div>
                </div>
                <div class="detection-item-right">
                    <span class="item-conf-tag">${item.confidence}%</span>
                </div>
            `;

            rowItem.addEventListener("click", () => {
                openComponentModal(item.raw_label || item.label);
            });

            detectionsStreamList.appendChild(rowItem);
        });
    }

    // ==========================================
    // 6. UPLOAD IMAGE & CAPTURE SNAPSHOT
    // ==========================================
    // Upload File Trigger
    btnUploadOverlay?.addEventListener("click", () => imageFileInput.click());
    btnUploadImage?.addEventListener("click", () => imageFileInput.click());

    imageFileInput?.addEventListener("change", async (e) => {
        const file = e.target.files?.[0];
        if (!file) return;

        // Jika kamera sedang aktif, hentikan dulu
        if (isCameraRunning) {
            stopCamera();
        }

        setHUDStatus("Memproses Foto...", "warning");
        setDetectionBannerStatus("detecting");

        try {
            const img = new Image();
            img.src = URL.createObjectURL(file);
            await new Promise((resolve, reject) => {
                img.onload = resolve;
                img.onerror = reject;
            });

            canvasElement.width = img.naturalWidth;
            canvasElement.height = img.naturalHeight;

            // Gambar foto ke canvas latar belakang
            context.drawImage(img, 0, 0, canvasElement.width, canvasElement.height);
            cameraOffOverlay.style.display = "none";

            const formData = new FormData();
            formData.append("file", file, file.name);

            const res = await fetch("/detect", {
                method: "POST",
                body: formData
            });

            if (!res.ok) throw new Error(`HTTP ${res.status}`);

            const data = await res.json();
            setHUDStatus("Foto Teranalisis", "normal");
            updateDetectionUI(data);

        } catch (err) {
            console.error("Gagal memproses upload gambar:", err);
            alert("Gagal menganalisis gambar. Pastikan format file adalah JPG/PNG.");
            setHUDStatus("Upload Gagal", "error");
        } finally {
            imageFileInput.value = "";
        }
    });

    // Capture Snapshot Frame
    btnCaptureSnapshot?.addEventListener("click", () => {
        if (!isCameraRunning) return;

        const mergeCanvas = document.createElement("canvas");
        mergeCanvas.width = canvasElement.width;
        mergeCanvas.height = canvasElement.height;
        const mCtx = mergeCanvas.getContext("2d");

        mCtx.drawImage(webcamElement, 0, 0, mergeCanvas.width, mergeCanvas.height);
        mCtx.drawImage(canvasElement, 0, 0, mergeCanvas.width, mergeCanvas.height);

        const dataUrl = mergeCanvas.toDataURL("image/jpeg", 0.9);
        snapshotImage.src = dataUrl;
        btnDownloadSnapshot.href = dataUrl;

        snapshotStatsBox.innerHTML = `
            <div style="font-size: 0.88rem; color: #475569;">
                <p><strong>Komponen Utama:</strong> ${currentPrimaryComponent ? currentPrimaryComponent.label : 'None'}</p>
                <p><strong>Jumlah Objek:</strong> ${listBadgeCount.innerText}</p>
                <p><strong>Waktu Capture:</strong> ${new Date().toLocaleTimeString('id-ID')}</p>
            </div>
        `;

        snapshotModal.classList.add("active");
        snapshotModal.setAttribute("aria-hidden", "false");
    });

    btnSnapshotClose?.addEventListener("click", closeSnapshotModal);
    btnSnapshotDismiss?.addEventListener("click", closeSnapshotModal);

    function closeSnapshotModal() {
        snapshotModal.classList.remove("active");
        snapshotModal.setAttribute("aria-hidden", "true");
    }

    // ==========================================
    // 7. COMPONENT EXPLORER (SEARCH & FILTER)
    // ==========================================
    function filterCatalog() {
        const query = componentSearchInput.value.trim().toLowerCase();
        const activeCategory = categoryFilterPills.querySelector(".filter-pill.active")?.dataset.category || "all";
        const cards = componentsGrid.querySelectorAll(".component-card");

        let visibleCount = 0;

        cards.forEach(card => {
            const cardName = card.dataset.name || "";
            const cardCategory = card.dataset.category || "";

            const matchesQuery = !query || cardName.includes(query);
            const matchesCategory = activeCategory === "all" || cardCategory === activeCategory;

            if (matchesQuery && matchesCategory) {
                card.style.display = "flex";
                visibleCount++;
            } else {
                card.style.display = "none";
            }
        });

        btnClearSearch.style.display = query ? "block" : "none";
        emptySearchState.style.display = visibleCount === 0 ? "block" : "none";
    }

    componentSearchInput?.addEventListener("input", filterCatalog);

    btnClearSearch?.addEventListener("click", () => {
        componentSearchInput.value = "";
        filterCatalog();
        componentSearchInput.focus();
    });

    btnResetSearch?.addEventListener("click", () => {
        componentSearchInput.value = "";
        categoryFilterPills.querySelectorAll(".filter-pill").forEach(p => p.classList.remove("active"));
        categoryFilterPills.querySelector('.filter-pill[data-category="all"]')?.classList.add("active");
        filterCatalog();
    });

    categoryFilterPills?.addEventListener("click", (e) => {
        const pill = e.target.closest(".filter-pill");
        if (!pill) return;

        categoryFilterPills.querySelectorAll(".filter-pill").forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        filterCatalog();
    });

    // ==========================================
    // 8. COMPONENT DETAIL MODAL
    // ==========================================
    async function openComponentModal(componentKey) {
        if (!componentKey) return;

        try {
            let comp = cachedComponents[componentKey];
            if (!comp) {
                const res = await fetch(`/api/components/${encodeURIComponent(componentKey)}`);
                if (res.ok) {
                    const data = await res.json();
                    comp = data.component;
                    cachedComponents[componentKey] = comp;
                }
            }

            if (!comp) {
                alert("Data spesifikasi komponen belum tersedia.");
                return;
            }

            modalCompTitle.innerText = comp.name;
            modalCompCategory.innerText = comp.category;
            modalCompRawName.innerText = `ID: ${comp.raw_name}`;
            modalCompDesc.innerText = comp.description;
            modalCompFunction.innerText = comp.function;
            modalCompWorking.innerText = comp.working_principle;
            modalCompPinout.innerText = comp.pinout;
            modalCompUsage.innerText = comp.usage;
            modalCompApplication.innerText = comp.application;

            btnModalAskAI.dataset.key = comp.raw_name;
            btnModalAskAI.dataset.name = comp.name;

            componentModal.classList.add("active");
            componentModal.setAttribute("aria-hidden", "false");

        } catch (err) {
            console.error("Gagal membuka detail komponen:", err);
        }
    }

    function closeComponentModal() {
        componentModal.classList.remove("active");
        componentModal.setAttribute("aria-hidden", "true");
    }

    btnModalClose?.addEventListener("click", closeComponentModal);
    btnModalDismiss?.addEventListener("click", closeComponentModal);
    componentModal?.addEventListener("click", (e) => {
        if (e.target === componentModal) closeComponentModal();
    });

    // Event listener untuk tombol "Lihat Detail" di katalog
    componentsGrid?.addEventListener("click", (e) => {
        const btnDetail = e.target.closest(".btn-comp-detail");
        const btnAsk = e.target.closest(".btn-comp-ask");

        if (btnDetail) {
            openComponentModal(btnDetail.dataset.key);
        } else if (btnAsk) {
            const key = btnAsk.dataset.key;
            openChatDrawerWithComponent(key);
        }
    });

    btnOpenPrimaryDetail?.addEventListener("click", () => {
        if (currentPrimaryComponent) {
            openComponentModal(currentPrimaryComponent.raw_label || currentPrimaryComponent.label);
        }
    });

    // ==========================================
    // 9. ELECTROVISION AI ASSISTANT CHATBOT
    // ==========================================
    function openChatDrawer() {
        chatDrawerOverlay.classList.add("active");
        chatDrawerOverlay.setAttribute("aria-hidden", "false");
        setTimeout(() => chatInput.focus(), 200);
    }

    function closeChatDrawer() {
        chatDrawerOverlay.classList.remove("active");
        chatDrawerOverlay.setAttribute("aria-hidden", "true");
    }

    floatingAiBtn?.addEventListener("click", openChatDrawer);
    btnNavAssistant?.addEventListener("click", openChatDrawer);
    btnCloseChat?.addEventListener("click", closeChatDrawer);
    chatDrawerOverlay?.addEventListener("click", (e) => {
        if (e.target === chatDrawerOverlay) closeChatDrawer();
    });

    function updateChatContext(displayName, rawLabel) {
        activeChatContext = rawLabel || displayName;
        chatContextComponentName.innerText = displayName;
        chatContextBar.style.display = "flex";
    }

    btnClearContext?.addEventListener("click", () => {
        activeChatContext = null;
        chatContextBar.style.display = "none";
    });

    btnClearChat?.addEventListener("click", () => {
        chatMessagesScroll.replaceChildren();
        appendAIMessage(`Riwayat percakapan telah dibersihkan. Silakan tanyakan hal apa pun seputar komponen elektronika!`);
    });

    function openChatDrawerWithComponent(componentName) {
        updateChatContext(componentName, componentName);
        openChatDrawer();
        appendAIMessage(`Anda memilih komponen **${componentName}**. Ada yang ingin ditanyakan seputar fungsi, pinout, atau contoh kodenya?`);
    }

    btnAskAIPrimary?.addEventListener("click", () => {
        if (currentPrimaryComponent) {
            openChatDrawerWithComponent(currentPrimaryComponent.label);
        }
    });

    btnModalAskAI?.addEventListener("click", () => {
        const name = btnModalAskAI.dataset.name || btnModalAskAI.dataset.key;
        closeComponentModal();
        openChatDrawerWithComponent(name);
    });

    // Suggestions Chips
    chatSuggestionsChips?.addEventListener("click", (e) => {
        const chip = e.target.closest(".suggestion-chip");
        if (!chip) return;
        const prompt = chip.dataset.prompt;
        submitUserChatMessage(prompt);
    });

    // Form Kirim Chat dengan Integrasi LangFlow
    chatInputForm?.addEventListener("submit", (e) => {
        e.preventDefault();
        const userText = chatInput.value.trim();
        if (!userText) return;

        // Kosongkan input
        chatInput.value = "";

        // Kirim pesan dengan konteks aktif jika ada
        submitUserChatMessage(userText);
    });

    async function submitUserChatMessage(userText) {
        // Ambil nilai teks dari elemen #chatContextComponentName jika #chatContextBar sedang aktif
        let currentContext = null;
        if (chatContextBar && chatContextBar.style.display !== "none") {
            currentContext = chatContextComponentName ? chatContextComponentName.innerText.trim() : null;
        }

        // Tampilkan gelembung chat pengguna di #chatMessagesScroll
        appendUserMessage(userText);

        // Tampilkan #chatTypingIndicator
        chatTypingIndicator.style.display = "flex";
        chatMessagesScroll.scrollTop = chatMessagesScroll.scrollHeight;

        try {
            // Lakukan fetch POST ke /api/chat
            const res = await fetch("/api/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: userText,
                    context: currentContext
                })
            });

            if (!res.ok) throw new Error(`HTTP ${res.status}`);

            const data = await res.json();

            // Sembunyikan typing indicator
            chatTypingIndicator.style.display = "none";

            // Cetak jawaban dari LangFlow ke dalam gelembung chat assistant
            appendAIMessage(data.reply || "Tidak ada jawaban.");

        } catch (err) {
            console.error("Chat error:", err);
            chatTypingIndicator.style.display = "none";
            appendAIMessage("Maaf, terjadi gangguan saat menghubungi server LangFlow.");
        }
    }

    function appendUserMessage(text) {
        const bubble = document.createElement("div");
        bubble.className = "message-bubble message-user";
        bubble.innerHTML = `
            <div class="bubble-content">
                <p>${escapeHtml(text)}</p>
            </div>
        `;
        chatMessagesScroll.appendChild(bubble);
        chatMessagesScroll.scrollTop = chatMessagesScroll.scrollHeight;
    }

    function appendAIMessage(markdownText) {
        const bubble = document.createElement("div");
        bubble.className = "message-bubble message-assistant";
        bubble.innerHTML = `
            <div class="bubble-avatar">⚡</div>
            <div class="bubble-content">
                ${renderBasicMarkdown(markdownText)}
            </div>
        `;
        chatMessagesScroll.appendChild(bubble);
        chatMessagesScroll.scrollTop = chatMessagesScroll.scrollHeight;
    }

    // Basic Markdown Parser untuk teks balasan AI
    function renderBasicMarkdown(md) {
        if (!md) return "";
        let html = md;

        // Escape XSS dasar
        html = html.replace(/</g, "&lt;").replace(/>/g, "&gt;");

        // Code Blocks ```cpp ... ```
        html = html.replace(/```(?:cpp|c|python)?([\s\S]*?)```/g, (match, p1) => {
            return `<pre><code>${p1.trim()}</code></pre>`;
        });

        // Inline Code `code`
        html = html.replace(/`([^`]+)`/g, "<code>$1</code>");

        // Headers ###
        html = html.replace(/^### (.*$)/gim, '<h4 style="font-size:0.95rem;margin:0.5rem 0 0.3rem;color:#0B1220;">$1</h4>');
        html = html.replace(/^## (.*$)/gim, '<h3 style="font-size:1.05rem;margin:0.6rem 0 0.35rem;color:#0B1220;">$1</h3>');

        // Bold & Italic
        html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
        html = html.replace(/\*([^*]+)\*/g, "<em>$1</em>");

        // Blockquotes
        html = html.replace(/^&gt; (.*$)/gim, '<blockquote>$1</blockquote>');

        // Unordered Lists
        html = html.replace(/^\s*-\s+(.*$)/gim, '<li style="margin-left:1.2rem;list-style:disc;">$1</li>');

        // Paragraphs
        html = html.split(/\n\n+/).map(p => {
            if (p.startsWith("<pre>") || p.startsWith("<h") || p.startsWith("<blockquote>")) return p;
            return `<p>${p.replace(/\n/g, "<br>")}</p>`;
        }).join("");

        return html;
    }

    function escapeHtml(str) {
        const div = document.createElement("div");
        div.textContent = str;
        return div.innerHTML;
    }

    // Keyboard Shortcuts: ESC to close modals/drawers
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            closeComponentModal();
            closeSnapshotModal();
            closeChatDrawer();
        }
    });

    // Mobile Navbar Menu Toggle
    btnMobileMenu?.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    // Nav smooth scroll & active link
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("active");
            document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));
            link.classList.add("active");
        });
    });

    // ==========================================
    // 10. INISIALISASI
    // ==========================================
    btnToggleCamera?.addEventListener("click", () => {
        if (isCameraRunning) {
            stopCamera();
        } else {
            startCamera(cameraSelect.value);
        }
    });

    btnStartOverlay?.addEventListener("click", () => {
        startCamera(cameraSelect.value);
    });

    cameraSelect?.addEventListener("change", () => {
        if (isCameraRunning) {
            startCamera(cameraSelect.value);
        }
    });

    // Mulai membaca kamera yang tersedia di perangkat
    loadCameras();
});
