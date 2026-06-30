import os
import time
import base64
import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# KONFIGURASI UTAMA
# ==========================================

# Pasang tanda petik rapi untuk kunci kamu
os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6Jgj6a8rQkyiTtjsGYo5Yg9T5tddDSX0-8JuJvVFu9D9g"
client = genai.Client()

# Setting Halaman Web
st.set_page_config(page_title="PIKACU AI v4", page_icon="⚡", layout="wide")

# File Gambar Pikacu Baru v4 (Pegang angka 4)
MASKOT_FILENAME = "pikacu.png" 

# Fungsi pembantu untuk mengubah gambar lokal menjadi kode Base64 agar bisa jadi Background Web
def get_base64_img(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_img(MASKOT_FILENAME)
bg_style = f"data:image/png;base64,{img_base64}" if img_base64 else ""

# ==========================================
# ⚡ st.session_state.loading_done = True

# ==========================================
# 🎨 BAGIAN 2: WALLPAPER GAMBAR PIKACU DI DALAM CHAT 🎨
# ==========================================
st.markdown(f"""
    <style>
    /* MENGUBAH BACKGROUND CHAT MENJADI GAMBAR PIKACU EMAS */
    .stApp {{
        background-image: url("{bg_style}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Overlay semi-transparan kuning petir agar teks obrolan tetap terbaca empuk */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(255, 235, 59, 0.45);
        z-index: -1;
    }}
    
    /* Box Chat User */
    .st-emotion-cache-janw4x {{
        background-color: rgba(255, 249, 196, 0.85) !important; 
        border-radius: 15px;
        border: 1px solid #ffeb3b;
    }}
    
    /* Box Chat Assistant / Pikacu */
    .st-emotion-cache-10o1dsi {{
        background-color: rgba(230, 238, 156, 0.85) !important;
        border-radius: 15px;
        border: 1px solid #cddc39;
    }}

    /* Maskot Pendukung Mengambang di Kanan Bawah */
    .pikachu-corner {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 998;
        text-align: center;
        background: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        border: 3px solid #ffde00;
    }}
    .pikachu-avatar {{
        width: 100px;
        height: auto;
    }}
    .status-bubble {{
        font-size: 13px;
        font-weight: bold;
        background-color: #fff;
        border: 2px solid #ff9100;
        border-radius: 10px;
        padding: 4px 8px;
        margin-top: -8px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🤖 BAGIAN 3: PROMPT KEPRIBADIAN PIKACU
# ==========================================
kepribadian_pikacu = (
    "Kamu adalah PIKACU AI v4, sebuah kecerdasan buatan super pintar namun punya kepribadian yang sangat lucu, menggemaskan, dan jahil. "
    "Kamu berbicara menggunakan bahasa Indonesia yang TIDAK BAKU, santai, imut, dan sesekali menggunakan kata-kata seperti 'pika-pika', 'yaa', 'nihh', 'tahuu'. "
    "Meskipun bicaranya lucu, kamu TETAP SANGAT PINTAR (setara Gemini) dan bisa menjawab pertanyaan rumit tentang coding, sains, sejarah, dll. "
    "Panggil pengguna selalu dengan nama 'Habibb'. Jangan pernah formal."
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "status_pikacu" not in st.session_state:
    st.session_state.status_pikacu = "👋 Pika-Pika! Hallo Habibb! v4 Siap!"

# ==========================================
# 🖥️ BAGIAN 4: TAMPILAN UTAMA & INTERAKSI
# ==========================================
st.markdown("<h1 style='text-align: center; color: #333; text-shadow: 2px 2px 4px rgba(255,255,255,0.8);'>⚡ PIKACU AI v4 ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; font-size: 18px; color: #222; text-shadow: 1px 1px 2px white;'>🤖 Edisi Spesial Habibb: Pegang Angka 4 Emas!</p>", unsafe_allow_html=True)
st.write("---")

# Menampilkan Obrolan
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Tempat Maskot Mengambang di Kanan Bawah
maskot_placeholder = st.empty()

def update_maskot(status_text):
    if bg_style:
        maskot_placeholder.markdown(f"""
            <div class="pikachu-corner">
                <img class="pikachu-avatar" src="{bg_style}">
                <div class="status-bubble">{status_text}</div>
            </div>
        """, unsafe_allow_html=True)

if st.session_state.loading_done:
    update_maskot(st.session_state.status_pikacu)

# ==========================================
# 💬 BAGIAN 5: PROSES CHAT
# ==========================================
if user_input := st.chat_input("Tanya Pikacu v4 di sini yaa Habibb..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    update_maskot("🤔 Pika.. pika? (Lagi mikir keras nih...)")
    time.sleep(2.0)
    
    try:
        history = []
        for m in st.session_state.messages[:-1]:
            role = "user" if m["role"] == "user" else "model"
            history.append(types.Content(role=role, parts=[types.Part.from_text(text=m["content"])]))
        
        chat = client.chats.create(
            model="gemini-2.5-flash",
            history=history,
            config=types.GenerateContentConfig(system_instruction=kepribadian_pikacu, temperature=0.8)
        )
        response = chat.send_message(user_input)
        jawaban = response.text
        
        update_maskot("💡 Aha! v4 Dapat Ide! Kring!")
        time.sleep(0.8)
        
        with st.chat_message("assistant"):
            st.write(jawaban)
        st.session_state.messages.append({"role": "assistant", "content": jawaban})
        
        st.session_state.status_pikacu = "⚡ Pikaaa! v4 Mantap!"
        update_maskot(st.session_state.status_pikacu)
        
    except Exception as e:
        st.error(f"Aduh error Habibb, kuncinya udah bener belum? : {e}")
        update_maskot("❌ Pika-Error!")
