import streamlit as st
from database import connect_db, create_table
from features.spending_form import show_form
from features.history import show_history
from features.analytics import show_category_chart, show_date_filter

from features.saving import show_saving_feature
from features.limitcheck import check_limit
from features.ai_advisor import ai_advice

from database import connect_db, create_table, create_saving_table

from features.saving import show_saving_feature

st.set_page_config(page_title="Wallart", layout="wide")
st.title("📊 WALLART - Harcamalarını Kontrol Et")

# Veritabanı bağlantısı
conn, c = connect_db()
create_table(c)
create_saving_table(c)

# Harcama ekleme formu
show_form(c, conn)

# Geçmişi göster
df = show_history(conn,c)

# Eğer veri varsa grafik ve filtre
if df is not None:
    show_category_chart(df)
    show_date_filter(df)

    show_saving_feature(conn)
    check_limit(df)
    ai_advice(df)


