HerokuApp Link : https://tugas-2-pbp-jay.herokuapp.com/katalog/items

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 
- urls.py, views.py, models.py, dan berkas html;
![Tugas2-PBP-Bagan_FarrasHafizhudinIndraWijaya_2106652682_B](https://user-images.githubusercontent.com/103520002/190291908-9b0c9fa5-66b0-457d-9106-f7c5775a5015.png)

- Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Sebelumnya, Virtual Environment adalah sebuah wadah untuk menampung modul dalam suatu project pekerjaan yang bertujuan untuk mengisolasi project tersebut. Kegunaannya 
semisal kita mengembangkan suatu aplikasi, kita dapat menggunakan modul dengan versi yang berbeda dengan mengisolate kedua (atau lebih) environment tersebut sesuai dengan 
versi berapa yang digunakan atau dibutuhkan. Kita tetap dapat membuat aplikasi tanpa menggunakan Virtual Environment, tetapi disaat pengembangan sebuah aplikasi tersebut, 
maka semua modul atau package yang digunakan atau dibutuhkan akan selalu ikut diperbaharui.

- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Pada views.py, import models yang ada ditujukan untuk pengambilan data dari database. Selanjutnya ada pemanggilan fungsi query ke model database dan menyimpan hasil 
Squery tersebut ke dalam sebuah variable yang dimana akan dirender oleh Django. Data tersebut akan di mapping untuk dapat memunculkannya di halaman HTML.
