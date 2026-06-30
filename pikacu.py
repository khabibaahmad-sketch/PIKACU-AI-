import os
import base64
import streamlit as st
from google import genai
from google.genai import types

# Setting Dasar Halaman Utama
st.set_page_config(page_title="PIKACU AI v4 SUPER", page_icon="⚡", layout="wide")

# ==========================================
# 🔑 KONFIGURASI API KEY & ASET
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
# ⚡ INTRO ANIMASI PETIR & SUARA (ANTI-BLANK) ⚡
# ==========================================
# Di sini kita hilangkan time.sleep agar server tidak membeku!
if "intro_played" not in st.session_state:
    st.session_state.intro_played = True
    sound_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptrackid=553823"
    
    st.markdown(f"""
        <div id="intro-screen">
            <!-- Audio Suara Pikachu Original Anime -->
            <audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>
            
            <div class="animation-container">
                <!-- Efek Petir Menggelegar di Tengah -->
                <div class="lightning-bolt">⚡</div>
                
                <!-- Kepala & Leher Pikachu Keluar dari Petir -->
                <div class="pikachu-head-box">
                    <img src="{bg_style}" style="width: 180px; height: auto;">
                </div>
            </div>
            <h2 class="loading-text">⚡ PIKACU AI v4 READY... ⚡</h2>
        </div>

        <style>
            #intro-screen {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: #111111; z-index: 99999; display: flex; flex-direction: column;
                justify-content: center; align-items: center; overflow: hidden;
                animation: fadeOut 5s forwards;
                pointer-events: none;
            }}
            .animation-container {{
                position: relative; width: 300px; height: 300px; 
                display: flex; justify-content: center; align-items: center;
            }}
            @keyframes thunder {{
                0% {{ transform: scale(0.3); opacity: 0; }}
                20% {{ transform: scale(1.3); opacity: 1; filter: drop-shadow(0 0 20px #FFF); }}
                40% {{ transform: scale(1.0); opacity: 1; }}
                85% {{ transform: scale(1.0); opacity: 1; }}
                100% {{ transform: scale(0); opacity: 0; }}
            }}
            .lightning-bolt {{
                font-size: 140px; color: #FFE000;
                animation: thunder 4.5s forwards;
                z-index: 2;
            }}
            @keyframes emerge {{
                0% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                35% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                55% {{ transform: translateY(10px) scale(1.1); opacity: 1; }}
                80% {{ transform: translateY(20px) scale(1); opacity: 1; }}
                100% {{ transform: translateY(-200px) scale(0); opacity: 0; }}
            }}
            .pikachu-head-box {{
                position: absolute; width: 180px; height: 145px; 
                overflow: hidden; z-index: 1;
                animation: emerge 4.5s forwards;
            }}
            @keyframes textAnim {{
                0% {{ opacity: 0; }} 20% {{ opacity: 1; }} 80% {{ opacity: 1; }} 100% {{ opacity: 0; }}
            }}
            .loading-text {{
                color: #FFE000; font-family: sans-serif; font-size: 26px; 
                margin-top: 20px; font-weight: bold; text-shadow: 0 0 10px #FFE000;
                animation: textAnim 4.5s forwards;
            }}
            @keyframes fadeOut {{
                0% {{ opacity: 1; visibility: visible; }}
                85% {{ opacity: 1; visibility: visible; }}
                100% {{ opacity: 0; visibility: hidden; }}
            }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 🎨 DESIGN INTERFACE & WALLPAPER UTAMA
# ==========================================
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_style}");
        background-size: cover; background-position: center;
        background-repeat: no-repeat; background-attachment: fixed;
    }}
    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(255, 248, 180, 0.45); z-index: -1;
    }}
    .custom-box {{
        background: rgba(255, 255, 255, 0.92) !important;
        padding: 20px; border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        border: 2px solid #ffde00; margin-bottom: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header Judul Keren
st.markdown("<h1 style='text-align: center; color: #222; text-shadow: 2px 2px 4px white;'>⚡ PIKACU AI v4 SUPER DASHBOARD ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; font-size: 16px; color: #444;'>👑 Edisi Spesial Habibb: Penuh Fitur Logu Lucu & Interaktif!</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 📱 MENU UTAMA DENGAN LOGO-LOGO LUCU
# ==========================================
st.markdown("### 🌟 Pilih Fitur Super Pikacu:")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    btn_chat = st.button("💬\n\nCHAT BOT AI", use_container_width=True)
with col2:
    btn_foto = st.button("📸\n\nFOTO AI", use_container_width=True)
with col3:
    btn_video = st.button("🎬\n\nVIDEO AI", use_container_width=True)
with col4:
    btn_mic = st.button("🎙️\n\nMIC SUARA", use_container_width=True)
with col5:
    btn_tugas = st.button("📚\n\nTUGAS SEKOLAH", use_container_width=True)
with col6:
    btn_tools = st.button("🛠️\n\nTOOLS AI LAIN", use_container_width=True)

# Menyimpan Menu yang Sedang Aktif
if "menu_aktif" not in st.session_state:
    st.session_state.menu_aktif = "💬 CHAT BOT AI"

if btn_chat: st.session_state.menu_aktif = "💬 CHAT BOT AI"
elif btn_foto: st.session_state.menu_aktif = "📸 FOTO AI"
elif btn_video: st.session_state.menu_aktif = "🎬 VIDEO AI"
elif btn_mic: st.session_state.menu_aktif = "🎙️ MIC SUARA"
elif btn_tugas: st.session_state.menu_aktif = "📚 TUGAS SEKOLAH"
elif btn_tools: st.session_state.menu_aktif = "🛠️ TOOLS AI LAIN"

st.write(f"#### Fitur Aktif: {st.session_state.menu_aktif}")

# ==========================================
# ⚙️ LOGIK JALUR OPERASIONAL FITUR
# ==========================================

# 1. 💬 MENU CHAT AI
if st.session_state.menu_aktif == "💬 CHAT BOT AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 💬 Room Chat Utama Pikacu")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_input := st.chat_input("Ketik pesanmu di sini ya Habibb..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            prompt_config = "Kamu PIKACU AI v4. Bicara sangat imut, panggil pengguna 'Habibb', gunakan gaya pika-pika ceria."
            chat = client.chats.create(model="gemini-2.5-flash", config=types.GenerateContentConfig(system_instruction=prompt_config))
            response = chat.send_message(user_input)
            with st.chat_message("assistant"):
                st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Aduh ada kendala koneksi nih Habibb: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 📸 MENU FOTO AI
elif st.session_state.menu_aktif == "📸 FOTO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📸 Scanner Foto Pintar")
    uploaded_file = st.file_uploader("Upload gambarmu ke sini, Habibb:", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Foto Berhasil Dimasukkan!", width=250)
        st.success("📸 Pikaa! Berhasil membaca gambar! Fitur analisis objek foto siap dijalankan!")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. 🎬 MENU VIDEO AI
elif st.session_state.menu_aktif == "🎬 VIDEO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎬 Video & Animasi Generator")
    st.text_input("Ketik skenario animasi video pendek yang mau kamu buat, Habibb:")
    st.info("Fitur render animasi video otomatis sedang dipersiapkan oleh server utama! 🍿")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 🎙️ MENU MIC SUARA
elif st.session_state.menu_aktif == "🎙️ MIC SUARA":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎙️ Perekam Suara Langsung")
    st.audio_input("Ketuk tombol mic di bawah ini lalu bicaralah, Pikacu siap mendengarkan:")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. 📚 MENU TUGAS SEKOLAH (SUB-MENU MAPEL)
elif st.session_state.menu_aktif == "📚 TUGAS SEKOLAH":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📚 Ruang Penyelesaian Tugas Sekolah Habibb")
    
    # Sub-Menu Mapel dengan Logo Lucu Masing-masing
    sub_mapel = st.selectbox(
        "✨ Pilih Mata Pelajaran yang Mau Dibantu Pikacu: ✨",
        [
            "📐 MATEMATIKA (Hitung Angka Kilat)",
            "🧪 IPA / SAINS (Eksperimen Lab AI)",
            "🎒 MAPEL LAINNYA (Sejarah, Bahasa, dll)"
        ]
    )
    
    st.write(f"**Kategori Aktif:** {sub_mapel}")
    soal_teks = st.text_area("Tulis atau tempel teks soal tugasmu di sini ya:")
    
    if st.button("🚀 Pecahkan Soal dengan Rumus Petir"):
        if soal_teks:
            with st.spinner("Pikacu lagi corat-coret rumus... ⚡"):
                try:
                    full_prompt = f"Selesaikan soal tugas sekolah kategori {sub_mapel} milik Habibb ini dengan cara bertahap yang cerdas dan jelas: {soal_teks}"
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=full_prompt)
                    st.success("📝 Solusi Tugas Selesai Dikerjakan!")
                    st.write(res.text)
                except Exception as e:
                    st.error(f"Gagal memproses: {e}")
        else:
            st.warning("Masukkan dulu teks pertanyaannya ya, Habibb! 😊")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. 🛠️ MENU TOOLS AI LAINNYA
elif st.session_state.menu_aktif == "🛠️ TOOLS AI LAIN":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🛠️ Gudang Tools AI Pembantu")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("#### 📝 Pembuat Puisi/Cerita")
        st.caption("Bikin karya sastra instan buatan AI.")
    with t2:
        st.markdown("#### 💻 Pemeriksa Kode Error")
        st.caption("Cari baris kodinganmu yang mogok.")
    with t3:
        st.markdown("#### 🎨 Palet Warna Web")
        st.caption("Rekomendasi paduan warna estetik.")
    st.markdown('</div>', unsafe_allow_html=True)
    import os
import base64
import streamlit as st
from google import genai
from google.genai import types

# Setting Dasar Halaman Utama
st.set_page_config(page_title="PIKACU AI v4 SUPER", page_icon="⚡", layout="wide")

# ==========================================
# 🔑 KONFIGURASI API KEY & ASET
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
# ⚡ INTRO ANIMASI PETIR & SUARA (ANTI-BLANK) ⚡
# ==========================================
# Di sini kita hilangkan time.sleep agar server tidak membeku!
if "intro_played" not in st.session_state:
    st.session_state.intro_played = True
    sound_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptrackid=553823"
    
    st.markdown(f"""
        <div id="intro-screen">
            <!-- Audio Suara Pikachu Original Anime -->
            <audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>
            
            <div class="animation-container">
                <!-- Efek Petir Menggelegar di Tengah -->
                <div class="lightning-bolt">⚡</div>
                
                <!-- Kepala & Leher Pikachu Keluar dari Petir -->
                <div class="pikachu-head-box">
                    <img src="{bg_style}" style="width: 180px; height: auto;">
                </div>
            </div>
            <h2 class="loading-text">⚡ PIKACU AI v4 READY... ⚡</h2>
        </div>

        <style>
            #intro-screen {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: #111111; z-index: 99999; display: flex; flex-direction: column;
                justify-content: center; align-items: center; overflow: hidden;
                animation: fadeOut 5s forwards;
                pointer-events: none;
            }}
            .animation-container {{
                position: relative; width: 300px; height: 300px; 
                display: flex; justify-content: center; align-items: center;
            }}
            @keyframes thunder {{
                0% {{ transform: scale(0.3); opacity: 0; }}
                20% {{ transform: scale(1.3); opacity: 1; filter: drop-shadow(0 0 20px #FFF); }}
                40% {{ transform: scale(1.0); opacity: 1; }}
                85% {{ transform: scale(1.0); opacity: 1; }}
                100% {{ transform: scale(0); opacity: 0; }}
            }}
            .lightning-bolt {{
                font-size: 140px; color: #FFE000;
                animation: thunder 4.5s forwards;
                z-index: 2;
            }}
            @keyframes emerge {{
                0% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                35% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                55% {{ transform: translateY(10px) scale(1.1); opacity: 1; }}
                80% {{ transform: translateY(20px) scale(1); opacity: 1; }}
                100% {{ transform: translateY(-200px) scale(0); opacity: 0; }}
            }}
            .pikachu-head-box {{
                position: absolute; width: 180px; height: 145px; 
                overflow: hidden; z-index: 1;
                animation: emerge 4.5s forwards;
            }}
            @keyframes textAnim {{
                0% {{ opacity: 0; }} 20% {{ opacity: 1; }} 80% {{ opacity: 1; }} 100% {{ opacity: 0; }}
            }}
            .loading-text {{
                color: #FFE000; font-family: sans-serif; font-size: 26px; 
                margin-top: 20px; font-weight: bold; text-shadow: 0 0 10px #FFE000;
                animation: textAnim 4.5s forwards;
            }}
            @keyframes fadeOut {{
                0% {{ opacity: 1; visibility: visible; }}
                85% {{ opacity: 1; visibility: visible; }}
                100% {{ opacity: 0; visibility: hidden; }}
            }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 🎨 DESIGN INTERFACE & WALLPAPER UTAMA
# ==========================================
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_style}");
        background-size: cover; background-position: center;
        background-repeat: no-repeat; background-attachment: fixed;
    }}
    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(255, 248, 180, 0.45); z-index: -1;
    }}
    .custom-box {{
        background: rgba(255, 255, 255, 0.92) !important;
        padding: 20px; border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        border: 2px solid #ffde00; margin-bottom: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header Judul Keren
st.markdown("<h1 style='text-align: center; color: #222; text-shadow: 2px 2px 4px white;'>⚡ PIKACU AI v4 SUPER DASHBOARD ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; font-size: 16px; color: #444;'>👑 Edisi Spesial Habibb: Penuh Fitur Logu Lucu & Interaktif!</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 📱 MENU UTAMA DENGAN LOGO-LOGO LUCU
# ==========================================
st.markdown("### 🌟 Pilih Fitur Super Pikacu:")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    btn_chat = st.button("💬\n\nCHAT BOT AI", use_container_width=True)
with col2:
    btn_foto = st.button("📸\n\nFOTO AI", use_container_width=True)
with col3:
    btn_video = st.button("🎬\n\nVIDEO AI", use_container_width=True)
with col4:
    btn_mic = st.button("🎙️\n\nMIC SUARA", use_container_width=True)
with col5:
    btn_tugas = st.button("📚\n\nTUGAS SEKOLAH", use_container_width=True)
with col6:
    btn_tools = st.button("🛠️\n\nTOOLS AI LAIN", use_container_width=True)

# Menyimpan Menu yang Sedang Aktif
if "menu_aktif" not in st.session_state:
    st.session_state.menu_aktif = "💬 CHAT BOT AI"

if btn_chat: st.session_state.menu_aktif = "💬 CHAT BOT AI"
elif btn_foto: st.session_state.menu_aktif = "📸 FOTO AI"
elif btn_video: st.session_state.menu_aktif = "🎬 VIDEO AI"
elif btn_mic: st.session_state.menu_aktif = "🎙️ MIC SUARA"
elif btn_tugas: st.session_state.menu_aktif = "📚 TUGAS SEKOLAH"
elif btn_tools: st.session_state.menu_aktif = "🛠️ TOOLS AI LAIN"

st.write(f"#### Fitur Aktif: {st.session_state.menu_aktif}")

# ==========================================
# ⚙️ LOGIK JALUR OPERASIONAL FITUR
# ==========================================

# 1. 💬 MENU CHAT AI
if st.session_state.menu_aktif == "💬 CHAT BOT AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 💬 Room Chat Utama Pikacu")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_input := st.chat_input("Ketik pesanmu di sini ya Habibb..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            prompt_config = "Kamu PIKACU AI v4. Bicara sangat imut, panggil pengguna 'Habibb', gunakan gaya pika-pika ceria."
            chat = client.chats.create(model="gemini-2.5-flash", config=types.GenerateContentConfig(system_instruction=prompt_config))
            response = chat.send_message(user_input)
            with st.chat_message("assistant"):
                st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Aduh ada kendala koneksi nih Habibb: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 📸 MENU FOTO AI
elif st.session_state.menu_aktif == "📸 FOTO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📸 Scanner Foto Pintar")
    uploaded_file = st.file_uploader("Upload gambarmu ke sini, Habibb:", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Foto Berhasil Dimasukkan!", width=250)
        st.success("📸 Pikaa! Berhasil membaca gambar! Fitur analisis objek foto siap dijalankan!")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. 🎬 MENU VIDEO AI
elif st.session_state.menu_aktif == "🎬 VIDEO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎬 Video & Animasi Generator")
    st.text_input("Ketik skenario animasi video pendek yang mau kamu buat, Habibb:")
    st.info("Fitur render animasi video otomatis sedang dipersiapkan oleh server utama! 🍿")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 🎙️ MENU MIC SUARA
elif st.session_state.menu_aktif == "🎙️ MIC SUARA":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎙️ Perekam Suara Langsung")
    st.audio_input("Ketuk tombol mic di bawah ini lalu bicaralah, Pikacu siap mendengarkan:")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. 📚 MENU TUGAS SEKOLAH (SUB-MENU MAPEL)
elif st.session_state.menu_aktif == "📚 TUGAS SEKOLAH":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📚 Ruang Penyelesaian Tugas Sekolah Habibb")
    
    # Sub-Menu Mapel dengan Logo Lucu Masing-masing
    sub_mapel = st.selectbox(
        "✨ Pilih Mata Pelajaran yang Mau Dibantu Pikacu: ✨",
        [
            "📐 MATEMATIKA (Hitung Angka Kilat)",
            "🧪 IPA / SAINS (Eksperimen Lab AI)",
            "🎒 MAPEL LAINNYA (Sejarah, Bahasa, dll)"
        ]
    )
    
    st.write(f"**Kategori Aktif:** {sub_mapel}")
    soal_teks = st.text_area("Tulis atau tempel teks soal tugasmu di sini ya:")
    
    if st.button("🚀 Pecahkan Soal dengan Rumus Petir"):
        if soal_teks:
            with st.spinner("Pikacu lagi corat-coret rumus... ⚡"):
                try:
                    full_prompt = f"Selesaikan soal tugas sekolah kategori {sub_mapel} milik Habibb ini dengan cara bertahap yang cerdas dan jelas: {soal_teks}"
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=full_prompt)
                    st.success("📝 Solusi Tugas Selesai Dikerjakan!")
                    st.write(res.text)
                except Exception as e:
                    st.error(f"Gagal memproses: {e}")
        else:
            st.warning("Masukkan dulu teks pertanyaannya ya, Habibb! 😊")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. 🛠️ MENU TOOLS AI LAINNYA
elif st.session_state.menu_aktif == "🛠️ TOOLS AI LAIN":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🛠️ Gudang Tools AI Pembantu")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("#### 📝 Pembuat Puisi/Cerita")
        st.caption("Bikin karya sastra instan buatan AI.")
    with t2:
        st.markdown("#### 💻 Pemeriksa Kode Error")
        st.caption("Cari baris kodinganmu yang mogok.")
    with t3:
        st.markdown("#### 🎨 Palet Warna Web")
        st.caption("Rekomendasi paduan warna estetik.")
    st.markdown('</div>', unsafe_allow_html=True)import os
import base64
import streamlit as st
from google import genai
from google.genai import types

# Setting Dasar Halaman Utama
st.set_page_config(page_title="PIKACU AI v4 SUPER", page_icon="⚡", layout="wide")

# ==========================================
# 🔑 KONFIGURASI API KEY & ASET
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
# ⚡ INTRO ANIMASI PETIR & SUARA (ANTI-BLANK) ⚡
# ==========================================
# Di sini kita hilangkan time.sleep agar server tidak membeku!
if "intro_played" not in st.session_state:
    st.session_state.intro_played = True
    sound_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptrackid=553823"
    
    st.markdown(f"""
        <div id="intro-screen">
            <!-- Audio Suara Pikachu Original Anime -->
            <audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>
            
            <div class="animation-container">
                <!-- Efek Petir Menggelegar di Tengah -->
                <div class="lightning-bolt">⚡</div>
                
                <!-- Kepala & Leher Pikachu Keluar dari Petir -->
                <div class="pikachu-head-box">
                    <img src="{bg_style}" style="width: 180px; height: auto;">
                </div>
            </div>
            <h2 class="loading-text">⚡ PIKACU AI v4 READY... ⚡</h2>
        </div>

        <style>
            #intro-screen {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: #111111; z-index: 99999; display: flex; flex-direction: column;
                justify-content: center; align-items: center; overflow: hidden;
                animation: fadeOut 5s forwards;
                pointer-events: none;
            }}
            .animation-container {{
                position: relative; width: 300px; height: 300px; 
                display: flex; justify-content: center; align-items: center;
            }}
            @keyframes thunder {{
                0% {{ transform: scale(0.3); opacity: 0; }}
                20% {{ transform: scale(1.3); opacity: 1; filter: drop-shadow(0 0 20px #FFF); }}
                40% {{ transform: scale(1.0); opacity: 1; }}
                85% {{ transform: scale(1.0); opacity: 1; }}
                100% {{ transform: scale(0); opacity: 0; }}
            }}
            .lightning-bolt {{
                font-size: 140px; color: #FFE000;
                animation: thunder 4.5s forwards;
                z-index: 2;
            }}
            @keyframes emerge {{
                0% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                35% {{ transform: translateY(150px) scale(0); opacity: 0; }}
                55% {{ transform: translateY(10px) scale(1.1); opacity: 1; }}
                80% {{ transform: translateY(20px) scale(1); opacity: 1; }}
                100% {{ transform: translateY(-200px) scale(0); opacity: 0; }}
            }}
            .pikachu-head-box {{
                position: absolute; width: 180px; height: 145px; 
                overflow: hidden; z-index: 1;
                animation: emerge 4.5s forwards;
            }}
            @keyframes textAnim {{
                0% {{ opacity: 0; }} 20% {{ opacity: 1; }} 80% {{ opacity: 1; }} 100% {{ opacity: 0; }}
            }}
            .loading-text {{
                color: #FFE000; font-family: sans-serif; font-size: 26px; 
                margin-top: 20px; font-weight: bold; text-shadow: 0 0 10px #FFE000;
                animation: textAnim 4.5s forwards;
            }}
            @keyframes fadeOut {{
                0% {{ opacity: 1; visibility: visible; }}
                85% {{ opacity: 1; visibility: visible; }}
                100% {{ opacity: 0; visibility: hidden; }}
            }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 🎨 DESIGN INTERFACE & WALLPAPER UTAMA
# ==========================================
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_style}");
        background-size: cover; background-position: center;
        background-repeat: no-repeat; background-attachment: fixed;
    }}
    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(255, 248, 180, 0.45); z-index: -1;
    }}
    .custom-box {{
        background: rgba(255, 255, 255, 0.92) !important;
        padding: 20px; border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        border: 2px solid #ffde00; margin-bottom: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header Judul Keren
st.markdown("<h1 style='text-align: center; color: #222; text-shadow: 2px 2px 4px white;'>⚡ PIKACU AI v4 SUPER DASHBOARD ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; font-size: 16px; color: #444;'>👑 Edisi Spesial Habibb: Penuh Fitur Logu Lucu & Interaktif!</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 📱 MENU UTAMA DENGAN LOGO-LOGO LUCU
# ==========================================
st.markdown("### 🌟 Pilih Fitur Super Pikacu:")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    btn_chat = st.button("💬\n\nCHAT BOT AI", use_container_width=True)
with col2:
    btn_foto = st.button("📸\n\nFOTO AI", use_container_width=True)
with col3:
    btn_video = st.button("🎬\n\nVIDEO AI", use_container_width=True)
with col4:
    btn_mic = st.button("🎙️\n\nMIC SUARA", use_container_width=True)
with col5:
    btn_tugas = st.button("📚\n\nTUGAS SEKOLAH", use_container_width=True)
with col6:
    btn_tools = st.button("🛠️\n\nTOOLS AI LAIN", use_container_width=True)

# Menyimpan Menu yang Sedang Aktif
if "menu_aktif" not in st.session_state:
    st.session_state.menu_aktif = "💬 CHAT BOT AI"

if btn_chat: st.session_state.menu_aktif = "💬 CHAT BOT AI"
elif btn_foto: st.session_state.menu_aktif = "📸 FOTO AI"
elif btn_video: st.session_state.menu_aktif = "🎬 VIDEO AI"
elif btn_mic: st.session_state.menu_aktif = "🎙️ MIC SUARA"
elif btn_tugas: st.session_state.menu_aktif = "📚 TUGAS SEKOLAH"
elif btn_tools: st.session_state.menu_aktif = "🛠️ TOOLS AI LAIN"

st.write(f"#### Fitur Aktif: {st.session_state.menu_aktif}")

# ==========================================
# ⚙️ LOGIK JALUR OPERASIONAL FITUR
# ==========================================

# 1. 💬 MENU CHAT AI
if st.session_state.menu_aktif == "💬 CHAT BOT AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 💬 Room Chat Utama Pikacu")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_input := st.chat_input("Ketik pesanmu di sini ya Habibb..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            prompt_config = "Kamu PIKACU AI v4. Bicara sangat imut, panggil pengguna 'Habibb', gunakan gaya pika-pika ceria."
            chat = client.chats.create(model="gemini-2.5-flash", config=types.GenerateContentConfig(system_instruction=prompt_config))
            response = chat.send_message(user_input)
            with st.chat_message("assistant"):
                st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Aduh ada kendala koneksi nih Habibb: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 📸 MENU FOTO AI
elif st.session_state.menu_aktif == "📸 FOTO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📸 Scanner Foto Pintar")
    uploaded_file = st.file_uploader("Upload gambarmu ke sini, Habibb:", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Foto Berhasil Dimasukkan!", width=250)
        st.success("📸 Pikaa! Berhasil membaca gambar! Fitur analisis objek foto siap dijalankan!")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. 🎬 MENU VIDEO AI
elif st.session_state.menu_aktif == "🎬 VIDEO AI":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎬 Video & Animasi Generator")
    st.text_input("Ketik skenario animasi video pendek yang mau kamu buat, Habibb:")
    st.info("Fitur render animasi video otomatis sedang dipersiapkan oleh server utama! 🍿")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 🎙️ MENU MIC SUARA
elif st.session_state.menu_aktif == "🎙️ MIC SUARA":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🎙️ Perekam Suara Langsung")
    st.audio_input("Ketuk tombol mic di bawah ini lalu bicaralah, Pikacu siap mendengarkan:")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. 📚 MENU TUGAS SEKOLAH (SUB-MENU MAPEL)
elif st.session_state.menu_aktif == "📚 TUGAS SEKOLAH":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 📚 Ruang Penyelesaian Tugas Sekolah Habibb")
    
    # Sub-Menu Mapel dengan Logo Lucu Masing-masing
    sub_mapel = st.selectbox(
        "✨ Pilih Mata Pelajaran yang Mau Dibantu Pikacu: ✨",
        [
            "📐 MATEMATIKA (Hitung Angka Kilat)",
            "🧪 IPA / SAINS (Eksperimen Lab AI)",
            "🎒 MAPEL LAINNYA (Sejarah, Bahasa, dll)"
        ]
    )
    
    st.write(f"**Kategori Aktif:** {sub_mapel}")
    soal_teks = st.text_area("Tulis atau tempel teks soal tugasmu di sini ya:")
    
    if st.button("🚀 Pecahkan Soal dengan Rumus Petir"):
        if soal_teks:
            with st.spinner("Pikacu lagi corat-coret rumus... ⚡"):
                try:
                    full_prompt = f"Selesaikan soal tugas sekolah kategori {sub_mapel} milik Habibb ini dengan cara bertahap yang cerdas dan jelas: {soal_teks}"
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=full_prompt)
                    st.success("📝 Solusi Tugas Selesai Dikerjakan!")
                    st.write(res.text)
                except Exception as e:
                    st.error(f"Gagal memproses: {e}")
        else:
            st.warning("Masukkan dulu teks pertanyaannya ya, Habibb! 😊")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. 🛠️ MENU TOOLS AI LAINNYA
elif st.session_state.menu_aktif == "🛠️ TOOLS AI LAIN":
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.write("### 🛠️ Gudang Tools AI Pembantu")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("#### 📝 Pembuat Puisi/Cerita")
        st.caption("Bikin karya sastra instan buatan AI.")
    with t2:
        st.markdown("#### 💻 Pemeriksa Kode Error")
        st.caption("Cari baris kodinganmu yang mogok.")
    with t3:
        st.markdown("#### 🎨 Palet Warna Web")
        st.caption("Rekomendasi paduan warna estetik.")
    st.markdown('</div>', unsafe_allow_html=True)

