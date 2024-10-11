# modul halaman exploratory
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

hourly_df = pd.read_csv('../data/hour.csv')
daily_df = pd.read_csv('../data/day.csv')

def exploratory():
    # st.write("## Exploratory Data Analysis")

    st.write("#### Langkah 1: Statistik Deskriptif | untuk memahami distribusi data")
    
    st.write("+ Statistik deskriptif untuk data harian")
    st.write(daily_df.describe(include='all'))
    
    st.write("+ Statistik deskriptif untuk data jam-an")
    st.write(hourly_df.describe(include='all'))

    st.write("#### Langkah 2: Demografi Data | untuk memahami pola data")
    
    st.write("+ Jumlah penyewaan sepeda berdasarkan cuaca")
    hourly_df['weathersit'] = hourly_df['weathersit'].map({1: 'Clear', 2: 'Mist', 3: 'Light Rain', 4: 'Heavy Rain'})
    st.write(hourly_df.groupby('weathersit')['cnt'].agg(['mean', 'median', 'std', 'min', 'max']).sort_values(by='mean', ascending=False))

    st.write("+ Jumlah penyewaan sepeda berdasarkan musim")
    hourly_df['season'] = hourly_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    st.write(hourly_df.groupby('season')['cnt'].agg(['mean', 'median', 'std', 'min', 'max']).sort_values(by='mean', ascending=False))

    st.write("+ Jumlah penyewaan sepeda berdasarkan hari")
    daily_df['dteday'] = pd.to_datetime(daily_df['dteday'])
    daily_df['day_of_week'] = daily_df['dteday'].dt.day_name()
    st.write(daily_df.groupby('day_of_week')['cnt'].agg(['mean', 'median', 'std', 'min', 'max']).sort_values(by='mean', ascending=False))

    st.write("+ Jumlah penyewaan sepeda berdasarkan jam")
    st.write(hourly_df.groupby('hr')['cnt'].agg(['mean', 'median', 'std', 'min', 'max']))

    st.write("+ Peristiwa atau anomali yang mempengaruhi jumlah penyewaan sepeda")
    # Menghitung Z-score untuk jumlah penyewaan sepeda
    daily_df['z_score'] = (daily_df['cnt'] - daily_df['cnt'].mean()) / daily_df['cnt'].std()

    # Menentukan threshold untuk anomali (misalnya, Z-score > 2 atau Z-score < -2)
    anomalies = daily_df[np.abs(daily_df['z_score']) > 2]

    # Menampilkan data yang dianggap anomali
    anomalies_sorted = anomalies[['dteday', 'cnt', 'z_score']].sort_values(by='dteday', ascending=True)

    st.write(anomalies_sorted)
    st.write('data yang dianggap anomali telah disimpan pada file anomalies.csv berjumlah', anomalies_sorted.shape[0], 'baris/data')

    st.write("+ Trend penyewaan sepeda berdasarkan waktu")
    # Mengelompokkan data berdasarkan tanggal untuk melihat tren bulanan
    monthly_trend = daily_df.groupby(daily_df['dteday'].dt.to_period('M'))['cnt'].sum().reset_index()

    # Menampilkan tren harian
    st.write(monthly_trend.head(24))

    st.write("+ Pengaruh variabel lain seperti kecepatan angin dan visibilitas terhadap jumlah penyewaan sepeda")
    # Menghitung matriks korelasi
    correlation_matrix = daily_df[['temp', 'hum', 'windspeed', 'cnt']].corr()
    st.write("Matriks Korelasi:")
    st.write(correlation_matrix)

    # Memilih fitur dan target
    X = daily_df[['temp', 'hum', 'windspeed']]
    y = daily_df['cnt']

    # Membuat model regresi linear
    model = LinearRegression()
    model.fit(X, y)

    # Menampilkan koefisien regresi
    st.write("\nKoefisien Regresi:")
    st.write(pd.DataFrame(model.coef_, X.columns, columns=['Coefficient']))

    st.write("""
    **Insight:**
    - Kami menemukan bahwa cuaca cerah menghasilkan jumlah penyewaan sepeda terbanyak diikuti cuaca berawan, hujan ringan dan badai
    - Kami menemukan bahwa musim gugut menghasilkan jumlah penyewaan sepeda terbanyak diikuti musim panas, dingin dan semi
    - Kami menemukan bahwa hari jumat menghasilkan jumlah penyewaan sepeda terbanyak diikuti kamis, sabtu, rabu, selasa, senin dan minggu
    - Kami menemukan bahwa di jam 17 - 18 (sore) menghasilkan jumlah penyewaan sepeda terbanyak dikikuti jam 8 (pagi) hingga yang tersedikit yakni jam 4 (dini hari)
    - Kami menemukan bahwa 10 data yang terindikasi anomali dalam data penyewaan sepeda, dari hari tanggal 2012-09-15 retensi penyewaan sepeda menaik karena ada event `H Street Festival`, banyak orang mengunjungi acara jalanan tahunan yang populer di Washington, D.C, kemudian terjadi penurunan pada tanggal 2012-10-29 bertepatan dengan `Hurricane Sandy` yakni badai besar yang dikenal badai perusak besar sehingga banyak orang tidak berkegiatan diluar ruangan karenanya, dan masih banyak insident lainnya pada rekam data anomali pada tanggal-tanggal tersebut yang mempengaruhi persewaan sepeda.
    - kami menemukan tren persewaan sepeda dalam rentang 2 tahun (2011-2012) dengan re-presentasi akumulasi bulanan ditemukan tren menaik namun terjadi penurunan persewaan yang signifikan di bulan oktober disetiap tahunnya.
    - Suhu (temp) adalah faktor yang paling berpengaruh dan memiliki hubungan positif yang kuat dengan jumlah (cnt). sedankan kelembapan (hum) dan kecepatan angin (windspeed) memiliki pengaruh negatif
    """)

