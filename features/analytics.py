import streamlit as st
#streamlit, Python’la web arayüzü oluşturmaya yarayan bir kütüphanedir.
#as st demek: Artık her yerde streamlit yerine kısaca st yazacağım demektir.

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def show_category_chart(df):
    st.subheader("📊 Kategori Bazlı Harcama Grafiği")

    if not df.empty:
        kategori_toplam = df.groupby("Kategori")["Tutar"].sum()
        fig, ax = plt.subplots()
        kategori_toplam.plot(kind="bar", color="purple", ax=ax)
        ax.set_ylabel("Toplam Harcama (₺)")
        ax.set_xlabel("Kategori")
        ax.set_title("Kategoriye Göre Toplam Harcamalar")
        st.pyplot(fig)
    else:
        st.info("Henüz kayıtlı harcama yok.")

def show_date_filter(df):
    st.header("📆 Tarihe Göre Harcamalar")
    tarih_aralik = st.date_input("Tarih Aralığı Seçiniz", [datetime(2024, 1, 1), datetime.today()])

    if len(tarih_aralik) == 2:
        baslangic, bitis = tarih_aralik
        mask = (df["Tarih"] >= str(baslangic)) & (df["Tarih"] <= str(bitis)) 
        filtreli_df = df[mask]

        st.subheader("🔍 Seçilen Aralıkta Harcamalar")
        st.dataframe(filtreli_df, use_container_width=True)
        toplam = filtreli_df["Tutar"].sum()
        st.markdown(f"💰 **Toplam harcama:** ₺{toplam:.2f}")

        #Markdown = Kalın yazı, italik, başlık gibi basit biçimlendirme dili.
        # f-string yani formatlı yazı. Python’da değişkenleri metne yerleştirmenin kolay yolu.

        if not filtreli_df.empty:
            kategori_toplam = filtreli_df.groupby("Kategori")["Tutar"].sum()
            fig2, ax2 = plt.subplots()
            kategori_toplam.plot(kind="bar", color="orange", ax=ax2)
            ax2.set_title("Seçilen Aralıkta Kategori Bazlı Harcamalar")
            ax2.set_ylabel("Tutar (₺)")
            ax2.set_xlabel("Kategori")
            st.pyplot(fig2)
        else:
            st.info("Bu tarih aralığında harcama bulunamadı.")
