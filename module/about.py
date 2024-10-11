# modul halaman about
import streamlit as st

def about():
    # menampilkan readme.md
    with open('data/basic-info.md', 'r') as file:
        data = file.read()
        st.write(data)

    st.write("proyek analisa data ini dibuat oleh:")
    st.write("""
    # Proyek Analisis Data: BIKE SHARING DATASET
    - **Nama:** ROIS HOIRON
    - **Email:** rois.khoiron@gmail.com
    - **ID Dicoding:** khoironrois
             """)
    
    st.write("## Pertanyaan Bisnis")

    st.write("""
    1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
    \n `Apakah ada pola tertentu dalam jumlah penyewaan sepeda berdasarkan suhu, kelembaban, atau curah hujan?`

    2. Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
    \n `Apakah ada perbedaan signifikan dalam jumlah penyewaan sepeda antara musim panas, musim gugur, musim dingin, danmusim semi?`

    3. Bagaimana pengaruh hari dalam minggu terhadap jumlah penyewaan sepeda?
    \n `Apakah ada perbedaan dalam jumlah penyewaan sepeda antara hari kerja dan akhir pekan?`

    4. Bagaimana pengaruh jam dalam sehari terhadap jumlah penyewaan sepeda?
    \n `Apakah ada jam-jam tertentu dalam sehari yang menunjukkan puncak penyewaan sepeda?`

    5. Apakah ada peristiwa atau anomali yang mempengaruhi jumlah penyewaan sepeda?
    \n `Apakah ada peristiwa khusus yang menyebabkan lonjakan atau penurunan jumlah penyewaan sepeda?`

    6. Bagaimana tren jumlah penyewaan sepeda dari waktu ke waktu?
    \n `Apakah ada tren peningkatan atau penurunan dalam jumlah penyewaan sepeda dari tahun 2011 ke 2012?`

    7. Bagaimana pengaruh variabel lain seperti kecepatan angin dan visibilitas terhadap jumlah penyewaan sepeda?
    \n `Apakah variabel-variabel ini memiliki korelasi yang signifikan dengan jumlah penyewaan sepeda?`
    """)