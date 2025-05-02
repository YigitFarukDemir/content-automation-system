1. Python backend (Algolia ile):
   🔹 10 popüler HackerNews hikayesini çeker
   🔹 Firestore'a yazar (summaryStatus: "pending")

2. Flutter app:
   🔹 Firestore'daki hikayeleri çeker
   🔹 Kullanıcı birini seçerse -> summaryStatus: "queued"

3. Python backend:
   🔹 summaryStatus == "queued" hikayeleri Gemini ile özetler + Türkçe çevirir
   🔹 summary ve translatedSummary alanlarına yazar
   🔹 summaryStatus: "done"

4. Flutter app:
   🔹 summaryStatus: "done" olanları gösterir
   🔹 (İsteğe bağlı: paylaşım butonu vs.)

PLANLANAN FIRESTORE YAPISI
    stories (collection)
    ├── story_id_1 (document)
    │   ├── title: "LLMs are eating the world"
    │   ├── url: "https://someurl.com"
    │   ├── author: "johnDoe"
    │   ├── points: 300
    │   ├── createdAt: timestamp (Algolia'dan gelen ISO date parse edilecek)
    │   ├── summaryStatus: "pending" | "queued" | "done"
    │   ├── summary: null or string
    │   ├── translatedSummary: null or string

PLANLANAN EKLENTİLER
    -DİL SEÇİMİ
    -AKILLI SAAT ENTEGRASYONU