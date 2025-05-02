# 🔎 Content Automation Summary App

Bu proje, **Hacker News** üzerindeki popüler haberleri toplayıp, yapay zeka ile özetleyip çok dilli olarak sunan ve linkednde paylaşmayı amaçlayan bir sistemdir. Mobil (Flutter) ve Python tabanlı backend'den oluşur.

## 🧩 AKIŞ

### 1. Python Backend (Algolia + Gemini API)
- ✅ Hacker News üzerinden Algolia API ile 10 popüler hikaye çekilir.
- ✅ Her hikaye `summaryStatus: "pending"` olarak **Firestore**'a kaydedilir.
- ✅ `summaryStatus: "queued"` olan hikayeler Google Gemini API ile özetlenir.
- ✅ Özetler Türkçeye çevrilir ve `summaryStatus: "done"` olarak güncellenir.

### 2. Flutter Mobil Uygulama
- ✅ Firestore'dan haber listesi çekilir.
- ✅ Kullanıcı bir haberi seçtiğinde, ilgili belgenin `summaryStatus` alanı `"queued"` yapılır.
- ✅ Özetleme tamamlandıysa kullanıcıya `summary` ve `translatedSummary` gösterilir.
- ✅ (Opsiyonel) Paylaşım butonları, dil seçimi, akıllı saat uyumluluğu.

---

## 🗃️ Firestore Veri Yapısı

```json
stories (collection)
├── story_id (document)
    ├── title: "LLMs are eating the world"
    ├── url: "https://someurl.com"
    ├── author: "johnDoe"
    ├── points: 300
    ├── createdAt: timestamp  // ISO 8601'den parse edilir
    ├── summaryStatus: "pending" | "queued" | "done"
    ├── summary: null or string
    ├── translatedSummary: null or string (örneğin Türkçe)
```

## 🧩 Planlanan Özellikler

- [ ] Haberleri Firestore'a aktarma
- [ ] Gemini ile haber özeti oluşturma
- [ ] Türkçeye çeviri (translatedSummary)
- [ ] Flutter uygulaması ile haber listesi gösterimi
- [ ] Kullanıcı dil seçimi desteği (örn. EN / TR)
- [ ] ⌚ Huawei / Android akıllı saat entegrasyonu
- [ ] 📤 Haber paylaşım (Share) butonları
- [ ] Çoklu özet dil desteği (`translatedSummaries` JSON yapısı)
- [ ] `updatedAt` alanı ile güncellenme zamanı takibi
- [ ] Kullanıcı favorileri veya yer imleri desteği

---

## 🧠 Kullanılan Teknolojiler

### 🔧 Backend (Python)
- `requests` – Algolia & Gemini API'den veri çekmek için
- `firebase-admin` – Firestore bağlantısı ve belge işlemleri
- `Google Gemini API` – Özetleme ve çeviri için LLM kullanımı

### 📱 Mobil (Flutter)
- `cloud_firestore` – Firestore'dan veri alma ve yazma
- `http` – Web istekleri (isteğe bağlı özetleme vs.)
- `provider` – Uygulama durumu yönetimi

### ☁️ Diğer Servisler
- Firestore (Firebase) – Gerçek zamanlı veri saklama
- Algolia HackerNews API – Haber verisi kaynağı
- Google Gemini (LLM API) – Özetleme ve çok dilli çıktı
