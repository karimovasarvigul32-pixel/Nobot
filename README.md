# 💍 Turmushga Chiqish Izhori / Предложение руки и сердца

Interaktiv sevgi izhori web-sahifasi Streamlit orqali.

## 📁 Fayllar

- `app.py` — Streamlit application
- `sevgi_izhori.html` — Interaktiv HTML izhori
- `requirements.txt` — Python dependencies

---

## 🚀 GitHub'ga joylashtirish va Streamlit Cloud'da deploy qilish

### 1️⃣ GitHub Repositorijini yaratish

1. **GitHub.com'ga boring va yangi repository yaratish:**
   - [github.com/new](https://github.com/new) ga boring
   - Repository nomi: `sevgi-izhori` (yoki istagan nom)
   - **Public** qilish (Streamlit Cloud uchun muhim)
   - "Create repository" bosmish

2. **Kompyuterda repository yaratish:**
```bash
# Papkani yaratish
mkdir sevgi-izhori
cd sevgi-izhori

# Git initialize qilish
git init

# Bu 3 faylni papkaga qo'yish:
# - app.py
# - sevgi_izhori.html
# - requirements.txt

# GitHub'ga push qilish
git add .
git commit -m "Initial commit: Interactive proposal app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sevgi-izhori.git
git push -u origin main
```

---

### 2️⃣ Streamlit Cloud'da Deploy qilish

1. **Streamlit Cloud'ga kirish:**
   - [share.streamlit.io](https://share.streamlit.io) ga boring
   - GitHub orqali sign up/login qilish (OAuth)

2. **Yangi app deploy qilish:**
   - "New app" tugmasini bosish
   - GitHub repository va branch tanlash:
     - **Repository:** `YOUR_USERNAME/sevgi-izhori`
     - **Branch:** `main`
     - **Main file path:** `app.py`
   - "Deploy" bosmish

3. **Kutish:**
   - Streamlit avtomatik app'ni build qilib deploy qiladi
   - ~2-3 minutda silingi URL beriladi
   - Masalan: `https://sevgi-izhori.streamlit.app`

---

## 🔄 O'zgartirishlar qilish

GitHub'dagi kodga o'zgartirishlar kiritgach, Streamlit Cloud avtomatik redeploy qiladi.

```bash
# O'zgartirishlar qilgach:
git add .
git commit -m "Update text/design"
git push origin main

# Streamlit Cloud 30-60 sekundda yangi versiyani deploy qiladi
```

---

## 💻 Lokal test qilish

Streamlit Cloud'ga push qilishdan oldin lokal test qilish:

```bash
pip install streamlit
streamlit run app.py
```

Browser'da `http://localhost:8501` ochiladi.

---

## 📋 Fayllar strukturasi

```
sevgi-izhori/
├── app.py                    # Streamlit app
├── sevgi_izhori.html         # Interaktiv izhori
├── requirements.txt          # Dependencies
└── README.md                 # Bu fayl
```

---

## 🌐 Qo'shimcha: Custom domain (ixtiyoriy)

Agar `sevgi-izhori.streamlit.app` o'rniga shaxsiy domen xohlasangiz:
- Streamlit Cloud settings'dan custom domain qo'shish mumkin
- Yoki GitHub Pages + custom domain bilan host qilish mumkin

---

## ❓ Muammolar

**Sahifa yuklanmayapti?**
- Browser console'da xatolar tekshiring (F12)
- `sevgi_izhori.html` faylini `app.py` bilan bir xil papkada ekanini tekshiring

**Tugmalar ishlamayapti?**
- Streamlit component'ning height sozlamasi: `height=920`
- Agar kerak bo'lsa o'zgartiring

**Deploy'dan keyin foydalanish:**
- Shakal/sevgi qilmoqchi bo'lgan kishiga link yuboring
- Telefonda, kompyuterda, iOS/Android Safari'da ishlaydi

---

## 📱 Mobil sahifa

- ✅ iPhone Safari
- ✅ Android Chrome
- ✅ Tablet
- ✅ Desktop

Barcha qurilmalarda to'g'ri ishlaydi!

---

**Qo'llanilgan texnologiya:** Streamlit + HTML5 + CSS3 + JavaScript

**Yaratuvchi:** Made with 💕

Muvaffaqiyali izhori! 🎉💍
