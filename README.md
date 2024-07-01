# Deteksi Anomali pada Komentar Reddit Menggunakan Autoencoder

Proyek ini bertujuan untuk mendeteksi anomali pada komentar di platform Reddit menggunakan algoritma Autoencoder, yang merupakan salah satu teknik deep learning. Data yang digunakan adalah komentar yang telah dibersihkan dan direpresentasikan dalam bentuk numerik menggunakan TF-IDF.

## Deskripsi

Deteksi anomali merupakan salah satu topik penting dalam analisis data, terutama dalam konteks data teks yang besar seperti komentar di media sosial. Komentar yang tidak biasa atau anomali dapat memberikan wawasan penting tentang tren atau kejadian tertentu. Algoritma autoencoder digunakan untuk mendeteksi anomali dengan mengukur kesalahan rekonstruksi.

## Algoritma yang Digunakan

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Teknik untuk mengubah teks menjadi representasi numerik.
- **Autoencoder**: Teknik deep learning yang digunakan untuk merekonstruksi data input dan mendeteksi anomali berdasarkan kesalahan rekonstruksi.

## Persyaratan

- Python 3.x
- Library: numpy, pandas, scikit-learn, tensorflow, matplotlib, tabulate

## Cara Penggunaan

### Menggunakan Jupyter Notebook

1. Clone repositori ini.
2. Instal library yang diperlukan dengan menjalankan perintah `pip install -r requirements.txt`.
3. Buka Jupyter Notebook dengan menjalankan perintah `jupyter notebook`.
4. Buka file notebook `.ipynb` yang ada di repositori ini.
5. Jalankan setiap sel di notebook untuk melihat hasilnya.
6. Pastikan file `Reddit_Data.csv` ada di direktori yang sama dengan notebook.

### Menggunakan Google Colab

1. Import notebook `.ipynb` ke Google Colab.
2. Upload file `Reddit_Data.csv` ke Colab.
3. Google Colab biasanya sudah memiliki banyak library yang diperlukan, namun untuk memastikan semua library terinstal, Anda bisa menjalankan perintah `!pip install -r requirements.txt` di sel pertama.
4. Jalankan setiap sel di notebook untuk melihat hasilnya.

### Menggunakan File `.py`

1. Clone repositori ini.
2. Instal library yang diperlukan dengan menjalankan perintah `pip install -r requirements.txt`.
3. Jalankan skrip dengan perintah `python script_name.py` (ganti `script_name.py` dengan nama file `.py` Anda).
4. Pastikan file `Reddit_Data.csv` ada di direktori yang sama dengan skrip.

## Penulis

- [Alip Rizky Firdaus](https://github.com/CallMeARF)

## Lisensi

Repositori ini dilisensikan di bawah MIT License.