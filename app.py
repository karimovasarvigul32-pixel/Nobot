import streamlit as st
import os

# Sahifa sozlamalari
st.set_page_config(
    page_title="Для тебя... 💌",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Streamlit o'zining padding/marginini o'chirish
st.markdown("""
<style>
    /* Remove Streamlit default padding */
    .block-container { padding-top: 0; padding-bottom: 0; }
    body { margin: 0; padding: 0; }
    .stApp { background: #fffaf6; }
    
    /* Hide Streamlit header/footer */
    header { display: none; }
    footer { display: none; }
</style>
""", unsafe_allow_html=True)

# HTML faylni o'qish
html_file_path = os.path.join(os.path.dirname(__file__), "sevgi_izhori.html")

# Agar fayl current papkada bo'lmasa, string sifatida belgilang
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    # Agar fayl topilmasa, HTML stringi
    html_content = """
    <div style="text-align:center; padding: 40px;">
        <h2>❌ sevgi_izhori.html faylini topib bo'lmadi</h2>
        <p>app.py bilan bir xil papkada sevgi_izhori.html bo'lishi kerak</p>
    </div>
    """

# HTML-ni Streamlit orqali ko'rsatish
st.components.v1.html(html_content, height=920, scrolling=True)
