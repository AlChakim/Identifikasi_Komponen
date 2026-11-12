"""
Database Komponen Elektronika untuk ElectroVision AI.
Berisi data lengkap 65 kelas komponen elektronika dari model YOLO11s.
"""

CATEGORIES = {
    "microcontroller": "Microcontroller",
    "sensor": "Sensor",
    "motor_actuator": "Motor & Actuator",
    "display": "Display",
    "passive": "Passive Components",
    "power": "Power Components",
    "communication": "Communication Module",
    "driver_controller": "Driver & Controller",
    "other": "Other Electronics"
}

COMPONENTS_DATA = {
    # 1. Microcontroller
    "Arduino-Uno": {
        "raw_name": "Arduino-Uno",
        "name": "Arduino Uno",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "Board mikrokontroler berbasis ATmega328P yang paling populer untuk pemula dan prototyping.",
        "icon": "cpu",
        "description": "Arduino Uno R3 adalah papan pengembangan mikrokontroler berbasis chip ATmega328P. Memiliki 14 pin I/O digital (6 di antaranya dapat digunakan sebagai output PWM), 6 input analog, osilator kristal 16 MHz, koneksi USB, jack daya, dan tombol reset.",
        "function": "Mengontrol perangkat input/output digital dan analog, memproses sensor, serta menjalankan logika komputasi otomatis.",
        "working_principle": "Mengeksekusi program (firmware C/C++) yang diunggah ke flash memory ATmega328P, membaca nilai pin input (sensor/tombol), dan mengirimkan sinyal output ke aktuator.",
        "pinout": "14 Digital I/O (D0-D13, D3/D5/D6/D9/D10/D11 PWM), 6 Analog In (A0-A5), 5V, 3.3V, GND, Vin, Reset.",
        "usage": "Diprogram menggunakan Arduino IDE melalui kabel USB Type-B. Catu daya 5V via USB atau 7-12V via barrel jack.",
        "application": "Otomasi rumah, robotika, pembaca sensor IoT, sistem kendali LED, proyek edukasi elektronika."
    },
    "Arduino-Nano": {
        "raw_name": "Arduino-Nano",
        "name": "Arduino Nano",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "Versi mini dari Arduino Uno yang breadboard-friendly dengan ATmega328P.",
        "icon": "cpu",
        "description": "Arduino Nano adalah board mikrokontroler kecil, lengkap, dan fleksibel yang cocok langsung dipasang pada breadboard. Menggunakan chip ATmega328P dengan 8 pin analog (2 lebih banyak dari Uno).",
        "function": "Memberikan kemampuan komputasi setara Arduino Uno dalam ukuran yang sangat ringkas untuk proyek kompak.",
        "working_principle": "Sama dengan Arduino Uno, mengeksekusi instruksi mikrokontroler 8-bit AVR 16 MHz.",
        "pinout": "14 Pin Digital (D0-D13), 8 Pin Analog (A0-A7), 5V, 3.3V, GND, RST, Mini-USB/Micro-USB port.",
        "usage": "Tancapkan pada breadboard, sambungkan kabel USB Mini/Micro ke laptop, pilih board 'Arduino Nano' di Arduino IDE.",
        "application": "Alat IoT portabel, wearable electronics, robot berukuran saku, modul kontrol mandiri."
    },
    "Arduino-Mega": {
        "raw_name": "Arduino-Mega",
        "name": "Arduino Mega",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "Board mikrokontroler ATmega2560 dengan 54 pin digital untuk proyek skala besar.",
        "icon": "cpu",
        "description": "Arduino Mega 2560 dirancang untuk proyek kompleks yang memerlukan banyak pin I/O dan memori flash besar (256 KB). Memiliki 54 pin digital I/O dan 16 input analog.",
        "function": "Mengontrol sistem multi-sensor dan multi-motor simultan tanpa kehabisan pin I/O.",
        "working_principle": "Chip ATmega2560 menjalankan logika tingkat lanjut, mendukung 4 UART serial hardware untuk komunikasi multi-perangkat.",
        "pinout": "54 Pin Digital (15 pin PWM), 16 Pin Analog (A0-A15), 4 port UART Hardware, SPI, I2C, 5V, 3.3V, GND.",
        "usage": "Hubungkan kabel USB, buka Arduino IDE pilih board 'Arduino Mega 2560'.",
        "application": "Printer 3D (RAMPS shield), robot humanoid, sistem otomasi industri, drone, dashboard telemetry."
    },
    "ESP32": {
        "raw_name": "ESP32",
        "name": "ESP32 Development Board",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "SoC 32-bit dual-core bertenaga tinggi dengan Wi-Fi dan Bluetooth BLE terintegrasi.",
        "icon": "wifi",
        "description": "ESP32 (ESP-WROOM-32) adalah modul mikrokontroler 32-bit dual-core Tensilica Xtensa LX6 berkecepatan hingga 240 MHz. Memiliki Wi-Fi 802.11 b/g/n dan Bluetooth v4.2 BR/EDR & BLE bawaan.",
        "function": "Memproses data berkecepatan tinggi dan menghubungkan sistem elektronika ke internet (IoT) via Wi-Fi/Bluetooth.",
        "working_principle": "Menjalankan FreeRTOS secara multitasking pada dual core, mengirimkan dan menerima paket data nirkabel secara efisien.",
        "pinout": "30/36 Pin Header: 36 GPIO, 18 ADC channels, 2 DAC channels, SPI, I2C, UART, capacitive touch sensors, 3.3V logic level.",
        "usage": "Diprogram menggunakan Arduino IDE, ESP-IDF, atau MicroPython. Perhatian: Logika pin adalah 3.3V (tidak toleran 5V langsung).",
        "application": "Smart Home IoT, web server embedded, audio streaming, monitoring sensor cloud, smart agriculture."
    },
    "ESP32-CAM": {
        "raw_name": "ESP32-CAM",
        "name": "ESP32-CAM",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "Modul ESP32 hemat biaya yang dilengkapi kamera OV2640 dan slot microSD.",
        "icon": "camera",
        "description": "ESP32-CAM menggabungkan prosesor ESP32 dengan modul kamera OV2640 2 Megapiksel, slot kartu TF/MicroSD, dan lampu flash LED berkecerahan tinggi.",
        "function": "Mengambil gambar, merekam video streaming, serta melakukan pengenalan gambar atau streaming video web server.",
        "working_principle": "Prosesor membaca data frame kamera OV2640 via DVP interface, mengompresi ke JPEG, dan mengalirkannya melalui Wi-Fi.",
        "pinout": "Konektor FPC Kamera, Slot MicroSD, Pin VCC (5V/3.3V), GND, U0R/U0T (untuk flash via USB-TTL), GPIO 0-16.",
        "usage": "Memerlukan adaptor FTDI USB-TTL untuk memprogram karena tidak memiliki port USB onboard. Hubungkan GPIO 0 ke GND saat flashing.",
        "application": "Kamera CCTV Wi-Fi, pengenalan wajah mandiri, pemantau pintu cerdas, video surveillance robot."
    },
    "ESP-01": {
        "raw_name": "ESP-01",
        "name": "ESP-01 (ESP8266)",
        "category": "Microcontroller",
        "category_id": "microcontroller",
        "short_desc": "Modul Wi-Fi ultra-ringkas berbasis SoC ESP8266 dengan antena PCB.",
        "icon": "wifi",
        "description": "ESP-01 adalah modul berbasis ESP8266 dengan 8 pin yang menyediakan konektivitas Wi-Fi murah untuk mikrokontroler lain atau sebagai modul kontrol mandiri.",
        "function": "Menambahkan konektivitas Wi-Fi ke board mikrokontroler via komunikasi serial AT Command.",
        "working_principle": "Menerjemahkan perintah serial UART menjadi request protokol TCP/IP Wi-Fi.",
        "pinout": "VCC (3.3V saja), GND, TX, RX, CH_PD/EN (Chip Enable), RST, GPIO0, GPIO2.",
        "usage": "Wajib menggunakan tegangan 3.3V stabil (maks 3.6V). Tarik pin CH_PD ke 3.3V agar modul menyala.",
        "application": "Smart plug Wi-Fi, saklar IoT relay, jembatan data sensor nirkabel."
    },

    # 2. Sensor
    "IR-Sensor": {
        "raw_name": "IR-Sensor",
        "name": "IR Sensor (Infrared Proximity)",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor jarak inframerah untuk deteksi rintangan dan keberadaan objek.",
        "icon": "radio",
        "description": "Modul sensor inframerah yang memiliki LED pemancar (transmitter) IR dan fotodioda penerima (receiver) disertai potensiometer pengatur sensitivitas jarak.",
        "function": "Mendeteksi ada tidaknya halangan atau objek di depan sensor dalam rentang 2-30 cm.",
        "working_principle": "Memancarkan sinar IR; bila ada objek, sinar dipantulkan kembali ke fotodioda penerima dan menghasilkan sinyal LOW/HIGH pada pin output.",
        "pinout": "VCC (3.3V - 5V), GND, OUT (Sinyal Digital).",
        "usage": "Hubungkan VCC ke 5V, GND ke GND, dan OUT ke pin digital mikrokontroler. Putar trimpot untuk menyesuaikan jarak deteksi.",
        "application": "Robot line follower, robot penghindar rintangan, sensor penghitung barang berjalan, kran air otomatis."
    },
    "Sonar-Sensor": {
        "raw_name": "Sonar-Sensor",
        "name": "Sonar / Ultrasonic Sensor (HC-SR04)",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor jarak ultrasonik non-kontak dengan rentang ukur 2 cm hingga 400 cm.",
        "icon": "activity",
        "description": "HC-SR04 adalah modul sensor jarak ultrasonik populer yang menggunakan dua tabung silinder transduser (Transmitter dan Receiver gelombang ultrasonik 40 kHz).",
        "function": "Mengukur jarak fisik objek secara presisi menggunakan pantulan gelombang suara ultrasonik.",
        "working_principle": "Pin Trig dipicu sinyal HIGH selama 10 mikrodetik. Modul memancarkan 8 pulsa 40 kHz dan pin Echo menghasilkan pulsa HIGH sebanding dengan waktu tempuh suara bolak-balik.",
        "pinout": "VCC (5V), Trig (Trigger input), Echo (Echo output), GND.",
        "usage": "Hitung jarak dengan rumus: Jarak = (Durasi pulsa Echo × 0.034 cm/us) / 2.",
        "application": "Pengukur tinggi badan digital, sensor parkir mobil, robot obstacle avoidance, pengukur ketinggian tangki air."
    },
    "Gas-Sensor": {
        "raw_name": "Gas-Sensor",
        "name": "Gas Sensor (MQ Series)",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor gas elektrokimia untuk mendeteksi asap, LPG, metana, dan gas mudah terbakar.",
        "icon": "wind",
        "description": "Sensor gas seri MQ (seperti MQ-2) menggunakan lapisan semikonduktor SnO2 (Timah Dioksida) yang konduktivitasnya berubah saat terpapar molekul gas target dalam udara.",
        "function": "Mendeteksi konsentrasi gas berbahaya, gas bocor, dan asap rokok/kebakaran.",
        "working_principle": "Pemanas internal (heater) memanaskan sensor; ketika ada gas reduksi, resistansi sensor turun sehingga tegangan output analog naik.",
        "pinout": "VCC (5V), GND, DO (Digital Output threshold), AO (Analog Output konsentrasi).",
        "usage": "Memerlukan pemanasan awal (preheating) sekitar 20-30 detik untuk pembacaan yang stabil.",
        "application": "Detektor kebocoran gas LPG rumah tangga, alarm kebakaran dini, monitoring kualitas udara industri."
    },
    "Humidity-Sensor": {
        "raw_name": "Humidity-Sensor",
        "name": "Humidity & Temp Sensor (DHT Series)",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor digital terkalibrasi untuk mengukur kelembaban relatif udara dan suhu.",
        "icon": "droplets",
        "description": "Sensor kelembaban dan suhu seperti DHT11 atau DHT22 menggunakan elemen kapasitif kelembaban dan termistor NTC untuk mengeluarkan sinyal digital bit-stream serial.",
        "function": "Mengukur kelembaban udara (% RH) dan suhu lingkungan secara akurat.",
        "working_principle": "Kapasitansi polimer berubah proporsional terhadap kelembaban udara. Mikrokontroler internal mengonversi nilai menjadi sinyal serial satu kabel (Single-bus).",
        "pinout": "VCC (3.3V - 5V), DATA (Sinyal digital I/O dengan pull-up resistor 10k), NC/GND.",
        "usage": "Gunakan library DHT sensor di Arduino. Baca data tiap interval minimal 1-2 detik.",
        "application": "Stasiun cuaca mini, pengatur kelembaban inkubator telur, sistem HVAC, green house cerdas."
    },
    "LDR-Sensor": {
        "raw_name": "LDR-Sensor",
        "name": "LDR / Light Sensor Module",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor intensitas cahaya berbasis fotoresistor (Light Dependent Resistor).",
        "icon": "sun",
        "description": "Modul sensor cahaya yang memanfaatkan material Kadmium Sulfida (CdS). Nilai resistansinya akan turun drastis saat terkena cahaya terang dan sangat tinggi saat gelap.",
        "function": "Mendeteksi tingkat pencahayaan di lingkungan sekitar (siang vs malam atau gelap vs terang).",
        "working_principle": "Foton cahaya menembus semikonduktor LDR, membebaskan elektron dan menurunkan nilai resistansi listrik.",
        "pinout": "VCC (3.3V - 5V), GND, DO (Digital Output), AO (Analog Output).",
        "usage": "Hubungkan pin AO ke pin ADC Arduino (A0) untuk pembacaan derajat lux secara halus.",
        "application": "Lampu penerangan jalan otomatis, sensor kecerahan layar pintar, solar tracker panel surya."
    },
    "Motion-Sensor": {
        "raw_name": "Motion-Sensor",
        "name": "PIR Motion Sensor (HC-SR501)",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor pendeteksi gerakan makhluk hidup berbasis radiasi inframerah pasif.",
        "icon": "eye",
        "description": "PIR (Passive Infrared) Sensor mendeteksi perubahan radiasi panas inframerah yang dipancarkan oleh tubuh manusia atau hewan yang bergerak melewati lensa Fresnel.",
        "function": "Mendeteksi kehadiran atau pergerakan orang dalam ruangan hingga jarak 7 meter.",
        "working_principle": "Elemen kristal piroelektrik menghasilkan muatan listrik ketika mendeteksi perbedaan fluktuasi panas IR di dua slot sensor.",
        "pinout": "VCC (5V - 12V), OUT (Digital 3.3V High saat ada gerak), GND. Dilengkapi 2 trimpot pengatur delay dan sensitivitas.",
        "usage": "Output pin menghasilkan sinyal digital HIGH selama durasi delay ketika gerakan terdeteksi.",
        "application": "Sistem alarm keamanan rumah, lampu koridor otomatis nyala saat orang lewat, penghemat energi ruangan."
    },
    "NTC-Thermistor": {
        "raw_name": "NTC-Thermistor",
        "name": "NTC Thermistor",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Resistor peka temperatur dengan koefisien suhu negatif.",
        "icon": "thermometer",
        "description": "NTC (Negative Temperature Coefficient) adalah resistor yang resistansinya menurun secara eksponensial seiring kenaikan temperatur sekitarnya.",
        "function": "Mengukur temperatur permukaan, fluida, atau udara secara instan dan ekonomis.",
        "working_principle": "Kenaikan suhu memicu lebih banyak pembawa muatan bergerak di dalam material keramik oksida logam.",
        "pinout": "2 Kaki terminal tanpa polaritas (pasif).",
        "usage": "Rangkai sebagai pembagi tegangan (voltage divider) dengan resistor referensi tetap 10k ohm ke pin analog mikrokontroler.",
        "application": "Hotend printer 3D, sensor suhu baterai laptop/HP, proteksi overheat amplifier, ketel air listrik."
    },
    "Raindrops-Module": {
        "raw_name": "Raindrops-Module",
        "name": "Raindrops / Rain Sensor Module",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Papan sensor jalur konduktif untuk mendeteksi tetesan air hujan.",
        "icon": "cloud-rain",
        "description": "Terdiri dari papan PCB dengan jalur nikel interlaced dan modul komparator LM393. Tetesan air hujan yang jatuh di atas papan menghubungkan jalur konduktif.",
        "function": "Mendeteksi terjadinya hujan serta intensitas curah hujan secara cepat.",
        "working_principle": "Air hujan bersifat konduktor listrik lemah; saat membasahi lempeng, resistansi antar jalur turun drastis.",
        "pinout": "Papan Sensor: 2 pin ke modul kontrol. Modul: VCC (3.3V-5V), GND, DO (Digital), AO (Analog).",
        "usage": "Letakkan papan sensor miring sekitar 15 derajat di luar ruangan agar air dapat mengalir turun setelah hujan reda.",
        "application": "Wiper mobil otomatis, jemuran otomatis menutup saat hujan, stasiun pemantau cuaca."
    },
    "Soil-Moisture-Sensor": {
        "raw_name": "Soil-Moisture-Sensor",
        "name": "Soil Moisture Sensor",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor probe kelembaban tanah untuk sistem irigasi cerdas.",
        "icon": "flower2",
        "description": "Sensor garpu probe yang ditancapkan ke dalam tanah untuk mengukur kadar air di sekitar perakaran tanaman.",
        "function": "Mengetahui apakah tanah dalam kondisi kering, lembab, atau basah.",
        "working_principle": "Tanah yang basah memiliki konduktivitas listrik lebih tinggi dibanding tanah yang kering.",
        "pinout": "Probe 2 pin, Modul LM393: VCC (3.3-5V), GND, DO, AO.",
        "usage": "Tancapkan kedua probe ke dalam tanah tanaman, baca nilai analog melalui pin A0 Arduino.",
        "application": "Sistem penyiram tanaman otomatis, smart agriculture, pot pintar pemantau tanaman hias."
    },
    "TCRT5000": {
        "raw_name": "TCRT5000",
        "name": "TCRT5000 Tracking Sensor",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor optik reflektif inframerah jarak dekat untuk pembaca garis robot.",
        "icon": "navigation",
        "description": "Sensor optoelektronik kompak yang mengintegrasikan LED pemancar inframerah dan fototransistor silikon NPN dalam kemasan plastik biru/hitam.",
        "function": "Membedakan permukaan terang (memantulkan sinar IR) dan gelap (menyerap sinar IR).",
        "working_principle": "Cahaya IR dipancarkan ke lantai; garis putih memantulkan cahaya kembali ke fototransistor, sedangkan garis hitam menyerapnya.",
        "pinout": "VCC (5V), GND, D0 (Digital out), A0 (Analog out).",
        "usage": "Pasang pada jarak 1-15 mm di atas permukaan lintasan robot line follower.",
        "application": "Robot pengikut garis (Line Tracer), sensor tachometer putaran motor, sensor kertas printer."
    },
    "Water-Sensor": {
        "raw_name": "Water-Sensor",
        "name": "Water Level Sensor",
        "category": "Sensor",
        "category_id": "sensor",
        "short_desc": "Sensor pendeteksi ketinggian air berbasis garis konduktor paralel.",
        "icon": "waves",
        "description": "Sensor berbentuk stik ramping dengan serangkaian jalur tembaga paralel terbuka untuk mendeteksi kedalaman rendaman air.",
        "function": "Mengukur volume atau level ketinggian cairan di dalam wadah penampung.",
        "working_principle": "Semakin tinggi air merendam jalur tembaga, semakin banyak arus listrik yang dihantarkan ke pin analog.",
        "pinout": "VCC (3.3V - 5V), GND, S (Signal Analog).",
        "usage": "Celupkan vertikal ke dalam tangki air; baca tegangan sinyal pada pin analog mikrokontroler.",
        "application": "Detektor banjir dini, monitor level tandon air rumah, sistem alarm kebocoran pipa."
    },

    # 3. Motor & Actuator
    "DC-Motor": {
        "raw_name": "DC-Motor",
        "name": "DC Motor (Direct Current)",
        "category": "Motor & Actuator",
        "category_id": "motor_actuator",
        "short_desc": "Motor listrik arus searah untuk menghasilkan gerakan putar terus menerus.",
        "icon": "rotate-cw",
        "description": "Aktuator elektromagnetik yang mengubah energi listrik DC menjadi energi kinetik rotasi continu.",
        "function": "Menggerakkan roda robot, baling-baling kipas, konveyor, dan mekanisme rotasi lainnya.",
        "working_principle": "Gaya Lorentz pada kumparan rotor dalam medan magnet stator menghasilkan torsi putar searah.",
        "pinout": "2 Terminal (Positif & Negatif, polaritas menentukan arah putaran).",
        "usage": "Wajib menggunakan modul driver motor (seperti L298N/L293D) karena arus motor melebihi kemampuan pin mikrokontroler.",
        "application": "Robot mobil (RC car), kipas pendingin, pembersih debu mini, pompa air DC."
    },
    "Servo-Motor": {
        "raw_name": "Servo-Motor",
        "name": "Servo Motor (SG90 / MG995)",
        "category": "Motor & Actuator",
        "category_id": "motor_actuator",
        "short_desc": "Motor dengan sistem umpan balik closed-loop untuk kendali sudut presisi (0-180°).",
        "icon": "compass",
        "description": "Motor servo mengombinasikan motor DC mini, gir reduksi gear-set, potensiometer feedback sudut, dan sirkuit kontrol internal dalam satu paket kompak.",
        "function": "Memposisikan lengan atau tuas poros pada sudut derajat tertentu (biasanya 0 hingga 180 derajat).",
        "working_principle": "Menerima sinyal kontrol PWM frekuensi 50 Hz; lebar pulsa (1 ms s.d. 2 ms) menentukan posisi sudut poros motor.",
        "pinout": "Cokelat/Hitam (GND), Merah (VCC 4.8V-6V), Oranye/Kuning (Sinyal PWM).",
        "usage": "Gunakan library `Servo.h` di Arduino, panggil method `myservo.write(sudut)`.",
        "application": "Lengan robot (robotic arm), penggerak kemudi rudder kapal/pesawat RC, palang pintu otomatis."
    },
    "Buzzer": {
        "raw_name": "Buzzer",
        "name": "Piezo Buzzer (Active / Passive)",
        "category": "Motor & Actuator",
        "category_id": "motor_actuator",
        "short_desc": "Komponen transduser audio piezoelektrik untuk menghasilkan suara peringatan atau melodi.",
        "icon": "volume-2",
        "description": "Buzzer piezoelektrik menggunakan piringan keramik piezo yang bergetar saat dialiri tegangan listrik untuk menghasilkan gelombang suara akustik.",
        "function": "Memberikan umpan balik suara, alarm peringatan, dan nada audio kepada pengguna.",
        "working_principle": "Efek piezoelektrik terbalik: tegangan bolak-balik menyebabkan piringan keramik memuai dan menyusut cepat sehingga memicu gelombang suara.",
        "pinout": "2 Pin: Positif (+) kaki panjang dan Negatif (-) kaki pendek.",
        "usage": "Buzzer aktif cukup diberi tegangan DC 5V; buzzer pasif membutuhkan sinyal PWM (`tone()` di Arduino).",
        "application": "Alarm anti maling, bel pintu, indikator suara kalkulator/microwave, instrumen nada musik 8-bit."
    },

    # 4. Display
    "LCD-Display": {
        "raw_name": "LCD-Display",
        "name": "LCD Display 16x2 (I2C)",
        "category": "Display",
        "category_id": "display",
        "short_desc": "Layar Liquid Crystal Display alfanumerik 16 karakter x 2 baris.",
        "icon": "monitor",
        "description": "Layar kristal cair monokrom berlatar biru/hijau dengan lampu latar LED yang mampu menampilkan 32 karakter teks secara bersamaan.",
        "function": "Menampilkan teks informasi, nilai sensor, menu, dan status sistem secara jelas.",
        "working_principle": "Molekul kristal cair menyelaraskan diri di bawah medan listrik untuk memblokir atau melewatkan cahaya backlight.",
        "pinout": "Modul I2C Backpack: GND, VCC (5V), SDA (Data I2C), SCL (Clock I2C).",
        "usage": "Gunakan library `LiquidCrystal_I2C`. Sambungkan SDA ke A4 dan SCL ke A5 pada Arduino Uno.",
        "application": "Display timbangan digital, penampil suhu/jam ruangan, counter antrean, display mesin kasir."
    },
    "OLED-Display": {
        "raw_name": "OLED-Display",
        "name": "OLED Display 0.96 inch (SSD1306)",
        "category": "Display",
        "category_id": "display",
        "short_desc": "Layar grafis OLED resolusi 128x64 pixel dengan kontras sangat tinggi dan hemat daya.",
        "icon": "tv",
        "description": "Layar Organic Light Emitting Diode berukuran 0.96 inci yang tidak memerlukan lampu latar karena setiap pixel menyala sendiri.",
        "function": "Menampilkan teks grafis halus, ikon, logo, grafik sinus, dan animasi pixel interaktif.",
        "working_principle": "Lapisan senyawa organik elektroluminesen memancarkan cahaya saat dialiri arus listrik.",
        "pinout": "VCC (3.3V-5V), GND, SCL (Clock I2C), SDA (Data I2C).",
        "usage": "Diprogram menggunakan library Adafruit_SSD1306 atau U8g2 via antarmuka I2C (alamat 0x3C).",
        "application": "Smartwatch DIY, indikator status baterai portable, alat ukur multimeter OLED, konsol game retro."
    },
    "7-Segment-Display": {
        "raw_name": "7-Segment-Display",
        "name": "7-Segment Display",
        "category": "Display",
        "category_id": "display",
        "short_desc": "Komponen display 7 segmen LED untuk menampilkan angka digital 0 hingga 9.",
        "icon": "hash",
        "description": "Kumpulan 7 batang LED tersusun membentuk angka '8' ditambah 1 titik desimal (DP). Tersedia tipe Common Anode (anoda bersama) dan Common Cathode (katoda bersama).",
        "function": "Menampilkan angka desimal, heksadesimal, dan indikator angka berukuran besar dan terang.",
        "working_principle": "Menyalakan kombinasi segmen LED tertentu (a, b, c, d, e, f, g) untuk merepresentasikan angka yang diinginkan.",
        "pinout": "10 Pin: 7 Pin segmen (A-G), 1 Pin DP, 2 Pin Common (VCC untuk Common Anode, GND untuk Common Cathode).",
        "usage": "Gunakan resistor pembatas arus 220 ohm pada tiap pin segmen atau gunakan chip driver MAX7219 / 74HC595.",
        "application": "Jam digital, stopwatch, papan skor olahraga, display lift, speedometer kendaraan."
    },

    # 5. Passive Components
    "Resistor": {
        "raw_name": "Resistor",
        "name": "Resistor (Fixed Resistor)",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Komponen pasif dua kutub untuk menghambat arus listrik dan membagi tegangan.",
        "icon": "sliders",
        "description": "Resistor karbon atau metal-film adalah komponen paling fundamental dalam elektronika. Nilai resistansinya ditandai oleh cincin gelang warna berkode standar EIA.",
        "function": "Membatasi arus listrik (current limiting), membagi tegangan (voltage divider), dan resistor pull-up/pull-down.",
        "working_principle": "Menerapkan Hukum Ohm (V = I × R), mendisipasikan kelebihan energi listrik menjadi panas sesuai nilai hambatan ohm (Ω).",
        "pinout": "2 Kaki terminal kawat simetris tanpa polaritas.",
        "usage": "Selalu pasang seri dengan LED (misal 220Ω atau 330Ω) untuk mencegah LED terbakar akibat arus lebih.",
        "application": "Semua rangkaian elektronika, pembagi tegangan sensor, pelindung pin mikroprosesor."
    },
    "Inductor": {
        "raw_name": "Inductor",
        "name": "Inductor (Toroid / Drum Core)",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Komponen pasif lilitan kawat untuk menyimpan energi dalam bentuk medan magnet.",
        "icon": "zap",
        "description": "Induktor berupa lilitan kawat tembaga berisolasi yang melingkar pada inti ferit atau toroid. Nilai induktansinya diukur dalam satuan Henry (H / mH / uH).",
        "function": "Menyaring frekuensi tinggi (filter noise), menstabilkan arus pada konverter daya, dan choke frekuensi radio.",
        "working_principle": "Menahan perubahan arus listrik tiba-tiba dengan menghasilkan gaya gerak listrik balik (Hukum Induksi Faraday).",
        "pinout": "2 Kaki kawat tanpa polaritas.",
        "usage": "Ditempatkan pada jalur power supply switching (SMPS) dan sirkuit filter LC bersama kapasitor.",
        "application": "Regulator tegangan step-down buck / boost converter, filter audio, transformator mini."
    },
    "Capacitor-10mf": {
        "raw_name": "Capacitor-10mf",
        "name": "Electrolytic Capacitor 10uF",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor elektrolit silinder 10 µF terpolarisasi untuk penyaring tegangan.",
        "icon": "database",
        "description": "Kapasitor aluminium elektrolitik bernilai 10 mikrofarad (10 µF). Memiliki tanda strip negatif putih pada badan silinder untuk membedakan polaritas.",
        "function": "Menyimpan muatan listrik sementara, menyaring riak tegangan (ripple filter), dan decoupling frekuensi rendah.",
        "working_principle": "Dua lapisan aluminium foil yang dipisahkan oleh kertas elektrolit menyimpan energi dalam medan listrik elektrostatik.",
        "pinout": "Kaki panjang = Positif (+), Kaki pendek bergaris = Negatif (-).",
        "usage": "Wajib diperhatikan polaritasnya! Pemasangan terbalik dapat merusak atau meledakkan kapasitor.",
        "application": "Filter catu daya mikrokontroler, sirkuit kopling audio, penstabil tegangan analog."
    },
    "Capacitor-470mf": {
        "raw_name": "Capacitor-470mf",
        "name": "Electrolytic Capacitor 470uF",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor elektrolit tabung berkapasitas besar 470 µF untuk reservoir daya.",
        "icon": "database",
        "description": "Kapasitor elektrolit dengan nilai kapasitas besar 470 mikrofarad (470 µF) yang mampu menyimpan cadangan muatan yang signifikan.",
        "function": "Meredam lonjakan arus mendadak (bulk capacitor), meratakan tegangan penyearah AC-DC, dan penyangga daya motor.",
        "working_principle": "Menyerap lonjakan tegangan dan menyuplai arus instan ketika beban tiba-tiba menarik daya besar.",
        "pinout": "Kaki panjang (+), Kaki pendek tanda strip (-).",
        "usage": "Pasang paralel antara jalur VCC dan GND pada input power supply rangkaian.",
        "application": "Power supply amplifier audio, buffer daya motor servo, adaptor switching 5V/12V."
    },
    "Film-Capacitor": {
        "raw_name": "Film-Capacitor",
        "name": "Film Capacitor (Polyester / Mylar)",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor film plastik non-polar dengan stabilitas dan keandalan tinggi.",
        "icon": "database",
        "description": "Kapasitor non-polar yang menggunakan film plastik tipis (seperti poliester, polipropilena) sebagai bahan dielektriknya. Sering berbentuk kotak merah/kuning atau oval hijau/cokelat.",
        "function": "Menghantarkan sinyal AC frekuensi tinggi tanpa distorsi dan menahan tegangan tinggi.",
        "working_principle": "Dielektrik film plastik berkualitas tinggi memberikan resistansi isolasi sangat besar dan losses dielektrik sangat rendah.",
        "pinout": "2 Kaki kawat tanpa polaritas (bebas bolak-balik).",
        "usage": "Bagus untuk rangkaian audio fidelity tinggi, snubber relay, dan crossover speaker.",
        "application": "Tapis frekuensi audio crossover, sirkuit peredam spark saklar, elektronika daya tinggi."
    },
    "High-Voltage-Ceramic-Capacitor": {
        "raw_name": "High-Voltage-Ceramic-Capacitor",
        "name": "High Voltage Ceramic Capacitor",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor keramik bulat biru/kuning tahan tegangan tinggi (1kV - 3kV+).",
        "icon": "shield-alert",
        "description": "Kapasitor cakram keramik yang dirancang khusus untuk beroperasi pada tegangan tembus tinggi hingga ribuan volt (1 kV - 3 kV atau lebih).",
        "function": "Meredam lonjakan tegangan petir/transien dan kopling tegangan AC tinggi.",
        "working_principle": "Material keramik berkekuatan dielektrik tinggi mencegah terjadinya loncatan percikan listrik antar elektroda.",
        "pinout": "2 Kaki kawat tanpa polaritas.",
        "usage": "Banyak dipakai pada bagian primer catu daya switching SMPS dan rangkaian penangkap tegangan lonjakan.",
        "application": "Rangkaian catu daya AC 220V, ballas lampu, proteksi surge TVS, generator pulsa tinggi."
    },
    "Low-Voltage-Ceramic-Capacitor": {
        "raw_name": "Low-Voltage-Ceramic-Capacitor",
        "name": "Ceramic Disc Capacitor",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor piringan keramik cokelat kecil bernilai pico/nanofarad (misal 100nF / 104).",
        "icon": "database",
        "description": "Kapasitor cakram keramik kecil berkode angka 3 digit (misalnya 104 = 100nF, 22 = 22pF). Sangat umum sebagai bypass kapasitor.",
        "function": "Membuang noise frekuensi tinggi ke ground (decoupling) tepat di dekat pin power IC.",
        "working_principle": "Memiliki impedansi sangat rendah pada frekuensi tinggi, sehingga noise gelombang radio langsung disalurkan ke ground.",
        "pinout": "2 Kaki kawat tanpa polaritas.",
        "usage": "Pasang sedekat mungkin dengan pin VCC dan GND mikrokontroler (kapasitor 100nF).",
        "application": "Osilator kristal (kapasitor 22pF), decoupling IC digital, radio tuner RF."
    },
    "MLC-Capacitor": {
        "raw_name": "MLC-Capacitor",
        "name": "MLCC (Multi-Layer Ceramic Capacitor)",
        "category": "Passive Components",
        "category_id": "passive",
        "short_desc": "Kapasitor keramik multi-lapis bertoleransi rapat dalam ukuran sangat kompak.",
        "icon": "layers",
        "description": "MLCC (Multi-Layer Ceramic Capacitor) dibuat dari puluhan hingga ratusan lapisan logam dan keramik tipis yang ditumpuk menjadi satu monolitik.",
        "function": "Menyediakan kapasitas besar dalam bentuk ultra-kompak untuk papan PCB modern.",
        "working_principle": "Struktur berlapis memperluas luas permukaan elektroda internal secara drastis sehingga menghasilkan kapasitas tinggi.",
        "pinout": "2 Terminal SMD atau through-hole berlapis timah.",
        "usage": "Standar industri untuk perataan sinyal digital kecepatan tinggi di smartphone dan motherboard.",
        "application": "Motherboard laptop, board smartphone, modul mikrokontroler SMD, radar miniature."
    },

    # 6. Power Components
    "1-5-Volt-Battery": {
        "raw_name": "1-5-Volt-Battery",
        "name": "1.5V Battery (AA / AAA Alkaline)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Sel baterai silinder standar 1.5 Volt tipe AA atau AAA.",
        "icon": "battery",
        "description": "Baterai elektrokimia primer silinder standar bertegangan nominal 1.5 Volt menggunakan kimia Karbon-Seng atau Alkaline Seng-Mangan Dioksida (Zn/MnO2).",
        "function": "Menyediakan sumber energi listrik DC portabel dan mandiri untuk perangkat elektronik.",
        "working_principle": "Reaksi reduksi-oksidasi kimia spontan melepaskan elektron dari anoda seng menuju katoda mangan dioksida.",
        "pinout": "Kutub Positif (+) menonjol, Kutub Negatif (-) rata di bagian bawah.",
        "usage": "Dapat dirangkai seri dalam battery holder (misal 2 baterai seri = 3.0V, 4 baterai seri = 6.0V).",
        "application": "Remote TV, senter, mainan robotik, jam dinding, modul pemantau nirkabel."
    },
    "3-3-Volt-Battery": {
        "raw_name": "3-3-Volt-Battery",
        "name": "3V Coin Battery (CR2032)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Baterai kancing lithium 3 Volt untuk memori RTC dan sensor ultra-tipis.",
        "icon": "circle-dot",
        "description": "Baterai koin lithium mangan dioksida (LiMnO2) seperti CR2032 dengan diameter 20 mm dan tebal 3.2 mm. Menghasilkan tegangan stabil 3.0V - 3.3V.",
        "function": "Mempertahankan daya jam RTC (Real Time Clock), BIOS komputer, dan remote car key.",
        "working_principle": "Reaksi lithium menghasilkan densitas energi tinggi dengan tingkat self-discharge sangat rendah (tahan hingga 5-10 tahun).",
        "pinout": "Permukaan atas dan tepi bertanda (+) adalah Positif, permukaan bawah bertekstur adalah Negatif (-).",
        "usage": "Dipasang pada soket baterai CR2032 koin di papan PCB.",
        "application": "Modul RTC DS3231, CMOS motherboard PC, tag bluetooth beacon, kalkulator tipis."
    },
    "9-Volt-Battery": {
        "raw_name": "9-Volt-Battery",
        "name": "9V Battery (6F22 Block)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Baterai kotak 9 Volt dengan konektor kancing snap-on ganda.",
        "icon": "battery-charging",
        "description": "Baterai berbentuk balok persegi panjang bertegangan nominal 9 Volt. Di dalamnya tersusun dari 6 sel silinder mini 1.5V yang terhubung secara seri.",
        "function": "Menyuplai daya tegangan 9V untuk mikrokontroler via pin Vin atau DC barrel jack.",
        "working_principle": "Tegangan akumulatif dari enam sel seri memberikan potensial 9 Volt untuk beban berdaya rendah hingga sedang.",
        "pinout": "Konektor snap ganda: Terminal kecil heksagonal Positif (+), Terminal besar melingkar Negatif (-).",
        "usage": "Gunakan kabel klip baterai 9V berkonektor DC barrel plug 2.1mm untuk dicolok langsung ke Arduino.",
        "application": "Multimeter digital portabel, mikrofon nirkabel, alarm asap detektor kebakaran, robot lab edukasi."
    },
    "Buck-Converter": {
        "raw_name": "Buck-Converter",
        "name": "Buck Converter (Step-Down LM2596)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Modul regulator switching penurun tegangan DC-DC dengan efisiensi tinggi hingga 92%.",
        "icon": "trending-down",
        "description": "Modul penurun tegangan switching efisien berbasis chip LM2596. Mampu menurunkan tegangan input DC (misal 12V-24V) menjadi tegangan output yang dapat diatur presisi (misal 5V atau 3.3V).",
        "function": "Menurunkan tegangan tinggi ke tegangan rendah yang aman untuk mikrokontroler tanpa menghasilkan panas berlebih.",
        "working_principle": "Menggunakan saklar PWM frekuensi tinggi (150 kHz), induktor, dan kapasitor filter untuk mentransfer daya secara efisien.",
        "pinout": "IN+ & IN- (Input DC), OUT+ & OUT- (Output DC teratur), Potensiometer multi-turn pengatur voltase.",
        "usage": "Hubungkan sumber daya ke IN+/IN-, putar obeng kecil pada potensiometer biru sambil mengukur tegangan OUT+/OUT- dengan multimeter.",
        "application": "Suplai daya robot dari baterai LiPo 3S 12V ke Arduino 5V, charger mobil USB, sistem panel surya."
    },
    "Bridge-Rectifier": {
        "raw_name": "Bridge-Rectifier",
        "name": "Bridge Rectifier (Diode Bridge)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Komponen penyearah gelombang penuh 4 dioda dalam satu paket untuk mengubah AC ke DC.",
        "icon": "shuffle",
        "description": "Konfigurasi jembatan 4 buah dioda penyearah yang dikemas dalam satu badan berkaki empat (seperti KBP206 atau DB107).",
        "function": "Mengubah tegangan bolak-balik (AC) dari trafo menjadi tegangan searah (DC) bergelombang penuh.",
        "working_principle": "Pada setiap setengah siklus gelombang AC, dua dioda menghantarkan arus secara bergantian sehingga polaritas output selalu positif searah.",
        "pinout": "4 Pin: Dua pin bergelombang (~ ~) untuk Input AC, Pin (+) untuk Output DC Positif, Pin (-) untuk Output DC Negatif.",
        "usage": "Ditempatkan tepat setelah trafo step-down dan sebelum kapasitor perata elektrolit besar.",
        "application": "Catu daya linier trafo, adaptor charger konvensional, inverter listrik, pengelas inverter."
    },
    "Fuse": {
        "raw_name": "Fuse",
        "name": "Glass / Ceramic Cartridge Fuse",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Komponen pengaman lebur untuk memutus sirkuit saat terjadi korsleting atau beban lebih.",
        "icon": "shield-check",
        "description": "Tabung kaca transparan atau keramik berisi kawat logam tipis berkalibrasi nilai arus tertentu (misal 1A, 2A, 5A, 10A).",
        "function": "Melindungi komponen mahal dan mencegah kebakaran akibat hubungan pendek (korsleting) arus listrik.",
        "working_principle": "Jika arus yang lewat melebihi batas ratingnya, kawat logam melebur (putus) akibat panas, sehingga aliran arus listrik terhenti seketika.",
        "pinout": "2 Cap logam di ujung silinder tabung.",
        "usage": "Dipasang seri pada jalur utama masukan daya fasa/positif menggunakan rumah sekring (fuse-base).",
        "application": "Power supply komputer, panel listrik rumah, multimeter pengaman proteksi input, amplifier audio."
    },
    "Fuse-Base": {
        "raw_name": "Fuse-Base",
        "name": "Fuse Base / Fuse Holder",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Dudukan rumah sekring untuk pemasangan dan penggantian fuse secara aman.",
        "icon": "box",
        "description": "Soket atau rumah dudukan berbahan isolator plastik tahan panas dan klip tembaga pegas yang menjepit sekring tabung kaca ukuran 5x20 mm atau 6x30 mm.",
        "function": "Memegang fuse dengan kuat pada PCB atau panel dan memudahkan penggantian jika fuse putus.",
        "working_principle": "Memberikan kontak resistansi rendah antar ujung kawat sekring dengan terminal kabel luar.",
        "pinout": "2 Kaki pin solder PCB atau terminal sekrup kabel panel.",
        "usage": "Solder pada PCB pada jalur input daya sebelum masuk ke saklar atau rangkaian utama.",
        "application": "Panel kotak sekring, PSU switching industri, trafo charger aki mobil."
    },
    "Heat-Sink": {
        "raw_name": "Heat-Sink",
        "name": "Heat Sink (Aluminium Radiator)",
        "category": "Power Components",
        "category_id": "power",
        "short_desc": "Pelepas panas berbahan sirip aluminium untuk mendinginkan transistor dan regulator daya.",
        "icon": "thermometer-snowflake",
        "description": "Blok logam paduan aluminium dengan banyak sirip-sirip vertikal yang dirancang untuk memperluas permukaan kontak termal dengan udara.",
        "function": "Menyerap panas dari komponen daya semikonduktor (seperti MOSFET, IC regulator LM7805) dan membuangnya ke udara sekitar.",
        "working_principle": "Konduksi termal menyerap panas dari casing komponen ke badan aluminium, lalu konveksi udara melepaskannya keluar.",
        "pinout": "Lubang baut M3 untuk memasang tab komponen TO-220/TO-247.",
        "usage": "Oleskan pasta termal (thermal paste) atau pasang mika isolator di antara komponen dan heatsink sebelum dibaut kencang.",
        "application": "Transistor final amplifier daya, regulator tegangan LM317/7805, pendingin prosesor PC, motor driver L298N."
    },

    # 7. Communication Module
    "Bluetooth-Module": {
        "raw_name": "Bluetooth-Module",
        "name": "Bluetooth Module (HC-05 / HC-06)",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Modul komunikasi nirkabel Bluetooth SPP (Serial Port Protocol) 2.4 GHz.",
        "icon": "bluetooth",
        "description": "Modul transceiver nirkabel Bluetooth klasik yang memungkinkan mikrokontroler berkomunikasi dengan smartphone Android atau PC via profil serial nirkabel.",
        "function": "Mengirim dan menerima data nirkabel jarak dekat (~10 meter) menggunakan komunikasi serial UART.",
        "working_principle": "Menerjemahkan data serial TX/RX dari mikrokontroler menjadi paket gelombang radio Bluetooth 2.4 GHz dan sebaliknya.",
        "pinout": "VCC (5V), GND, TXD (Sinyal serial keluar 3.3V), RXD (Sinyal serial masuk toleran 3.3V), STATE, EN/KEY.",
        "usage": "Hubungkan TXD modul ke RX Arduino, RXD modul ke TX Arduino (gunakan pembagi tegangan 5V ke 3.3V untuk pin RXD).",
        "application": "Kontrol robot mobil via aplikasi Android Bluetooth, remote control nirkabel, telemetry sensor nirkabel."
    },
    "GSM-Module": {
        "raw_name": "GSM-Module",
        "name": "GSM / GPRS Module (SIM800L)",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Modul seluler mini untuk mengirim SMS, panggilan suara, dan koneksi internet GPRS.",
        "icon": "signal",
        "description": "Modul seluler GSM/GPRS ultra-kompak yang dilengkapi slot Micro-SIM. Mampu beroperasi pada frekuensi Quad-Band 850/900/1800/1900 MHz.",
        "function": "Mengirim/menerima SMS, panggilan telepon darurat, dan mengunggah data sensor ke server cloud via koneksi data 2G GPRS.",
        "working_principle": "Mikrokontroler mengirimkan perintah AT Command standar Hayes melalui antarmuka serial UART ke modul SIM800L.",
        "pinout": "VCC (3.7V - 4.2V baterai Li-Ion), GND, SIM_TXD, SIM_RXD, RST, Ring Indicator (RI), Antena IPEX.",
        "usage": "Memerlukan catu daya arus puncak hingga 2 Ampere pada tegangan 3.7V-4.0V (gunakan buck converter atau baterai Li-Ion).",
        "application": "Sistem alarm maling via SMS darurat, pelacak GPS kendaraan via SMS/HTTP, remote reset BTS."
    },
    "NRF24L01": {
        "raw_name": "NRF24L01",
        "name": "NRF24L01+ 2.4GHz RF Module",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Modul radio frekuensi 2.4 GHz ultra-hemat daya dan berkecepatan data hingga 2 Mbps.",
        "icon": "radio",
        "description": "Transceiver nirkabel single chip pita 2.4 GHz ISM dari Nordic Semiconductor. Memiliki fitur auto-acknowledgement dan multi-channel transmisi.",
        "function": "Komunikasi nirkabel point-to-point atau point-to-multipoint antar mikrokontroler tanpa router Wi-Fi.",
        "working_principle": "Menggunakan modulasi GFSK pada frekuensi 2.4 GHz dengan protokol Enhanced ShockBurst bawaan perangkat keras.",
        "pinout": "8 Pin: VCC (3.3V saja!), GND, CSN, CE, MOSI, SCK, MISO, IRQ.",
        "usage": "Gunakan library `RF24`. Pasang kapasitor 10uF paralel pada pin VCC dan GND modul untuk kestabilan transmisi radio.",
        "application": "Remote joystick drone quadcopter, jaringan sensor nirkabel multi-node cerdas, telemetry telemetry robotik."
    },
    "FT-232-USB-Serial-Module": {
        "raw_name": "FT-232-USB-Serial-Module",
        "name": "FT232RL USB to Serial UART Module",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Konverter USB ke serial UART berkinerja tinggi berbasis chip FTDI FT232RL.",
        "icon": "usb",
        "description": "Modul adaptor yang menjembatani port USB komputer dengan antarmuka serial logika TTL mikrokontroler (Arduino Pro Mini, ESP32-CAM, router).",
        "function": "Memprogram mikrokontroler tanpa USB onboard dan memonitor komunikasi serial teks di komputer.",
        "working_principle": "Driver FTDI mengubah paket USB menjadi aliran byte data serial UART full duplex dengan buffer internal FIFO.",
        "pinout": "DTR (Auto-reset), RXD, TXD, VCC (jumper 3.3V / 5V), CTS, GND.",
        "usage": "Pilih tegangan logika 3.3V atau 5V via jumper header. Hubungkan TXD ke RX board target, dan RXD ke TX target.",
        "application": "Flashing firmware ESP32-CAM, Arduino Pro Mini, unbricking router mikrotik, konsol UART Linux."
    },
    "USB-TTL-ESP01": {
        "raw_name": "USB-TTL-ESP01",
        "name": "ESP-01 USB Flasher Programmer",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Adaptor USB khusus dengan soket 2x4 pin untuk menghubungkan ESP-01 langsung ke PC.",
        "icon": "hard-drive",
        "description": "Dongle USB yang dirancang khusus dengan soket 8-pin untuk menancapkan modul ESP-01 / ESP-01S secara langsung tanpa kabel jumper kusut.",
        "function": "Memprogram dan menguji modul ESP8266 ESP-01 secara praktis lewat port USB laptop.",
        "working_principle": "Menggunakan chip CH340G USB to serial dengan regulator 3.3V onboard untuk menyuplai arus modul ESP-01.",
        "pinout": "Port USB Type-A jantan, soket female header 2x4 pin sesuai pinout ESP-01.",
        "usage": "Tancapkan modul ESP-01 ke soket. Untuk mode flash, pastikan GPIO 0 dihubungkan ke GND saat dicolokkan ke USB.",
        "application": "Pengembangan IoT ESP-01, flashing AT-firmware atau kode Arduino, pengujian modul Wi-Fi cepat."
    },
    "RFID-Scanner": {
        "raw_name": "RFID-Scanner",
        "name": "RFID Reader Module (RC522)",
        "category": "Communication Module",
        "category_id": "communication",
        "short_desc": "Modul pembaca kartu dan gantungan kunci RFID frekuensi 13.56 MHz (Mifare).",
        "icon": "credit-card",
        "description": "Modul pembaca kartu nirkabel jarak dekat (NFC / RFID) frekuensi 13.56 MHz berbasis chip Philips/NXP MFRC522.",
        "function": "Membaca UID (nomor identitas unik) kartu/tag RFID serta menulis data pada memori kartu Mifare.",
        "working_principle": "Antena kumparan PCB memancarkan medan elektromagnetik 13.56 MHz yang menyalakan chip pasif pada kartu melalui induksi resonansi.",
        "pinout": "3.3V (Hanya 3.3V!), RST, GND, MISO, MOSI, SCK, NSS/SDA (SPI Interface), IRQ.",
        "usage": "Gunakan library `MFRC522`. Hubungkan jalur SPI ke Arduino (pin 10-13) dengan tegangan VCC 3.3V.",
        "application": "Sistem absensi siswa/karyawan, kunci pintu pintar hotel, pembayaran e-toll miniature, loker otomatis."
    },

    # 8. Driver & Controller
    "Motor-Driver": {
        "raw_name": "Motor-Driver",
        "name": "Motor Driver (L298N Dual H-Bridge)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Modul driver motor ganda H-Bridge bertenaga tinggi untuk kendali 2 motor DC atau 1 stepper.",
        "icon": "cpu",
        "description": "Modul penggerak motor populer berbasis IC L298N ganda H-Bridge yang dilengkapi heatsink aluminium tebal dan regulator 5V onboard.",
        "function": "Mengontrol arah putaran (maju/mundur) dan kecepatan (PWM) dari 2 motor DC secara terpisah atau 1 motor stepper.",
        "working_principle": "Sirkuit H-Bridge transistor daya internal memungkinkan pembalikan polaritas tegangan pada kedua kutub motor.",
        "pinout": "Power: VMS (5V-35V Motor), GND, 5V Logic. Kontrol: ENA, IN1, IN2 (Motor A), IN3, IN4, ENB (Motor B). Output: OUT1, OUT2, OUT3, OUT4.",
        "usage": "Beri sinyal PWM pada pin ENA/ENB untuk mengatur kecepatan motor, sinyal digital pada IN1-IN4 untuk mengatur arah.",
        "application": "Robot mobil roda 4/roda 2, robot tangki, kendali conveyor belt, aktuator linier otomatis."
    },
    "Relay-Module": {
        "raw_name": "Relay-Module",
        "name": "Relay Module (5V Single / Dual Channel)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Saklar elektromekanik dengan optocoupler untuk mengontrol beban listrik AC 220V dari mikrokontroler 5V.",
        "icon": "toggle-right",
        "description": "Saklar magnetik terisolasi opto-isolator yang memungkinkan mikrokontroler bertegangan rendah (5V) menyalakan dan mematikan peralatan listrik bertegangan tinggi hingga 250V AC / 10A.",
        "function": "Mengontrol peralatan listrik rumah tangga (lampu 220V, pompa air AC, pemanas) secara digital.",
        "working_principle": "Arus kecil pada koil relay menghasilkan medan magnet yang menarik armatur logam mekanik untuk menghubungkan kontak NO atau NC.",
        "pinout": "Input: VCC (5V), GND, IN (Active Low). Output Terminal: COM (Common), NO (Normally Open), NC (Normally Closed).",
        "usage": "Hubungkan beban pada pin COM dan NO; ketika pin IN ditarik LOW oleh mikrokontroler, relay 'klik' dan beban menyala.",
        "application": "Smart home saklar lampu internet, pompa irigasi AC otomatis, kontrol pemanas kandang ternak."
    },
    "MOSFET": {
        "raw_name": "MOSFET",
        "name": "Power MOSFET (IRF520 / IRFZ44N)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Transistor efek medan gerbang terisolasi untuk saklar arus tinggi berkecepatan sangat cepat.",
        "icon": "git-commit",
        "description": "Transistor daya N-Channel MOSFET berkemasan TO-220 yang mampu menghantarkan arus puluhan ampere dengan resistansi On (Rds-on) sangat rendah.",
        "function": "Saklar elektronik solid-state kecepatan tinggi untuk beban arus besar (LED strip berdaya besar, pemanas, motor).",
        "working_principle": "Tegangan pada Gate (Vgs) menciptakan saluran konduksi elektron antara Drain dan Source tanpa memerlukan arus gate konstan.",
        "pinout": "Pin 1: Gate (G), Pin 2: Drain (D), Pin 3: Source (S).",
        "usage": "Beri resistor pull-down 10k pada Gate ke GND untuk memastikan MOSFET mati saat mikrokontroler booting.",
        "application": "Pengatur kecerahan lampu LED strip PWM 12V, pemanas heated bed printer 3D, pengatur kecepatan motor DC efisien."
    },
    "IGBT": {
        "raw_name": "IGBT",
        "name": "IGBT (Insulated Gate Bipolar Transistor)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Komponen saklar daya tinggi yang menggabungkan kontrol mudah MOSFET dan kemampuan tegangan tinggi BJT.",
        "icon": "zap",
        "description": "Semikonduktor daya berkemasan TO-247/TO-220 yang menggabungkan keunggulan input impedansi tinggi gerbang MOSFET dan kemampuan saturasi tegangan rendah transistor bipolar (BJT).",
        "function": "Mengendalikan daya listrik sangat besar (ratusan hingga ribuan volt dan puluhan ampere).",
        "working_principle": "Gerbang terisolasi mengontrol konduksi arus tinggi antara Kolektor dan Emitor dengan losses konduksi minimal.",
        "pinout": "Pin 1: Gate (G), Pin 2: Collector (C), Pin 3: Emitter (E).",
        "usage": "Memerlukan driver gate khusus (misal 15V) untuk memastikan saklar hidup sempurna pada frekuensi tinggi.",
        "application": "Kompor induksi listrik (induction cooker), inverter motor kereta listrik & mobil listrik EV, mesin las listrik."
    },
    "BJT-Transistor": {
        "raw_name": "BJT-Transistor",
        "name": "BJT Transistor (NPN / PNP e.g. 2N2222, BC547)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Transistor bipolar sambungan untuk penguatan sinyal audio dan saklar elektronik arus kecil.",
        "icon": "split",
        "description": "Transistor sambungan bipolar NPN atau PNP kemasan TO-92 atau TO-18 yang dikendalikan oleh arus input pada basisnya.",
        "function": "Menguatkan sinyal analog kecil (audio/radio) atau bertindak sebagai saklar digital arus rendah (<800 mA).",
        "working_principle": "Arus kecil pada terminal Basis mengontrol aliran arus yang jauh lebih besar dari Kolektor ke Emitor (penguatan beta hFE).",
        "pinout": "3 Kaki: Kolektor (C), Basis (B), Emitor (E).",
        "usage": "Wajib memasang resistor pembatas arus pada pin Basis (biasanya 1kΩ - 10kΩ) dari pin mikrokontroler.",
        "application": "Penggerak buzzer, pemicu koil relay 5V, penguat mikrofon preamp, saklar transistor logika."
    },
    "Diode": {
        "raw_name": "Diode",
        "name": "Rectifier Diode (1N4007 / 1N4148)",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Komponen semikonduktor satu arah untuk penyearahan arus dan proteksi polaritas.",
        "icon": "arrow-right",
        "description": "Dioda sambungan P-N silikon standar (seperti seri 1N4007 berkapasitas 1A 1000V). Memiliki cincin cincin perak penanda katoda.",
        "function": "Mengalirkan arus listrik hanya ke satu arah dan memblokir aliran arus arah sebaliknya.",
        "working_principle": "Arus maju (forward bias) melintasi sambungan semikonduktor dengan jatuh tegangan ~0.7V, sedangkan tegangan balik ditahan (reverse bias).",
        "pinout": "Badan hitam = Anoda (+), Ujung bergaris perak/putih = Katoda (-).",
        "usage": "Gunakan sebagai dioda flyback paralel terbalik pada koil relay/motor untuk melindungi mikrokontroler dari lonjakan ggl induksi balik.",
        "application": "Proteksi polaritas terbalik baterai, penyearah AC ke DC, flyback diode relay induktif."
    },
    "Zener-Diode": {
        "raw_name": "Zener-Diode",
        "name": "Zener Diode",
        "category": "Driver & Controller",
        "category_id": "driver_controller",
        "short_desc": "Dioda khusus yang mempertahankan tegangan stabil saat mengalami breakdown tegangan mundur.",
        "icon": "minimize-2",
        "description": "Dioda silikon berdoping tinggi kemasan kaca oranye yang dirancang bekerja secara stabil pada daerah tegangan tembus balik (Zener breakdown voltage).",
        "function": "Menjadi penstabil tegangan referensi dan proteksi tegangan lebih (overvoltage protection).",
        "working_principle": "Jika tegangan mundur melebihi tegangan Zener ratingnya (misal 5.1V), dioda menghantarkan arus untuk menjaga tegangan tetap stabil di nilai tersebut.",
        "pinout": "Anoda (+) dan Katoda bergaris hitam (-).",
        "usage": "Pasang secara reverse bias seri dengan resistor pembatas arus ke sumber tegangan.",
        "application": "Pembatas tegangan input ADC 3.3V/5V, regulator tegangan referensi sederhana, proteksi surge sirkuit komunikasi."
    },

    # 9. Other Electronics
    "Breadboard": {
        "raw_name": "Breadboard",
        "name": "Solderless Breadboard (400 / 830 Points)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Papan eksperimen bebas solder dengan ratusan lubang klip berpegas untuk merakit prototipe rangkaian.",
        "icon": "grid",
        "description": "Papan plastik putih berlubang grid 2.54 mm standar yang di dalamnya terdapat deretan klip logam pegas penghantar untuk merangkai komponen elektronik tanpa perlu menyolder.",
        "function": "Tempat merakit dan menguji rangkaian elektronika sementara secara cepat dan fleksibel.",
        "working_principle": "Lubang pada kolom 5 titik (a-e dan f-j) terhubung secara vertikal, sedangkan jalur rel daya atas dan bawah terhubung secara horizontal.",
        "pinout": "Jalur Rel Daya Positif (+) merah, Negatif (-) biru, serta Baris terminal komponen tengah (a,b,c,d,e dan f,g,h,i,j).",
        "usage": "Tancapkan kaki komponen dan kabel jumper; cabut kembali dengan mudah tanpa merusak komponen.",
        "application": "Praktikum laboratorium elektronika, prototyping proyek mikrokontroler, uji coba sensor dan IC."
    },
    "Keypad": {
        "raw_name": "Keypad",
        "name": "Matrix Keypad (4x4 Membrane / Tactile)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Papan tombol membran matriks 16 tombol (0-9, A-D, *, #) untuk input angka dan perintah.",
        "icon": "layout-grid",
        "description": "Modul keypad fleksibel dengan 16 tombol yang disusun dalam formasi matriks 4 baris dan 4 kolom.",
        "function": "Memberikan antarmuka input angka PIN, password keamanan, dan pemilihan menu pada mikrokontroler.",
        "working_principle": "Menggunakan metode pemindaian baris-kolom (matrix scanning), hanya membutuhkan 8 pin mikrokontroler untuk membaca 16 tombol unik.",
        "pinout": "Konektor female 8 Pin: 4 Pin Baris (Row 1-4) dan 4 Pin Kolom (Col 1-4).",
        "usage": "Gunakan library `Keypad.h` di Arduino untuk mendeklarasikan peta karakter tombol dengan mudah.",
        "application": "Kunci pintu brankas kode PIN, mesin absensi, kalkulator mini, pengatur timer industri."
    },
    "Pin-Header": {
        "raw_name": "Pin-Header",
        "name": "Pin Header (Male / Female 2.54mm)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Deretan pin konektor logam berjarak standar 2.54 mm untuk sambungan kabel dan modul.",
        "icon": "align-justify",
        "description": "Strip konektor listrik berupa deretan pin jarum kuningan berlapis timah atau soket berjarak pitch standar 2.54 mm (0.1 inci).",
        "function": "Menyediakan titik koneksi kabel jumper antar papan sirkuit PCB dan modul pendukung.",
        "working_principle": "Kontak logam mekanis langsung menghantarkan arus listrik sinyal dan daya antar konektor.",
        "pinout": "Tersedia tipe Male (jarum jantan), Female (lubang betina), lurus (straight), maupun siku (right-angle).",
        "usage": "Solder pada lubang tepian PCB untuk menghubungkan kabel jumper Dupont.",
        "application": "Konektor pada Arduino shield, modul sensor, koneksi pita flat kabel IDE, expansion port."
    },
    "Push-Switch": {
        "raw_name": "Push-Switch",
        "name": "Push Switch (Latching / Momentary Button)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Saklar tombol tekan untuk menyambung atau memutus arus dengan gaya tekan.",
        "icon": "square",
        "description": "Saklar mekanik tombol berukuran sedang dengan pegas pengembali atau mekanisme pengunci (latching) yang dapat dipasang di panel bodi proyek.",
        "function": "Saklar utama ON/OFF daya atau tombol aksi berukuran mantap pada panel box elektronika.",
        "working_principle": "Menekan tombol mendorong piringan kontak tembaga menghubungkan dua kutub terminal listrik.",
        "pinout": "2 Pin (SPST) atau 3-6 Pin (SPDT / DPDT).",
        "usage": "Pasang di lubang panel box alat kontrol untuk kemudahan pengoperasian oleh pengguna.",
        "application": "Tombol power box instrumen, bel darurat, pedal mesin, tombol start/stop mesin pabrik."
    },
    "Rocker-Switch": {
        "raw_name": "Rocker-Switch",
        "name": "Rocker Switch (KCD1 ON-OFF)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Saklar jungkit bodi plastik dengan simbol 'I' (ON) dan 'O' (OFF).",
        "icon": "power",
        "description": "Saklar saklar jungkit (rocker) snap-in yang berayun maju-mundur saat satu sisi ditekan untuk membuka atau menutup sirkuit.",
        "function": "Saklar saklar daya utama perangkat elektronik rumah tangga dan casing instrumen lab.",
        "working_principle": "Mekanisme jungkit pegas internal mengunci posisi kontak tertutup atau terbuka dengan stabil.",
        "pinout": "2 Pin untuk tipe standar atau 3 Pin dengan lampu indikator neon/LED bawaan.",
        "usage": "Potong lubang persegi panjang pada bodi panel, tekan saklar hingga terkunci oleh klip snap-in.",
        "application": "Saklar power supply ATX, stop kontak kabel roll, adaptor catu daya, amplifier audio."
    },
    "Tact-Switch": {
        "raw_name": "Tact-Switch",
        "name": "Tactile Push Button (4-Pin Micro Switch)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Tombol mikro sentuh momentary berbunyi klik saat ditekan.",
        "icon": "mouse-pointer-click",
        "description": "Tombol taktil miniatur berukuran 6x6 mm dengan umpan balik klik fisik yang jelas saat ditekan dan kembali terbuka saat dilepas.",
        "function": "Tombol reset, navigasi menu, tombol input hitungan, dan pemicu sinyal digital ke mikrokontroler.",
        "working_principle": "Kubah logam fleksibel melengkung ke bawah menghubungkan kaki terminal saat ditekan.",
        "pinout": "4 Kaki: Kaki sisi bersebelahan terhubung berpasangan.",
        "usage": "Gunakan mode `pinMode(pin, INPUT_PULLUP)` di Arduino untuk kemudahan tanpa perlu resistor eksternal.",
        "application": "Tombol Reset Arduino, kontrol volume headset, tombol gamepad stik, remote control."
    },
    "Taper-Potentiometer": {
        "raw_name": "Taper-Potentiometer",
        "name": "Rotary Potentiometer (Rotary Volume Knob)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Resistor variabel putar dengan poros untuk pengaturan volume, kecepatan, dan tuning.",
        "icon": "gauge",
        "description": "Resistor variabel 3 terminal dengan lintasan karbon melingkar dan wiper bergerak yang diputar menggunakan kenop poros.",
        "function": "Mengatur resistansi atau tegangan analog secara manual dan kontinu (misal mengatur volume suara atau kecerahan lampu).",
        "working_principle": "Memutar poros menggeser wiper di sepanjang lintasan hambatan, mengubah rasio pembagi tegangan secara proporsional.",
        "pinout": "Pin 1: VCC (5V), Pin 2 (Tengah): Wiper Tegangan Output Analog, Pin 3: GND.",
        "usage": "Hubungkan pin tengah ke pin analog ADC Arduino untuk membaca nilai input analog 0-1023.",
        "application": "Knob pengatur volume speaker, pengatur kecepatan motor, kalibrasi instrumen sensor, mixer audio."
    },
    "Trimmer-Potentiometer": {
        "raw_name": "Trimmer-Potentiometer",
        "name": "Trimpot (Trimmer Potentiometer 3296 / 103)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Resistor variabel mini berpresisi tinggi yang diatur menggunakan obeng obeng minus.",
        "icon": "settings",
        "description": "Potensiometer kompak yang dirancang untuk disolder permanen pada papan PCB dan disetel sesekali untuk kalibrasi sirkuit.",
        "function": "Menyetel ambang batas sensitivitas sensor (threshold komparator) dan kontras layar LCD.",
        "working_principle": "Mekanisme sekrup cacing multi-turn (10-25 putaran) memberikan akurasi pengaturan hambatan yang sangat halus.",
        "pinout": "3 Kaki segaris atau segitiga: Kaki 1 & 3 terminal ujung resistansi, Kaki 2 wiper tengah.",
        "usage": "Gunakan obeng minus kecil untuk memutar sekrup kuningan di atas trimpot secara perlahan.",
        "application": "Pengatur kontras layar LCD 16x2, kalibrasi modul sensor inframerah dan sensor gas, tuning catu daya."
    },
    "IC-Chip": {
        "raw_name": "IC-Chip",
        "name": "Integrated Circuit (DIP IC)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Sirkuit terpadu semikonduktor dalam kemasan DIP hitam berkaki ganda.",
        "icon": "cpu",
        "description": "Komponen silikon mikroelektronika terpadu berkemasan Dual In-line Package (DIP) hitam yang mengemas ribuan hingga jutaan transistor, resistor, dan gerbang logika.",
        "function": "Menjalankan fungsi logika terprogram, op-amp analog (LM358), timer (NE555), shift register (74HC595), atau mikrokontroler (ATmega328P).",
        "working_principle": "Mikroskopis sirkuit terpadu pada wafer silikon mengeksekusi fungsi komputasi atau pengolahan sinyal terpadu.",
        "pinout": "DIP-8, DIP-14, DIP-16, DIP-28 dengan lekukan penanda pin 1 di salah satu ujung kemasan.",
        "usage": "Pasang pada soket IC (IC-base) untuk memudahkan penggantian chip tanpa menyolder ulang.",
        "application": "Timer osilator 555, penguat audio, mikrokontroler, memori EEPROM, gerbang logika digital."
    },
    "IC-Base-14-Pin": {
        "raw_name": "IC-Base-14-Pin",
        "name": "14-Pin IC Socket (DIP-14)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Soket dudukan IC 14-pin untuk melindungi chip dari panas solder.",
        "icon": "grid",
        "description": "Soket perantara 14 pin (2 baris x 7 lubang berjarak 7.62 mm) yang disolder permanen pada PCB agar chip IC 14-pin dapat ditancapkan secara bebas.",
        "function": "Melindungi chip IC yang sensitif terhadap panas saat penyolderan dan memudahkan penggantian jika chip rusak.",
        "working_principle": "Pegas kontak kuningan ganda di dalam lubang menjepit kaki IC secara kokoh dan menghantarkan listrik dengan stabil.",
        "pinout": "14 Lubang pin dengan takik penanda posisi pin 1 di bagian atas.",
        "usage": "Solder soket terlebih dahulu pada papan PCB, kemudian tancapkan IC 14-pin (seperti gerbang logika 74HC00/74HC14) ke soket.",
        "application": "Rangkaian digital logika TTL/CMOS 14-pin, synthesizer audio, kit modul praktikum sekolah."
    },
    "IC-Base-28-Pin": {
        "raw_name": "IC-Base-28-Pin",
        "name": "28-Pin IC Socket (DIP-28)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Soket dudukan IC 28-pin lebar, standar untuk chip mikrokontroler ATmega328P.",
        "icon": "grid",
        "description": "Soket dudukan 28 pin (2 baris x 14 pin) berjarak standar 0.3 inci (narrow) atau 0.6 inci (wide) yang umum digunakan untuk mikrokontroler papan Arduino Uno.",
        "function": "Memungkinkan mikrokontroler ATmega328P dipasang dan dicabut kapan saja untuk diprogram secara eksternal.",
        "working_principle": "Menghubungkan 28 jalur I/O mikrokontroler ke jalur PCB tanpa kontak solder langsung pada badan chip.",
        "pinout": "28 Lubang pin kontak ganda dengan tanda cekungan setengah lingkaran di ujung pin 1.",
        "usage": "Solder pada board Arduino Uno atau kit DIY mandiri, pasang ATmega328P dengan hati-hati agar tidak ada kaki yang tertekuk.",
        "application": "Papan Arduino Uno DIY, sistem kontrol industri berbasis ATmega, programmer chip AVR."
    },
    "Shield-ESP32": {
        "raw_name": "Shield-ESP32",
        "name": "ESP32 Expansion Shield",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Papan ekspansi terminal sekrup dan daya untuk modul ESP32 NodeMCU 30/38 Pin.",
        "icon": "layers",
        "description": "Papan ekspansi (breakout expansion shield) yang dilengkapi jack adaptor DC daya, regulator voltase mandiri, dan terminal koneksi 3-pin (Signal, VCC, GND) untuk memudahkan kabel sensor.",
        "function": "Mempermudah perakitan kabel sensor dan aktuator ke ESP32 tanpa perlu membuat rangkaian kabel jumper yang rumit.",
        "working_principle": "Meneruskan setiap pin GPIO ESP32 ke pin header servo berpasangan daya (G-V-S) dan jack daya DC 6-12V.",
        "pinout": "Soket ESP32 30/38 pin, DC Jack 2.1mm, baris header Servo (GND-VCC-Signal) untuk tiap GPIO.",
        "usage": "Tancapkan board ESP32 ke soket shield, sambungkan adaptor 9V-12V ke DC jack untuk menyuplai servo bertenaga besar.",
        "application": "Proyek robotika multi-servo ESP32, gateway sensor IoT smart home, otomasi laboratorium cerdas."
    },
    "LED-Light": {
        "raw_name": "LED-Light",
        "name": "LED (Light Emitting Diode 5mm)",
        "category": "Other Electronics",
        "category_id": "other",
        "short_desc": "Dioda pemancar cahaya semikonduktor 5mm hemat energi untuk indikator visual.",
        "icon": "lightbulb",
        "description": "Dioda semikonduktor optoelektronik berkubah epoksi transparan atau berwarna (merah, hijau, biru, kuning, putih) yang memancarkan cahaya terang saat dialiri arus searah.",
        "function": "Indikator visual status rangkaian (aktif/nonaktif, transmisi data RX/TX, alarm peringatan).",
        "working_principle": "Proses elektroluminesensi: rekombinasi elektron dan lubang (hole) pada persimpangan P-N melepaskan energi foton cahaya tampak.",
        "pinout": "Kaki panjang = Anoda (+), Kaki pendek dengan sisi kubah rata = Katoda (-).",
        "usage": "Wajib dipasang seri dengan resistor pembatas arus (220Ω - 1kΩ) untuk mencegah LED terbakar akibat arus lebih.",
        "application": "Proyek 'Blink' dasar pemula, lampu indikator power, display lampu lalu lintas mini, pencahayaan hias."
    }
}

