# 1️⃣ Yol Haritası ve Geliştirme Adımları

## Adım 1 – Repo ve Temel Kurulum (Gün 1)

**Yapılacaklar:**

- GitHub’da repo oluştur (stylemind-ai)
- Local’e çek
- Monorepo yapısı kur
- Klasör yapısı:

```text
stylemind-ai/
├── backend/
├── frontend/
├── README.md
└── .gitignore
```

👉 **Hedef:** Boş repo değil, iskelet hazır

---

## Adım 2 – Backend Başlangıç (Gün 1–2)

**Yapılacaklar:**

- Python virtualenv
- FastAPI ayağa kaldır
- /health endpoint’i yaz

**Hedef:**

- Tarayıcıda http://localhost:8000/docs açılıyor mu?
- Swagger açılıyorsa doğru yoldasın.

---

## Adım 3 – Backend Mimariyi Kur (Çok Önemli) (Gün 2)

**Yapılacaklar:**

- Aşağıdaki klasör yapısını aynen oluştur:

```text
backend/app/
├── main.py
├── core/
├── db/
├── api/
├── services/
└── schemas/
```

- Database bağlantısı
- SQLAlchemy base + session

👉 **Hedef:** Kod yazmadan önce düzenli mimari

---

## Adım 4 – Auth (Register / Login) (Gün 3)

**Yapılacaklar:**

- User modeli
- Password hash (bcrypt)
- JWT üretimi
- Register & Login endpoint

**Endpoint’ler:** - POST /auth/register - POST /auth/login - GET /auth/me

👉 **Hedef:** Kullanıcı kayıt olup login olabiliyor mu? JWT dönüyor mu? ✅

---

## Adım 5 – Wardrobe (Dolap Yönetimi) (Gün 4)

**Yapılacaklar:**

- ClothingItem modeli
- Kıyafet ekleme
- Listeleme
- Silme

**Endpoint’ler:** - POST /wardrobe - GET /wardrobe - DELETE /wardrobe/{id}

👉 **Hedef:** Login olan kullanıcı kendi dolabını görüyor mu?

---

## Adım 6 – Kombin Motoru (Gün 5)

**Yapılacaklar:**

- Rule-based recommendation engine
- Kombin üretme algoritması

**Endpoint:** - POST /outfits/generate

👉 **Hedef:** “Bana kombin öner” dediğinde mantıklı bir şey geliyor mu?

---

## Adım 7 – Hava Durumu Entegrasyonu (Gün 6)

**Yapılacaklar:**

- Weather API
- Backend’ten çağır
- Kombin kurallarına ekle

👉 **Hedef:** Yağmurlu günde açık ayakkabı önerilmiyor mu?

---

## Adım 8 – Frontend (Gün 7–8)

**Yapılacaklar:**

- Login / Register ekranı
- Wardrobe ekranı
- Kombin ekranı
- JWT yönetimi

👉 **Hedef:** Normal kullanıcı gibi uygulamayı kullanabiliyor musun?

---

## Adım 9 – README + Sunum (Gün 9)

**Yapılacaklar:**

- Proje açıklaması
- Tech stack
- Özellikler
- Ekran görüntüleri

👉 **Hedef:** Recruiter repo’ya girince ne yaptığını anlıyor mu?

---

# 2️⃣ Yapılacaklar Dökümantasyonu (Checklist)

## 📌 Project: StyleMind – AI-Powered Personal Style Assistant

### ✅ Phase 0 – Setup

- GitHub repository oluşturuldu
- Monorepo yapısı kuruldu
- Backend & frontend klasörleri oluşturuldu

### 🔐 Phase 1 – Authentication

- User modeli oluşturuldu
- Password hashing eklendi
- JWT authentication implement edildi
- Register endpoint
- Login endpoint
- Protected route middleware

### 👗 Phase 2 – Wardrobe Management

- ClothingItem modeli
- Kıyafet ekleme
- Kıyafet listeleme
- Kıyafet silme
- Kullanıcıya özel veri izolasyonu

### 🧠 Phase 3 – Outfit Recommendation Engine

- Rule-based kombin motoru
- Mekâna göre filtreleme
- Stil uyumluluğu kontrolü
- Kombin endpoint’i

### 🌦️ Phase 4 – Weather Integration

- Weather API entegrasyonu
- Hava durumuna göre kombin
- Edge-case kuralları (yağmur, soğuk)

### 🤖 Phase 5 – AI Enhancements (Optional)

- Fotoğraftan kıyafet türü algılama
- Renk tespiti
- Manuel giriş fallback

### 🎨 Phase 6 – Frontend

- Login / Register UI
- Wardrobe UI
- Outfit UI
- Auth state management

### 📄 Phase 7 – Documentation

• **README.md** hazırlandı
• **Kurulum adımları** eklendi
• **API endpoint dokümantasyonu** tamamlandı
• **Proje ekran görüntüleri** eklendi
