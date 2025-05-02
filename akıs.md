# 🔎 HackerNews Summary App

Bu proje, **Hacker News** üzerindeki popüler haberleri toplayıp, yapay zeka ile özetleyip çok dilli olarak sunan bir sistemdir. Mobil (Flutter) ve Python tabanlı backend'den oluşur.

## 🧩 Bileşenler

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


## Eklenecekler
-PLANLANAN EKLENTİLER
    -DİL SEÇİMİ
    -AKILLI SAAT ENTEGRASYONU