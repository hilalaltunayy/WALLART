import sqlite3
#sqlite3, küçük projelerde kullanılan, dosya tabanlı bir veritabanı sistemidir.
#MySQL gibi sunucuya gerek yoktur, sadece .db uzantılı bir dosya yeterlidir.

def connect_db():
    conn = sqlite3.connect("harcamalar.db", check_same_thread=False)
    #check_same_thread=False demek: Streamlit birden fazla işlem başlattığında veritabanı çökmesin, rahatça çalışsın.
    c = conn.cursor()
    #Bu satırla veritabanında işlem yapmak için bir “imleç (cursor)” oluştururuz.
    #SQL komutlarını çalıştırırken bu imleci (c) kullanacağız.
    return conn, c

    #sqlite3.connect(...): Uygulama, harcamalar.db adlı bir veritabanı dosyasına bağlanır.
    #Eğer dosya yoksa Python otomatik olarak oluşturur.
    #conn: Bağlantı objesidir. Yani "veritabanıyla iletişim kuracağımız kanal.

def create_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS harcamalar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih TEXT,
            kategori TEXT,
            tutar REAL,
            aciklama TEXT
        )
    ''') #SQL Tablo Oluşturma biliyorsun zaten.
     
     
     
def create_saving_table(c):
     c.execute('''
        CREATE TABLE IF NOT EXISTS kumbara (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ay_yil TEXT UNIQUE,
            hedef REAL,
            biriktirilen REAL
        )
    ''')