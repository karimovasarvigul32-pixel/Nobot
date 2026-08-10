# ⚡ Tez Boshlash / Быстрый Старт

## 🇺🇿 UZBEK — TEZKOR QO'LLANMA

### 3 Bosqichda GitHub'ga joylashtirish:

**1. GitHub.com'da yangi repo yaratish**
- [github.com/new](https://github.com/new) ga boring
- Repo nomi: `sevgi-izhori`
- **Public** tanlang
- "Create" bosmish

**2. Kompyuterda:**
```bash
# Git o'rnatish (agar o'rnatilmagan bo'lsa)
# Windows: https://git-scm.com/download/win
# Mac: brew install git

# Papkani yaratish
mkdir sevgi-izhori
cd sevgi-izhori

# 4 faylni shu papkaga qo'yish:
# ✅ app.py
# ✅ sevgi_izhori.html
# ✅ requirements.txt
# ✅ .gitignore

# Git konfiguratsiya
git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"

# Push qilish
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sevgi-izhori.git
git push -u origin main
```

**3. Streamlit Cloud'da deploy:**
- [share.streamlit.io](https://share.streamlit.io) ga boring
- GitHub bilan login qiling
- "New app" → repository tanlang
- Main file: `app.py`
- "Deploy" bosmish

✅ **Tayyor!** ~2 minutdan keyin sahifa ishga tushladi.

---

## 🇷🇺 RUSSIAN — БЫСТРАЯ ИНСТРУКЦИЯ

### 3 шага для размещения на GitHub:

**1. Создать новый репозиторий на GitHub.com**
- Перейти на [github.com/new](https://github.com/new)
- Название: `sevgi-izhori`
- Выбрать **Public**
- Нажать "Create"

**2. На компьютере:**
```bash
# Установить Git (если не установлен)
# Windows: https://git-scm.com/download/win
# Mac: brew install git

# Создать папку
mkdir sevgi-izhori
cd sevgi-izhori

# Положить 4 файла в эту папку:
# ✅ app.py
# ✅ sevgi_izhori.html
# ✅ requirements.txt
# ✅ .gitignore

# Настроить Git
git config --global user.name "Ваше имя"
git config --global user.email "email@example.com"

# Загрузить на GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sevgi-izhori.git
git push -u origin main
```

**3. Развернуть на Streamlit Cloud:**
- Перейти на [share.streamlit.io](https://share.streamlit.io)
- Авторизация через GitHub
- "New app" → выбрать репозиторий
- Main file: `app.py`
- Нажать "Deploy"

✅ **Готово!** Через ~2 минуты приложение будет живым.

---

## 📌 ФАЙЛЫ, КОТОРЫЕ НУЖНЫ:

```
sevgi-izhori/
├── app.py                      ← Streamlit приложение
├── sevgi_izhori.html           ← HTML интерактив
├── requirements.txt            ← Зависимости
├── .gitignore                  ← Игнор файлы
├── .streamlit/
│   └── config.toml            ← Оформление
└── README.md                   ← Документация (уже есть)
```

---

## 🔗 ПОСЛЕ РАЗВЕРТЫВАНИЯ:

Получите ссылку: `https://sevgi-izhori.streamlit.app`

**Делитесь с:**
- 📱 Мобильный телефон
- 💻 Компьютер
- 👨‍💻 Любое устройство

**Работает в:**
- ✅ Safari (iPhone)
- ✅ Chrome (Android)
- ✅ Desktop браузеры

---

## 💡 СОВЕТЫ:

| Проблема | Решение |
|----------|---------|
| Ошибка сертификата | Переправить на `https://` |
| Страница не загружается | Проверить файл `app.py` |
| Кнопки не работают | Проверить `sevgi_izhori.html` |
| Изменения не применяются | Подождать 30-60 сек (автоматический редеплой) |

---

## 🎯 ИТОГО:

1. ✅ Создать репо → 1 мин
2. ✅ Загрузить файлы → 2 мин
3. ✅ Deploy на Streamlit → 2 мин

**Всего: ~5 минут** ⏱️

Давайте! 💍🎉
