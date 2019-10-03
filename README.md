# Information Retrieval with Vector Space Model for News Article

Proyek ini bertujuan untuk membuat sistem temu kembali informasi terhadap artikel berita. Algoritme yang digunakan di dalam proyek ini adalah algoritme Vector Space Model dengan evaluasinya menggunakan Mean Average Precision (MAP), Precision@K, dan R-Precision. Data yang digunakan adalah artikel-artikel berita yang diambil dari situs Kumparan. Terdapat 60 artikel berita dengan 3 kategori (Politik, Teknologi, Travel). Masing-masing kategori berisi 20 artikel berita. Kemudian pada proyek ini juga dibuat dalam 4 skenario, yaitu:
1. Tanpa Stemming - Dengan Stopword: <br>
    Pada skenario ini setiap dokumen tidak dilakukan proses stemming dan stopword yang ada di dalam dokumen tetap digunakan 
2. Tanpa Stemming - Tanpa Stopword: <br>
    Pada skenario ini setiap dokumen tidak dilakukan proses stemming dan stopword yang ada di dalam dokumen tidak digunakan (stopword dihapus)
3. Dengan Stemming - Dengan Stopword: <br>
    Pada skenario ini setiap dokumen dilakukan proses stemming dan stopword yang ada di dalam dokumen tetap digunakan
4. Dengan Stemming - Tanpa Stopword: <br>
    Pada skenario ini setiap dokumen dilakukan proses stemming dan stopword yang ada di dalam dokumen tidak digunakan (stopword dihapus)

Setelah dilakukan pengujian menggunakan evaluasi Mean Average Precision, didapatkan hasil:
1. Skenario 2 – Tanpa Stemming Tanpa Stopword 		=> 0.8028486394557823
2. Skenario 4 – Dengan Stemming Tanpa Stopword 		=> 0.7900198885109599
3. Skenario 1 – Tanpa  Stemming Dengan Stopword 	=> 0.7748469387755103
4. Skenario 3 – Dengan Stemming Dengan Stopword 	=> 0.7668191609977324

Dapat dilihat dari hasil evaluasi tersebut bahwa skenario "tanpa stopword" lebih baik dalam hal presisi dibandingkan dengan skenario "dengan stopword". Hal ini dikarenakan kata-kata yang tidak terlalu penting (stopword) akan dihapus dari corpus yang ada. Apabila penghapusan kata yang ada di daftar stopword tidak dilakukan maka kata tersebut akan dilakukan pembobotan yang mana hampir di setiap dokumen terdapat kata tersebut sehingga akan mempengaruhi hasil cosine similarity, kemudian apabila dilakukan proses information retrieval terdapat banyak dokumen yang tidak relevan di peringkat atas. Sehingga dihapusnya kata yang merupakan stopword bertujuan agar hanya kata-kata penting dan relevan yang dijadikan term di dalam pembobotan. 
Dari hasil evaluasi diatas juga didapatkan bahwa penggunaan stemming tidak terlalu mempengaruhi tingkat presisi. Hal tersebut disebabkan karena terjadinya proses stemming yang tidak sempurna (over-stemming maupun under-stemming).
