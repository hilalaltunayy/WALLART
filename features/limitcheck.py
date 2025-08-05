import streamlit as st

def check_limit(df):
    st.subheader("🚨 Harcama Limiti Kontrolü")

    limit = st.number_input("Aylık harcama limitini belirle (₺)", min_value=0.0, format="%.2f")
    toplam = df["Tutar"].sum()

    if limit > 0:
        if toplam > limit:
            st.error(f"⚠️ Dikkat! Harcama limitini {toplam - limit:.2f}₺ aştın.")
        else:
            kalan = limit - toplam
            st.success(f"✅ Harcama limitin içinde kaldın. {kalan:.2f}₺ limitin kaldı.")
    else:
        st.info("Henüz limit belirlemedin.")