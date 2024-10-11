# modul halaman explanatory
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

hourly_df = pd.read_csv('data/hour.csv')
daily_df = pd.read_csv('data/day.csv')
daily_df['dteday'] = pd.to_datetime(daily_df['dteday'])
hourly_df['dteday'] = pd.to_datetime(hourly_df['dteday'])

sns.set_style('dark')
def explanatory():
    st.write("### Pertanyaan 1:") 

    daily_df['weathersit_name'] = daily_df['weathersit'].map({1: 'Clear', 2: 'Mist', 3: 'Light Rain', 4: 'Heavy Rain'})

    colors = ["#D3D3D3", "#72BCD4", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='weathersit_name', y='cnt', data=daily_df, palette=colors, ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Cuaca (Weather Situation x Count)')
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

    st.write("### Pertanyaan 2:")
    daily_df['season_name'] = daily_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='season_name', y='cnt', data=daily_df, palette=colors, ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Musim (Season x Count)')
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

    st.write("### Pertanyaan 3:")
    daily_df['day_of_week'] = daily_df['dteday'].dt.day_name()

    colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='day_of_week', y='cnt', data=daily_df.sort_values(by='dteday'), palette=colors, ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Hari (Day of Week x Count)')
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

    st.write("### Pertanyaan 4:")
    hourly_df['hr'] = hourly_df['hr'].astype('category')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='hr', y='cnt', data=hourly_df, palette='viridis', ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Jam (Hour x Count)')
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

    st.write("### Pertanyaan 5:")
    # Menampilkan anomali data denga z-score > 2 atau z-score < -2
    daily_df['z_score'] = (daily_df['cnt'] - daily_df['cnt'].mean()) / daily_df['cnt'].std()
    anomalies = daily_df[(daily_df['z_score'] > 2) | (daily_df['z_score'] < -2)]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(daily_df['dteday'], daily_df['cnt'], color='gray', label='Penyewaan Sepeda')
    ax.scatter(anomalies['dteday'], anomalies['cnt'], color='red', label='Anomali')
    ax.set_title('Penyewaan Sepeda Harian')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.legend()
    st.pyplot(fig)

    st.write("### Pertanyaan 6:")
    plt.figure(figsize=(10, 6))
    monthly_trend = daily_df.groupby(daily_df['dteday'].dt.to_period('M')).agg({'dteday': 'min', 'cnt': 'sum'})

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_trend['dteday'], monthly_trend['cnt'], marker='o')
    ax.set_title('Tren Penyewaan Sepeda (2011 -)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig) 

    st.write("### Pertanyaan 7:") 
    correlation_matrix = daily_df[['temp', 'hum', 'windspeed', 'cnt']].corr()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Matriks Korelasi')
    st.pyplot(fig)

    # Memilih fitur yang relevan untuk clustering
    features = hourly_df[['temp', 'hum', 'windspeed', 'cnt']]

    # Melakukan normalisasi data
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Menggunakan KMeans untuk clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    hourly_df['cluster'] = kmeans.fit_predict(scaled_features)

    # Visualisasi hasil clustering
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x=hourly_df['temp'], y=hourly_df['cnt'], hue=hourly_df['cluster'], palette='viridis', ax=ax)
    ax.set_title('Clustering Analysis of Bike Rentals')
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Count of Rentals')
    st.pyplot(fig)

    st.write("""
    **Insight:**
    - Berdasarkan grafik ini, cuaca cerah (Clear) menjadi faktor utama dengan jumlah penyewaan sepeda terbanyak, mencapai lebih dari 4.500 unit. Cuaca berawan (Mist) menyusul di urutan kedua dengan angka penyewaan yang lebih rendah, sementara cuaca hujan ringan (Light Rain) mencatatkan angka penyewaan paling sedikit, menunjukkan bahwa orang lebih suka menyewa sepeda saat cuaca cerah.

    - Grafik ini menunjukkan bahwa musim gugur (Fall) memiliki jumlah penyewaan sepeda tertinggi, dengan lebih dari 5.500 unit. Musim panas (Summer) mengikuti di urutan kedua, dengan angka penyewaan yang sedikit lebih rendah. Sementara itu, musim dingin (Winter) dan musim semi (Spring) mencatatkan angka penyewaan yang paling rendah, dengan musim semi berada di urutan terbawah.

    - Berdasarkan grafik ini, hari Jumat adalah hari yang paling ramai dalam hal penyewaan sepeda. Setelah Jumat, Kamis dan Sabtu mengikuti dengan angka penyewaan yang juga tinggi. Sementara itu, Rabu, Selasa, dan Senin berada di posisi berikutnya. Yang menarik, meskipun akhir pekan sering dianggap waktu favorit untuk aktivitas luar ruangan, hari Minggu justru mencatatkan jumlah penyewaan sepeda paling sedikit.

    - Pada grafik ini, selain hari dan musim, waktu juga menunjukkan peran penting dalam tren penyewaan sepeda. Jam 17.00 hingga 18.00 (sore hari) adalah waktu puncak penyewaan, kemungkinan besar karena banyak orang yang pulang kerja. Jam 08.00 (pagi hari) mencatatkan lonjakan penyewaan kedua, mungkin karena banyak orang yang mulai memulai aktivitas harian mereka. Sebaliknya, pada jam 04.00 dini hari, tingkat penyewaan sangat rendah, karena sebagian besar orang belum aktif beraktivitas.

    - Grafik ini juga menunjukkan adanya 10 anomali signifikan dalam pola penyewaan sepeda. Salah satunya adalah pada 15 September 2012, di mana terjadi lonjakan penyewaan yang besar, yang berkaitan dengan acara tahunan 'H Street Festival', sebuah festival jalanan besar di Washington, D.C. Sebaliknya, pada 29 Oktober 2012, terjadi penurunan drastis, yang bertepatan dengan datangnya "Hurricane Sandy", badai besar yang memaksa banyak orang membatasi aktivitas luar ruangan. Selain dua peristiwa besar ini, ada beberapa insiden lain yang juga mempengaruhi pola penyewaan sepeda pada tanggal-tanggal tertentu.

    - Selama periode 2011 hingga 2012, grafik penyewaan sepeda menunjukkan tren peningkatan yang konsisten, terutama jika dilihat dari akumulasi bulanan pada grafik tersebut. Namun, ada penurunan signifikan setiap bulan Oktober di kedua tahun tersebut, yang terlihat jelas pada grafik, dan kemungkinan besar disebabkan oleh faktor eksternal seperti cuaca atau acara tertentu.

    - Analisis lebih lanjut dari grafik menunjukkan bahwa suhu memiliki pengaruh besar terhadap jumlah penyewaan sepeda. Suhu yang lebih hangat cenderung meningkatkan jumlah penyewaan. Meskipun kelembaban dan kecepatan angin juga berpengaruh, dampaknya jauh lebih kecil dibandingkan suhu. Grafik scatterplot menunjukkan hubungan antara suhu dan jumlah penyewaan sepeda, dibagi menjadi tiga cluster: cluster 0 (ungu) dengan suhu rendah dan penyewaan sedikit, cluster 1 (hijau) dengan suhu menengah dan variasi penyewaan, dan cluster 2 (kuning) dengan suhu hangat dan penyewaan tertinggi. Semakin tinggi suhu, semakin banyak orang yang menyewa sepeda. Anomali atau outlier yang terlihat pada grafik juga menunjukkan adanya penyewaan yang tidak mengikuti pola umum, kemungkinan besar karena faktor-faktor eksternal seperti acara khusus atau cuaca ekstrem.
    """)