def get_all_components():
    """Mengembalikan semua data komponen sebagai list."""
    return list(COMPONENTS_DATA.values())

def get_component(raw_name_or_key: str):
    """Mencari data komponen berdasarkan nama mentah atau nama tampilannya."""
    if raw_name_or_key in COMPONENTS_DATA:
        return COMPONENTS_DATA[raw_name_or_key]
    
    # Cari dengan perbandingan case-insensitive atau pembersihan tanda minus
    cleaned = raw_name_or_key.strip().lower().replace(" ", "-")
    for key, comp in COMPONENTS_DATA.items():
        if key.lower() == cleaned or comp["name"].lower() == raw_name_or_key.strip().lower():
            return comp
    return None

def answer_ai_query(question: str, context_component: str = None) -> dict:
    """
    Knowledge engine sederhana untuk ElectroVision AI Assistant.
    Memberikan jawaban teknis akurat dan ramah tentang komponen elektronika,
    pinout, fungsi, prinsip kerja, serta contoh pemrograman Arduino/ESP32.
    """
    q = question.lower().strip()
    
    # Cari komponen yang menjadi konteks
    comp = None
    if context_component:
        comp = get_component(context_component)
    
    if not comp:
        # Coba deteksi apakah ada nama komponen di dalam pertanyaan pengguna
        for key, c in COMPONENTS_DATA.items():
            if c["name"].lower() in q or key.lower() in q or key.replace("-", " ").lower() in q:
                comp = c
                break

    # 1. Jika pengguna menanyakan tentang fungsi / apa itu
    if comp and any(k in q for k in ["fungsi", "apa itu", "kegunaan", "pengertian", "apa fungsi"]):
        return {
            "source": "knowledge_base",
            "component": comp["name"],
            "reply": f"### 💡 Fungsi {comp['name']}\n\n**{comp['name']}** ({comp['category']}):\n{comp['description']}\n\n**Fungsi Utama:**\n{comp['function']}\n\n**Contoh Penerapan:**\n{comp['application']}"
        }

    # 2. Jika menanyakan tentang pinout / kaki / koneksi
    if comp and any(k in q for k in ["pin", "pinout", "kaki", "terminal", "koneksi", "sambungan"]):
        return {
            "source": "knowledge_base",
            "component": comp["name"],
            "reply": f"### 🔌 Pinout & Koneksi {comp['name']}\n\nBerikut konfigurasi pin untuk **{comp['name']}**:\n\n- **Pinout:** {comp['pinout']}\n- **Petunjuk Penggunaan:** {comp['usage']}\n\n> **Tips Keamanan:** Selalu pastikan polaritas dan batas tegangan kerja komponen sebelum menyalakan daya untuk menghindari kerusakan."
        }

    # 3. Jika menanyakan prinsip kerja / cara kerja
    if comp and any(k in q for k in ["prinsip kerja", "cara kerja", "bagaimana bekerja", "cara kerjanya"]):
        return {
            "source": "knowledge_base",
            "component": comp["name"],
            "reply": f"### ⚙️ Prinsip Kerja {comp['name']}\n\n**Prinsip Kerja:**\n{comp['working_principle']}\n\n**Cara Penggunaan:**\n{comp['usage']}"
        }

    # 4. Jika menanyakan perbandingan Arduino Uno vs ESP32
    if ("arduino" in q and "esp32" in q) or ("perbedaan" in q and ("arduino" in q or "esp32" in q)):
        return {
            "source": "knowledge_base",
            "component": "Perbandingan Arduino Uno vs ESP32",
            "reply": """### ⚡ Perbandingan Arduino UNO vs ESP32

| Fitur | Arduino UNO | ESP32 |
|---|---|---|
| **Prosesor** | 8-bit ATmega328P (16 MHz) | 32-bit Dual-Core Xtensa (240 MHz) |
| **Konektivitas** | Tidak ada (perlu modul tambahan) | Wi-Fi 802.11 b/g/n & Bluetooth 4.2 BLE Onboard |
| **RAM / Flash** | 2 KB SRAM / 32 KB Flash | 520 KB SRAM / 4-16 MB Flash |
| **Tegangan Logika** | 5V | 3.3V (Hati-hati tidak toleran 5V) |
| **Ideal Untuk** | Pemula, edukasi, logika sederhana | IoT, smart home, web server, pemrosesan cepat |

**Kesimpulan:** Gunakan **Arduino Uno** untuk belajar dasar elektronika dengan proteksi tegangan 5V yang tangguh. Gunakan **ESP32** jika proyek Anda membutuhkan koneksi internet, Wi-Fi, atau komputasi cepat."""
        }

    # 5. Jika menanyakan cara menggunakan sensor ultrasonik
    if "ultrasonic" in q or "sonar" in q or "hc-sr04" in q:
        return {
            "source": "knowledge_base",
            "component": "Sonar Sensor (HC-SR04)",
            "reply": """### 📡 Cara Menggunakan Sensor Ultrasonik HC-SR04

Sensor **HC-SR04** mengukur jarak menggunakan gelombang suara berkecepatan 340 m/s.

#### Rangkaian ke Arduino:
- **VCC** ➜ Pin 5V Arduino
- **GND** ➜ Pin GND Arduino
- **Trig** ➜ Pin Digital 9
- **Echo** ➜ Pin Digital 10

#### Contoh Kode Arduino:
```cpp
const int trigPin = 9;
const int echoPin = 10;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  float distanceCm = duration * 0.034 / 2;

  Serial.print("Jarak: ");
  Serial.print(distanceCm);
  Serial.println(" cm");
  delay(200);
}
```"""
        }

    # 6. Jika komponen ditemukan tetapi pertanyaan umum
    if comp:
        return {
            "source": "knowledge_base",
            "component": comp["name"],
            "reply": f"""### 🔍 Analisis Komponen: {comp['name']}

**Kategori:** {comp['category']}  
**Ringkasan:** {comp['short_desc']}

- **Fungsi Utama:** {comp['function']}
- **Prinsip Kerja:** {comp['working_principle']}
- **Pinout:** {comp['pinout']}
- **Tips Penggunaan:** {comp['usage']}
- **Contoh Aplikasi:** {comp['application']}

*Ada hal spesifik yang ingin Anda tanyakan seputar kode program atau skema rangkaian {comp['name']}?*"""
        }

    # 7. Respon default jika pertanyaan umum tentang elektronika
    return {
        "source": "assistant",
        "component": None,
        "reply": f"""Halo! Saya **ElectroVision AI Assistant** ⚡

Saya siap membantu Anda memahami **65 komponen elektronika** yang dapat dideteksi oleh model YOLO11s sistem ini.

**Anda dapat bertanya mengenai:**
- Fungsi dan prinsip kerja komponen (misal: *"Apa fungsi ESP32?"*, *"Bagaimana cara kerja relay?"*)
- Konfigurasi pinout dan cara merangkai komponen ke Arduino / ESP32.
- Contoh kode pemrograman Arduino IDE / MicroPython.
- Perbedaan antar komponen (misal: *"Perbedaan Arduino Uno dan ESP32"*).

💡 *Tips: Anda juga bisa menyalakan kamera dan mendeteksi komponen terlebih dahulu, lalu klik tombol **Tanya AI** untuk analisis otomatis!*"""
    }
