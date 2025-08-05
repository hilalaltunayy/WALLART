import streamlit as st
#streamlit, Python’la web arayüzü oluşturmaya yarayan bir kütüphanedir.
#as st demek: Artık her yerde streamlit yerine kısaca st yazacağım demektir.
import pandas as pd

def show_history(conn, c):
    st.header("📋 Harcama Geçmişi")
    c.execute("SELECT * FROM harcamalar ORDER BY tarih DESC")
    veriler = c.fetchall()

    

    if veriler:
        df = pd.DataFrame(veriler, columns=["ID", "Tarih", "Kategori", "Tutar", "Aciklama"])
        #df → Pandas DataFrame (tablo yapısı)

        for i, row in df.iterrows():
            #`df.iterrows()` → DataFrame’deki her satırı tek tek döner.
            with st.expander(f"{row['Tarih']} | {row['Kategori']} | {row['Tutar']}₺"):
                #st.expander() → Tıklanınca açılan bir kutu oluşturur.
                #
                st.write(f"📝 {row['Aciklama']}")

                col1, _ = st.columns([1, 4])
                #columns=[...] → Sütun başlıkları (veritabanı tablosuna uygun olarak sırayla yazılır)
                   
                with col1:
                    
                #Sayfayı yatay olarak 2 sütuna böler.
                #col1: Buton için dar sütun (1 birim genişlik)
                
                    if st.button("❌ Sil", key=f"sil_{row['ID']}"): #❌ Sil` butonunu sadece `col1` sütunu içinde göstermek için.
                        delete_expense(conn, row['ID']) #Her butona benzersiz bir anahtar verir (yoksa hepsi aynı kabul edilir)
                        st.success("Kayıt silindi!")
                        st.rerun()#Streamlit sürümü şu an bunu destekliyor experimental çalışmadı.
                        #st.experimental_rerun()   #Sayfayı yeniden yükler. Böylece silinen kayıt hemen ekrandan kaybolur
                        # _→ Python’da "bunu kullanmayacağım" anlamına gelir.
                        #Eğer kullanıcı sil butonuna bastıysa, ilgili `ID`’li harcama `delete_expense()` fonksiyonuyla silinir.
        return df
             #DataFrame’i geri döndürür. Böylece bu fonksiyon başka yerlerde bu veriyi kullanmak isterse erişebilir.
    else:


        st.info("Henüz harcama eklenmedi.")
        return None

def delete_expense(conn, expense_id):
    c = conn.cursor()
    c.execute("DELETE FROM harcamalar WHERE ID = ?", (expense_id,))
    conn.commit() #Silme işlemini kalıcı hale getirir (veritabanını günceller)
    
        #bu kod Veritabanından tüm verileri çeker
        #Pandas ile bir tabloya (DataFrame) dönüştürür
        #Streamlit üzerinden gösterir