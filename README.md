# 📊 İstanbul Sözleşmesi Üzerine Toplumsal Algı Analizi – Tweet Duygu Analizi

## 🎯 Proje Özeti

Bu projede, İstanbul Sözleşmesi hakkında sosyal medya platformu X (eski adıyla Twitter) üzerinden yapılan paylaşımlar analiz edilerek toplumsal duygu durumu ortaya konmuştur. Yaklaşık 16.000 Türkçe tweet toplanarak doğal dil işleme (NLP) ve derin öğrenme yöntemleriyle duygu analizi gerçekleştirilmiştir. Ayrıca, klasik makine öğrenmesi ve derin öğrenme modelleri birleştirilerek hibrit bir yaklaşım denenmiştir.

---

## 🧰 Kullanılan Teknolojiler

- **Python 3.10**
- **Google Colab**
- **Selenium WebDriver** – Tweet toplama
- **Pandas, NumPy** – Veri işleme
- **Regex, urlextract** – Ön işleme
- **Transformers (Hugging Face)** – Derin öğrenme modelleri
- **Scikit-learn** – Makine öğrenmesi algoritmaları
- **Torch** – GPU destekli model eğitimi
- **Matplotlib, WordCloud** – Görselleştirme

---

## 🗂 Veri Toplama ve Ön İşleme

- **Kaynak:** X.com (Twitter)
- **Yöntem:** Anahtar kelime = `"İstanbul Sözleşmesi"`
- **Toplam Tweet:** 15.943
- **Temizlenmiş Tweet:** 13.008 (yaklaşık %18.4 veri kaybı)

### Uygulanan Temizleme Adımları:
- Tekrarlanan tweet’lerin silinmesi
- 3 kelimeden az içeren tweet’lerin çıkarılması
- URL, etiket ve emojilerin dönüştürülmesi
- Stopword’lerin ayıklanması (bağlam belirleyiciler hariç)

---

## 🔍 Modelleme ve Analiz

### 🎓 Denenen Modeller

| Model Adı | Durum |
|-----------|-------|
| `savasy/bert-base-turkish-sentiment-cased` | ❌ |
| `anilguven/bert_tr_turkish_tweet` | ❌ |
| `akoksal/bounti` | ✅ |
| `VRLLab/TurkishBERTweet` | ✅ (Ana model) |

> `VRLLab/TurkishBERTweet`, 894 milyon tweet ile eğitilmiş, Türk sosyal medya diline özel bir modeldir.

---

## ⚙️ Fine-Tuning ve Veri Artırma

| Aşama | Doğruluk | Makro F1 | Ağırlıklı F1 |
|-------|----------|----------|--------------|
| Temel Bounti Modeli | %68.00 | 0.636 | 0.635 |
| Fine-Tuned Bounti (90 tweet) | %72.00 | 0.700 | 0.690 |
| Fine-Tuned + Augmentation (382 tweet) | %70.00 | 0.642 | 0.650 |

> Veri artırmayla 90 tweet’lik eğitim verisi, 382 örneğe genişletildi.

---

## 🔒 Güven Eşiği Analizi

| Güven Eşiği | Doğruluk | F1 Skoru | Kapsam |
|-------------|----------|----------|--------|
| 0.50 | %71.43 | 0.665 | %98.00 |
| **0.65 (Optimal)** | **%75.00** | **0.697** | **%88.00** |
| 0.95 | %78.57 | 0.661 | %56.00 |

---

## 🤖 Klasik Makine Öğrenmesi Modelleri

- **Veri Seti:** 90 eğitim, 50 test (manuel etiketli)
- **Özellik Çıkarımı:** TF-IDF

| Model | Doğruluk | F1 Skoru (Pozitif / Nötr / Negatif) |
|-------|----------|--------------------------------------|
| Random Forest | **%83.61** | 0.74 / 0.61 / 0.90 |
| SVM | %81.88 | 0.75 / 0.49 / 0.89 |
| k-NN | %30.09 | Zayıf performans (özellikle negatif sınıfta düşük recall) |

---

## 🔁 Hibrit Model Yaklaşımı

- Fine-tuned Bounti çıktıları, makine öğrenmesi modellerine giriş olarak verildi.
- Random Forest modeli, hibrit yaklaşımda **%83.51** doğruluk ile en yüksek başarıyı sağladı.
- Hibrit yaklaşım, tek başına klasik veya derin öğrenme yöntemlerine kıyasla daha iyi sonuçlar verdi.

---

## 📈 Görselleştirmeler

- Pozitif/negatif/nötr dağılım grafikleri
- Aylık duygu değişim çizgileri
- Kelime bulutları (öncesi/sonrası)
- En etkileşimli tweet’ler ve kullanıcılar
- Tweet başına ortalama beğeni, yorum, retweet analizi

---

## ✅ Doğrulama

- 50 manuel etiketli tweet ile test
- Ortalama başarı oranı (fine-tuned + augmentation model):  
  - **Doğruluk:** %75  
  - **Makro F1 Skoru:** 0.697

---

## 🏁 Proje Gelişimi

### ✔️ Tamamlananlar
- Geniş tweet toplama
- NLP ön işleme ve görselleştirme
- Farklı modellerin test edilmesi
- Hibrit modelleme
- Performans karşılaştırmaları

### 🎯 Hedefler
- Kendi Türkçe duygu sınıflandırma modelimizi eğitmek
- Veri artırma yöntemlerini zenginleştirmek
- Akademik makale ve açık kaynak paylaşımı yapmak

---

## 📚 Kaynaklar

- [VRLLab/TurkishBERTweet](https://huggingface.co/VRLLab/TurkishBERTweet)
- [akoksal/bounti](https://huggingface.co/akoksal/bounti)
- [scikit-learn](https://scikit-learn.org/)

---

## 👩‍💻 Geliştirici

- **Ad:** Ayşenur Arslan  
 
- **Danışman:** Doç. Dr. Nurdan Baykan  
- **Üniversite:** Konya Teknik Üniversitesi – Bilgisayar Mühendisliği

---

## 📝 Lisans

Bu proje yalnızca akademik kullanım içindir. İzinsiz kopyalanamaz. Bilgi alıntılamak için kaynak gösterilmesi gerekmektedir.
