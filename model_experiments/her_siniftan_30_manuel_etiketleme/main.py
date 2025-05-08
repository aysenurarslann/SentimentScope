import pandas as pd  # Pandas kütüphanesini içe aktar
#from IPython.display import display, clear_output  # Colab uyumlu ekran temizleme işlemleri için gerekli modüller

# 📌 1. Veriyi Oku (CSV dosyasını oku)
try:
    df = pd.read_csv("her_siniftan_30_manuel_etiketleme\\tweets.csv")  # Tweet verisini içeren CSV dosyasını oku
except FileNotFoundError:  # Dosya bulunamazsa hata mesajı ver
    print("Hata: 'tweets.csv' dosyası bulunamadı! Lütfen yüklediğinizden emin olun.")
    exit()  # Programı sonlandır

# **Etiketli veri yok, tüm tweetleri al**
unlabeled = df.sample(frac=1).reset_index(drop=True)  # Veriyi rastgele karıştır ve indeksleri sıfırdan başlat

# 📌 2. Etiket Sayacı (Her sınıftan 30 tane olacak)
label_counts = {"pozitif": 0, "nötr": 0, "negatif": 0}  # Her sınıfın başlangıçta 0 etiketi var
max_count = 30  # Her sınıftan en fazla 30 tweet etiketlenecek
labeled_data = []  # Etiketlenen tweetleri saklayacak liste

# 📌 3. Kullanıcıdan Etiket Al (Colab Uyumlu)
def label_tweets():  # Etiketleme işlemini gerçekleştiren fonksiyon
    global labeled_data  # Fonksiyon içinde labeled_data değişkenine erişmek için

    for idx, row in unlabeled.iterrows():  # Tüm tweetler üzerinde dön
        tweet = row["text"]  # Tweet'in metnini al

        # Eğer her sınıftan 30 veri etiketlendiyse işlemi durdur
        if all(count >= max_count for count in label_counts.values()):
            print("\n✅ **Etiketleme tamamlandı!**")
            break  # Döngüyü sonlandır

        # Geçerli etiketlenebilir sınıfları belirle
        available_labels = [label for label, count in label_counts.items() if count < max_count]

        # Eğer sadece dolu sınıf için uygun bir tweet geldiyse bunu atla
        if not available_labels:
            print("⏩ Bu tweeti atlıyoruz...")
            continue  # Bir sonraki tweeti işlemeye devam et

        # **Tweet'i ekrana yazdır**
        print(f"\n📌 **Tweet:** {tweet}\n")
        print(f"🟢 Pozitif ({label_counts['pozitif']}/30)\n🔵 Nötr ({label_counts['nötr']}/30)\n🔴 Negatif ({label_counts['negatif']}/30)")

        # **Ekran temizleme işleminden önce input al**
        while True:  # Geçerli bir etiket girilene kadar döngüde kal
            label = input(f"Lütfen etiketi gir ({', '.join(available_labels)}) veya 'geç' yazarak tweeti atla: ").strip().lower()  # Kullanıcıdan etiket al

            if label == "geç":  # Eğer kullanıcı "geç" yazarsa tweeti atla
                print("⏩ Tweet atlandı.")
                break
            if label in available_labels:  # Eğer girilen etiket geçerliyse döngüden çık
                labeled_data.append([tweet, label])  # Tweet ile birlikte etiketi listeye ekle
                label_counts[label] += 1  # Seçilen etiketin sayısını artır
                break
            print(f"⚠️ Geçersiz veya dolu sınıf seçildi! Tekrar deneyin. (Geçerli sınıflar: {', '.join(available_labels)})")

        # **Ekranı temizlemeden önce bir tweet etiketlendiği için bekle**
        #clear_output(wait=True)  # Terminalde ekranı temizle (Colab'da düzgün çalışır)

    # 📌 4. Veriyi Kaydet (Etiketlenen veriyi CSV dosyasına kaydet)
    df_labeled = pd.DataFrame(labeled_data, columns=["tweet", "label"])  # Etiketli veriyi DataFrame'e çevir
    df_labeled.to_csv("30_data_every_each_class_labeled_tweets.csv", index=False)  # CSV dosyası olarak kaydet
    print("\n✅ Etiketlenen veriler **30_data_every_each_class_labeled_tweets.csv** dosyasına kaydedildi.")

# 📌 5. Etiketleme Başlat
label_tweets()  # Fonksiyonu çağırarak etiketleme işlemini başlat
