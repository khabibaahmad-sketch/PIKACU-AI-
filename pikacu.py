import os
import time
import base64
import streamlit as st
from google import genai
from google.genai import types

# Setting Halaman Utama Web
st.set_page_config(page_title="PIKACU AI v4 SUPER", page_icon="⚡", layout="wide")

# ==========================================
# KONFIGURASI UTAMA & API KEY
# ==========================================
os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6Jgj6a8rQkyiTtjsGYo5Yg9T5tddDSX0-8JuJvVFu9D9g"
client = genai.Client()

MASKOT_FILENAME = "pikacu.png" 

def get_base64_img(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_img(MASKOT_FILENAME)
bg_style = f"data:image/png;base64,{img_base64}" if img_base64 else ""

# ==========================================
# ⚡ INTRO ANIMASI PETIR & SUARA PIKACHU ORIGINAL ⚡
# ==========================================
if "intro_done" not in st.session_state:
    # Link Suara Pikachu Asli dari Film Anime
    sound_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptrackid=553823"
    
    st.markdown(f"""
        <div id="intro-screen" style="
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: #111111; z-index: 99999; display: flex; flex-direction: column;
            justify-content: center; align-items: center; overflow: hidden; font-family: sans-serif;">
            
            <!-- Audio Suara Pikachu -->
            <audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>
            
            <div style="position: relative; width: 300px; height: 300px; display: flex; justify-content: center; align-items: center;">
                <!-- Efek Petir Menggelegar -->
                <div class="lightning-bolt">⚡</div>
                
                <!-- Kepala Pikachu Keluar Dari Petir -->
                <div class="pikachu-head-box">
                    <img src="{bg_style}" style="width: 180px; height: auto;">
                </div>
            </div>
            
            <h2 style="color: #FFE000; text-align: center; font-size: 28px; margin-top: 20px; font-weight: bold; text-shadow: 0 0 10px #FFE000;">
                PIKACU AI v4 LOADING...
            </h2>

            <style>
                /* Animasi Petir Ditengah */
                @keyframes thunder {{
                    0% {{ transform: scale(0.3) rotate(0deg); opacity: 0; }}
                    30% {{ transform: scale(1.3) rotate(-10deg); opacity: 1; filter: drop-shadow(0 0 20px #FFF); }}
                    45% {{ transform: scale(1.0) rotate(0deg); opacity: 1; }}
                    80% {{ transform: scale(1.0); opacity: 1; }}
                    100% {{ transform: scale(0); opacity: 0; }}
                }}
                .lightning-bolt {{
                    font-size: 150px;
                    animation: thunder 4.5s forwards;
                    z-index: 2;
                }}
                
                /* Animasi Kepala & Leher Pikachu Keluar */
                @keyframes emerge {{
                    0% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                    40% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                    60% {{ transform: translateY(15px) scale(1.1); opacity: 1; }}
                    85% {{ transform: translateY(25px) scale(1); opacity: 1; }}
                    100% {{ transform: translateY(-200px) scale(0); opacity: 0; }}
                }}
                .pikachu-head-box {{
                    position: absolute;
                    width: 180px;
                    height: 155px; /* Memotong badan agar hanya kepala dan leher yang muncul */
                    overflow: hidden;
                    z-index: 1;
                    animation: emerge 4.5s forwards;
                }}
                
                /* Efek Transisi Keluar Layar */
                @keyframes fadeOut {{
                    0% {{ opacity: 1; }}
                    90% {{ opacity: 1; }}
                    100% {{ opacity: 0; visibility: hidden; }}
                }}
                #intro-screen {{
                    animation: fadeOut 5s forwards;
                }}
            </style>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(4.8)
    st.session_state.intro_done = True

# ==========================================
# 🎨 STYLE HAKAMAN & WALLPAPER CHAT
# ==========================================
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_style}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(255, 248, 180, 0.45);
        z-index: -1;
    }}
    /* Gaya untuk mempercantik pilihan menu */
    .stSelectbox, .stRadio {{
        background: rgba(255, 255, 255, 0.9) !important;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    </style>
""", unsafe_allow_html=True)

# Inisialisasi Memori
if "messages" not in st.session_state:
    st.session_state.messages = []

# Kepribadian AI
kepribadian_pikacu = "Kamu adalah PIKACU AI v4. Balas dengan imut, sebut pengguna 'Habibb', gunakan kata 'pika-pika'."

# ==========================================
# 📱 PANEL MENU UTAMA (DENGAN LOGO LUCU)
# ==========================================
st.markdown("<h1 style='text-align: center; color: #333; text-shadow: 2px 2px 5px white;'>⚡ PIKACU AI v4 SUPER ⚡</h1>", unsafe_allow_html=True)

# Membuat Grid Menu Utama memakai Emojis sebagai Logo Lucu
menu_pilihan = st.radio(
    "✨ SILAHKAN PILIH MODUL DAN FITUR PIKACU DI SINI, HABIBB: ✨",
    [
        "💬 CHAT BOT AI (Ngobrol Seru)",
        "📷 FOTO AI (Deteksi Gambar)",
        "🎥 VIDEO AI (Bikin Animasi)",
        "🎙️ MIC SUARA (Bicara ke Pikacu)",
        "📚 TUGAS SEKOLAH (Ruang Belajar)",
        "🛠️ TOOLS AI LAINNYA (Fitur Canggih)"
    ],
    horizontal=True
)

st.write("---")

# ==========================================
# ⚙️ JALUR LOGIK STRUKTUR FITUR
# ==========================================

# 1. FITUR CHAT BOT
if "💬 CHAT BOT" in menu_pilihan:
    st.subheader("💬 Room Chat Pikacu AI")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_input := st.chat_input("Tanya Pikacu v4 di sini yaa Habibb..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            chat = client.chats.create(model="gemini-2.5-flash", config=types.GenerateContentConfig(system_instruction=kepribadian_pikacu))
            response = chat.send_message(user_input)
            with st.chat_message("assistant"):
                st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Kunci API belum aktif nih Habibb: {e}")

# 2. FITUR FOTO AI
elif "📷 FOTO AI" in menu_pilihan:
    st.subheader("📷 Fitur Deteksi Foto Lucu")
    uploaded_file = st.file_uploader("Upload fotomu di sini Habibb, biar Pikacu terawang! 😜", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Foto Berhasil Diupload!", width=300)
        st.success("📸 Pikaa! Fitur scan foto siap dikembangkan lebih lanjut!")

# 3. FITUR VIDEO AI
elif "🎥 VIDEO AI" in menu_pilihan:
    st.subheader("🎥 Generator Video & Animasi")
    st.info("Pika-pika! Di sini nanti Habib bisa bikin video animasi Pikachu otomatis lewat perintah teks! Fitur ini sedang disiapkan sistem server! 🍿")

# 4. FITUR MIC SUARA
elif "🎙️ MIC SUARA" in menu_pilihan:
    st.subheader("🎙️ Voice Recognition (Deteksi Suara)")
    st.audio_input("Ketuk tombol mic di bawah untuk merekam suaramu ke Pikacu, Habibb:")

# 5. FITUR TUGAS SEKOLAH (SUB-MENU MAPEL)
elif "📚 TUGAS SEKOLAH" in menu_pilihan:
    st.subheader("📚 Ruang Belajar khusus Tugas Habib")
    
    # Sub-fitur di dalam Tugas
    mapel = st.selectbox(
        "Pilih Mata Pelajaran Kamu, Habibb:",
        [
            "📐 MATEMATIKA (Hitung Cepat)",
            "🧪 IPA / SAINS (Eksperimen AI)",
            "🎒 MAPEL LAINNYA (Sejarah, Inggris, dll)"
        ]
    )
    
    st.write(f"### Kamu memilih modul {mapel} ✨")
    soal = st.text_area("Tempel atau ketik soal tugas sekolahmu di sini, biar Pikacu kerjakan:")
    if st.button("🚀 Suruh Pikacu Selesaikan Tugas"):
        if soal:
            with st.spinner("Pikacu lagi ngitung pakai rumus petir... ⚡"):
                try:
                    prompt_tugas = f"Kamu adalah guru pintar. Selesaikan soal sekolah dari Habibb ini dengan penjelasan mudah: {soal}"
                    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_tugas)
                    st.success("📝 Jawaban Selesai!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Gagal memproses tugas: {e}")
        else:
            st.warning("Isi dulu soalnya dong, Habibb! 😁")

# 6. FITUR TOOLS AI LAINNYA
elif "🛠️ TOOLS AI" in menu_pilihan:
    st.subheader("🛠️ Gudang Alat AI Pendukung")
    st.write("* 📝 **AI Pembuat Puisi/Cerita**")
    st.write("* 💻 **AI Pembantu Nyari Kode/Error**")
    st.write("* 🎨 **AI Pembuat Paduan Warna Website**")
    st.success("Semua tools AI berlogo lucu siap diintegrasikan di sini!")
