# 📊 Wallart - Harcama Takip Uygulaması

Wallart, kişisel harcamalarınızı takip etmenizi, kategorilere göre analiz yapmanızı ve birikim hedeflerine ulaşmanızı sağlayan interaktif bir bütçe takip uygulamasıdır. Streamlit ile geliştirilmiştir.
---------------------------

## 🚀 Özellikler

- 📥 Harcama ekleme (kategori, tarih, açıklama)
- 🗃️ Harcama geçmişi ve silme özelliği
- 📊 Kategori bazlı harcama grafikleri
- 📅 Tarih aralığına göre filtreleme
- 💰 Aylık birikim hedefi belirleme ve durumu takip etme
- 🚨 Limit kontrolü: Belirlediğin limit aşıldığında uyarı
- 🤖 Yapay zeka destekli harcama tavsiyeleri (AI Advisor)
---------------------------

## ⚙️ Kurulum

### 1. Gerekli ortamı oluştur

```bash
python -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

## Gerekli Paketler
pip install -r requirements.txt

streamlit run app.py

📁 Dosya Yapısı
pgsql
Kopyala
Düzenle
Wallart/
│
├── app.py
├── harcamalar.db
├── requirements.txt
├── README.md
├── .gitignore
│
├── database.py
├── features/
│   ├── spending_form.py
│   ├── history.py
│   ├── analytics.py
│   ├── saving.py
│   ├── limitcheck.py
│   └── ai_advisor.py


👩‍💻 Geliştirici

Hilal Yeşim Altunay
Teknik olarak geliştirdiğim ilk profesyonel projeydi. 
Proje geliştirme sürecinde keyifli vakit geçirdim. Pek çok teknolojiyi kullanmayı öğrendim.
İletişim: altunayhilal14@gmail.com
