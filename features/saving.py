import streamlit as st
import datetime

def show_saving_feature(conn):
    st.subheader("💰 Kumbara - Aylık Birikim Takibi")

    today = datetime.date.today()
    current_month = today.strftime("%Y-%m")

    c = conn.cursor()

    # Önce var olan kayıt var mı diye kontrol et
    c.execute("SELECT hedef, biriktirilen FROM kumbara WHERE ay_yil = ?", (current_month,))
    result = c.fetchone()

    if result:
        hedef, biriktirilen = result
    else:
        hedef = 0.0
        biriktirilen = 0.0

    with st.form("saving_form"):
        yeni_hedef = st.number_input("🎯 Aylık birikim hedefin nedir? (₺)", min_value=0.0, value=hedef, format="%.2f")
        yeni_birikim = st.number_input("🏦 Bu ay biriktirdiğin tutar nedir? (₺)", min_value=0.0, value=biriktirilen, format="%.2f")

        submitted = st.form_submit_button("Kaydet")
        if submitted:
            # Kayıt varsa güncelle, yoksa ekle
            c.execute("REPLACE INTO kumbara (ay_yil, hedef, biriktirilen) VALUES (?, ?, ?)",
                      (current_month, yeni_hedef, yeni_birikim))
            conn.commit()
            st.success("Kumbara verileri kaydedildi!")

    # Karşılaştırma
    if hedef > 0:
        kalan = max(0, hedef - biriktirilen)
        if kalan == 0:
            st.success("🎉 Harika! Bu ayki hedefini doldurdun!")
        else:
            st.info(f"Bu ay {hedef:.2f}₺ biriktirmek için {kalan:.2f}₺ daha biriktirmelisin.")
    else:
        st.warning("🔔 Henüz bir hedef belirlemedin.")

        #Streamlit'in kullanıcı arayüzüne bir şeyler gösteriyor: st.info, st.success, st.warning gibi.
        #Yani: ekrana çıktı basıyor, bir şey göstermek dışında başka bir iş yapmıyor.
        #Dolayısıyla return etmemizi gerektirecek bir durum yok.