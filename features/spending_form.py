import streamlit as st
 #streamlit, Python’la web arayüzü oluşturmaya yarayan bir kütüphanedir.
 #as st demek: Artık her yerde streamlit yerine kısaca st yazacağım demektir.

from datetime import datetime

def show_form(c, conn):
    st.subheader("➕ Harcama Ekle")

    #Harcama Giriş Formu
    #with yapısı: Bir bloğun başlangıcını belirtir.
    #st.form("..."): Sayfada bir form alanı oluşturur. Bu form, bir butona tıklanınca çalışır.

    with st.form("Harcama Formu"):
        tarih = st.date_input("📅 Tarih", datetime.today())
        kategori = st.selectbox("📂 Kategori", ["Yiyecek", "Ulaşım", "Fatura", "Eğlence", "Sağlık", "Diğer"])
        tutar = st.number_input("💸 Tutar (₺)", min_value=0.0, format="%.2f")
        aciklama = st.text_input("📝 Açıklama")

        submitted = st.form_submit_button("Kaydet")

        #Buton oluşturur. Kullanıcı tıklayınca formu gönderir.
        #Tıklanırsa submitted = True olur, aksi halde False.

        if submitted:
            c.execute("INSERT INTO harcamalar (tarih, kategori, tutar, aciklama) VALUES (?,?,?,?)",
                      (str(tarih), kategori, tutar, aciklama))
            conn.commit()
            st.success("✅ Harcama kaydedildi!")
            
            #Eğer kullanıcı "Kaydet"e bastıysa:
            #Veritabanına bir kayıt ekle (SQL komutu: INSERT INTO)
            #?’ler yer tutucudur, güvenlik için (SQL injection’a karşı)
            #(str(tarih), kategori, tutar, aciklama): Formdan gelen veriler
            #conn.commit(): Veriyi kaydet
            #st.success(...): Kullanıcıya mesaj göster (yeşil kutuda)"""
