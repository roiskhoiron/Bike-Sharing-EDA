# modul halaman wrangling
import streamlit as st
import pandas as pd
import io

# membuat fungsi untuk menghitung konversi tipe data object to datetime
def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])
    return df

def wrangling():
    # st.write("## Data Wrangling")

    st.write("### Gathering Data")

    st.write("##### 1. Mendapatkan data penyewaan sepeda yang diakumulasi setiap jam")
    hourly_df = pd.read_csv('data/hour.csv')
    st.write(hourly_df.head(5))

    st.write("##### 2. Mendapatkan data penyewaan sepeda yang diakumulasi setiap hari")
    daily_df = pd.read_csv('data/day.csv')
    st.write(daily_df.head(5))

    # Insight
    st.write("""
    **Insight:**
    - terdapat 17 kolom pada data penyewaan harian dan 16 kolom pada data penyewaan jam-an, 
    yang membedakan yakni adanya kolom `hr` di data penyewaan jam-an.
    - Berikut informasi kolom
        + instant: indeks catatan
        + dteday : tanggal
        + season : musim (1:musim semi, 2:musim panas, 3:musim gugur, 4:musim dingin)
        + yr : tahun (0: 2011, 1:2012)
        + mnth : bulan (1 sampai 12)
        + hr : jam (0 sampai 23)
        + holiday : apakah hari itu libur atau tidak (diambil dari http://dchr.dc.gov/page/holiday-schedule)
        + weekday : hari dalam minggu
        + workingday : jika hari tersebut bukan akhir pekan atau libur, nilainya adalah 1, sebaliknya adalah 0.
        + weathersit : 
            + 1: Cerah, Sedikit awan, Sebagian berawan
            + 2: Kabut + Berawan, Kabut + Awan terpecah, Kabut + Sedikit awan, Kabut
            + 3: Salju ringan, Hujan ringan + Badai + Awan terpecah, Hujan ringan + Awan terpecah
            + 4: Hujan lebat + Es + Badai + Kabut, Salju + Kabut
        + temp : Suhu yang dinormalisasi dalam Celsius. Nilai dibagi dengan 41 (maksimum)
        + atemp: Suhu yang dirasakan dinormalisasi dalam Celsius. Nilai dibagi dengan 50 (maksimum)
        + hum: Kelembaban yang dinormalisasi. Nilai dibagi dengan 100 (maksimum)
        + windspeed: Kecepatan angin yang dinormalisasi. Nilai dibagi dengan 67 (maksimum)
        + casual: jumlah pengguna kasual
        + registered: jumlah pengguna terdaftar
        + cnt: jumlah total penyewaan sepeda termasuk pengguna kasual dan terdaftar
    """)

    st.write("### Assessing Data")

    st.write("#### 1. Menilai kualitas data penyewaan sepeda yang diakumulasi setiap hari")

    st.write("+ #####  Memeriksan Tipe data, Missing value dan Null data")

    st.write('Jumlah data duplikat pada data daily_df:', daily_df.duplicated().sum())
    buffer = io.StringIO()
    daily_df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.write("+ #####  Memeriksa parameter statistik data")
    st.write(daily_df.describe())

    st.write("#### 2. Menilai kualitas data penyewaan sepeda yang diakumulasi setiap hari")

    st.write("+ #####  Memeriksan Tipe data, Missing value dan Null data")
    
    st.write('Jumlah data duplikat pada data hourly_df:', hourly_df.duplicated().sum())

    buffer = io.StringIO()
    hourly_df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.write("+ #####  Memeriksa parameter statistik data")
    st.write(hourly_df.describe())

    st.write("""
    **Insight:**
    - Terdapat masalah dengan tipe data kolom `dteday` yakni `object` atau string yang seharusnya `datetime` karena merupakan data berisi tanggal
    - Tidak terdapat `Missing Value` pada kedua sumber data, indikasi penghitung non-null sama rata disetiap kolom
    - Tidak terdapat `Data Duplicate` pada kedua sumber data, indikasi hasil operasi fungsi pengecekan data duplikasi bernilai 0
    - Tidak ada kejanggalan input pada masing" kolom yang ber`parameter statistik`, indikasi sesuai pada aturan bisnisnya
    """)
    st.write("### Cleaning Data")
    st.write("Dari hasil temuan pada proses sebelumnya struktur dan nilai data pada sumber data hanya mengalami sedikit kasus yang perlu untuk diterapkannya perbaikan, yakni melakukan perubahan tipe data object menjadi datetime saja:")

    st.write("##### 1. Merubah tipe data dteday dari object ke datetime di data penyewaan akumulasi harian")
    daily_df = convert_to_datetime(daily_df, ['dteday'])
    st.write(daily_df.dtypes)
    st.write("data penyewaan akumulasi harian telah malakukan perubahan tipe data `dteday` menjadi `datetime`, dan siap untuk digunakan pada tahap selanjutnya")

    st.write("##### 2. Merubah tipe data dteday dari object ke datetime di data penyewaan akumulasi jam-an")
    hourly_df = convert_to_datetime(hourly_df, ['dteday'])
    st.write(hourly_df.dtypes)
    st.write("data penyewaan akumulasi jam-an telah malakukan perubahan tipe data `dteday` menjadi `datetime`, dan siap untuk digunakan pada tahap selanjutnya")

    st.write("""
    **Insight:**
    - Berhasil melakukan perubahan tipe data pada kolom yang semestinya
    - Data siap untuk diolah ditahap berikutnya
    """)