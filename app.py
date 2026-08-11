import streamlit as st
import os

st.set_page_config(
    page_title="Для тебя... 💌",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit UI yashirish + iframe scrollbar to'liq o'chirish
st.markdown("""
<style>
    header[data-testid="stHeader"],
    footer,
    #MainMenu,
    .stDeployButton,
    div[data-testid="stToolbar"],
    div[data-testid="stDecoration"],
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }

    .stApp { background: #fffaf6 !important; }

    .block-container,
    section[data-testid="stMain"],
    section[data-testid="stMain"] > div {
        padding: 0 !important;
        max-width: 100% !important;
        overflow: hidden !important;
    }

    /* IFRAME scrollbar butunlay o'chirish */
    iframe {
        border: none !important;
        overflow: hidden !important;
        scrollbar-width: none !important;
    }
    iframe::-webkit-scrollbar {
        display: none !important;
    }

    /* Streamlit html component wrapper */
    div[data-testid="stHtml"],
    div[data-testid="stHtml"] > div,
    div[data-testid="stHtml"] > div > div,
    .element-container,
    .stComponentContainer {
        overflow: hidden !important;
        scrollbar-width: none !important;
    }
    div[data-testid="stHtml"] *::-webkit-scrollbar,
    .element-container *::-webkit-scrollbar {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sevgi_izhori.html")

try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    html_content = '<div style="text-align:center;padding:40px;"><h2>sevgi_izhori.html topilmadi</h2></div>'

# Iframe ICHIDA scrollbar o'chirish — bu eng muhimi
# Chunki Streamlit tashqi CSS iframe ichiga kirmaydi
scrollbar_kill = """
<style>
html, body, .card, * {
    overflow: hidden !important;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
}
html::-webkit-scrollbar,
body::-webkit-scrollbar,
.card::-webkit-scrollbar,
*::-webkit-scrollbar {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    background: transparent !important;
}
</style>
"""

if "</head>" in html_content:
    html_content = html_content.replace("</head>", scrollbar_kill + "</head>")

# height kattaroq = content sig'adi = scrollbar chiqmaydi
st.components.v1.html(html_content, height=900, scrolling=False)
