import streamlit as st

def ai_advice(df):
    st.subheader("🤖 Harcama Tavsiyesi (Yapay Zeka Simülasyonu)")

    if df.empty:
        st.info("Öneri verebilmem için önce harcama girmelisin.")
        return

    fazla_kategori = df.groupby("Kategori")["Tutar"].sum().idxmax()

    st.markdown(f"🧠 **Tavsiyem:** Bu ay en çok `{fazla_kategori}` kategorisinde harcama yaptın. Bu alanda tasarruf etmeyi düşünebilirsin.")