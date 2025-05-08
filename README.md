# 📊 İstanbul Sözleşmesi Üzerine Toplumsal Algı Analizi – Tweet Duygu Analizi

## 🎯 Proje Özeti

Bu projede, İstanbul Sözleşmesi hakkında sosyal medya platformu X (eski adıyla Twitter) üzerinden yapılan paylaşımlar analiz edilerek toplumsal duygu durumu ortaya konmuştur. Yaklaşık 16.000 Türkçe tweet toplanarak çeşitli veri işleme adımlarından geçirilmiş, ardından modern doğal dil işleme (NLP) yöntemleri ve derin öğrenme tabanlı modellerle duygu analizi gerçekleştirilmiştir.

---

## 🧰 Kullanılan Teknolojiler

- **Python 3.10**
- **Google Colab**
- **Selenium WebDriver** – Tweet toplama
- **Pandas, NumPy** – Veri işleme
- **Regex, urlextract, argparse** – Ön işleme
- **Transformers (Hugging Face)** – Duygu analizi modelleri
- **Matplotlib, WordCloud** – Görselleştirme
- **Torch** – Model tahmini ve GPU desteği

---

## 🗂 Veri Toplama Süreci

- **Kaynak:** X.com (Twitter)
- **Yöntem:** Anahtar kelime = "İstanbul Sözleşmesi"
- **Toplam Tweet Sayısı:** 15.943
- **Toplanan Bilgiler:**
  - Tweet ID
  - Kullanıcı Adı
  - Tweet Metni
  - Tarih
  - Beğeni, Retweet ve Yorum Sayısı
  - Tweet Bağlantısı
  - Hashtagler
  - Görseller (varsa)

---

## 🧹 Veri Ön İşleme

- Eksik/verisiz günlerin belirlenmesi
- Tekrarlanan tweet’lerin kaldırılması
- 3 kelimeden az olan metinlerin filtrelenmesi
- URL ve kullanıcı etiketlerinin temizlenmesi
- Emojilerin anlamlı karşılıklarla çevrilmesi
- Stopword’lerin ayıklanması (ancak “değil” gibi bağlam belirleyiciler korunmuştur)

---

## 🔍 Modelleme ve Analiz

### 🎓 Denenen Modeller:
1. `savasy/bert-base-turkish-sentiment-cased` ❌
2. `anilguven/bert_tr_turkish_tweet` ❌
3. `akoksal/bounti` ✅
4. `VRLLab/TurkishBERTweet` ✅ 

> **Not:** `VRLLab/TurkishBERTweet`, 894 milyon tweet ile eğitilmiş, Türk sosyal medya diline özgü optimize edilmiş bir modeldir.

---

### 🧪 Uygulanan Adımlar:
- Tweet metinleri tokenizer ile dönüştürüldü
- Her tweet için **pozitif**, **negatif** ya da **nötr** etiketi tahmin edildi
- Sonuçlar CSV olarak kaydedildi
- Etiket dağılımları ve zaman bazlı duygu değişimleri grafiklerle analiz edildi
- En çok beğeni, yorum ve retweet alan tweet’ler duygu bazlı incelendi

---

## 📊 Sonuçlar

- Temizleme sonrası veri sayısı: **13.008** (18.41% veri kaybı)
- Etiket dağılımları:
  - Pozitif
  - Negatif
  - Nötr

- **En Yoğun Tweet Dönemi:** 2021 yılı Mart ayı (sözleşmeden çekilme süreci)
- **En Etkileşimli Tweet:** 6.611 beğeni, 1.927 retweet
- **En Aktif Kullanıcılar:** İlk 10 kullanıcı analiz edildi

---

## 📈 Görselleştirmeler

- Kelime bulutları (öncesi/sonrası)
- Pozitif/negatif/nötr etiket bar grafikleri
- Aylık ve haftalık duygu değişim grafikleri
- Tweet başına ortalama etkileşim sayıları

---

## ✅ Doğrulama ve Değerlendirme

- 50 tweet manuel olarak etiketlendi
- Model çıktılarıyla karşılaştırıldı
- Ortalama başarı oranı: **%58**

---

## 🏁 Dönemsel Gelişim ve Hedefler

### Gerçekleştirilenler:
- Veri toplama ve temizleme
- Duygu analizi model testi
- Etkileşim analizi
- Görselleştirme

### Gelecek Hedefler:
- Kendi duygu sınıflandırma modelimizi eğitmek
- Augmentasyonla daha yüksek başarı elde etmek
- Sonuçları makale olarak yayımlamak

---

## 📚 Kaynaklar

- [VRLLab/TurkishBERTweet](https://huggingface.co/VRLLab/TurkishBERTweet)
- [anilguven/bert_tr_turkish_tweet](https://huggingface.co/anilguven/bert_tr_turkish_tweet)
- [akoksal/bounti](https://huggingface.co/akoksal/bounti)
- [savasy/bert-base-turkish-sentiment-cased](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased)

---

## 👩‍💻 Geliştirici

- **Ad:** Ayşenur Arslan 



