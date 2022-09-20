HerokuApp Link : https://tugas-3-pbp-jay.herokuapp.com/mywatchlist/

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
  
  - JSON menyimpan elemennya cukup efisien, tetapi kurang rapih secara tampilannya. Sedangkan XML menyimpan elemen-elemennya secara terstruktur, mudah dibaca both oleh 
  manusia dan mesin, tetapi kurang efisien.

  - JSON digunakan untuk mengirim data sedemikian rupa sehingga dapat dianalisis dan dikirim melalui Internet. XML memungkinkan usernya untuk menambahkan catatan.

  - HTML on the other hand, digunakan dalam menyusun bagian paragraf, heading, maupun link pada halaman web melalui serangkaian tags yang tersusun untuk membentuk website 
  tersebut. Keep in mind that HTML bukan termasuk language programming karena tidak capable untuk memberikan fungsi dinamis.
  
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  
  - Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuk dan 
  kegunaannya seperti catatan, susunan heading pada website, dan lainnya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

  - Implementasinya menggunakan suatu booleanField yang apabila bernilai true, html akan show html-code checkmarks (&#10003). Dengan begitu apa yang ada di database 
  hanyalah nilai boolean untuk menandakan suatu telah ditonton atau tidak, sedangkan html berperan untuk show nilai tersebut berdasarkan checks or cross.
  
Postman Screenshots
  # HTML : ![postmanhtml](https://user-images.githubusercontent.com/103520002/191259358-c8d4e4a5-efdb-4c9a-a58d-2c8d5ec5e1dc.png)
  # JSON : ![postmanjson](https://user-images.githubusercontent.com/103520002/191259417-0600266b-63c1-45af-8e2f-60ecb3c70d9f.png)
  # XML  : ![postmanxml](https://user-images.githubusercontent.com/103520002/191259463-f712a372-a8ac-4f0e-b614-cde179603a4c.png)
