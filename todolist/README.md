HerokuApp Link : 
[Main Menu](https://tugas-2-pbp-jay.herokuapp.com/todolist/) |
[ToDoList Cards](https://tugas-2-pbp-jay.herokuapp.com/todolist/as-cards/) |
[Register](https://tugas-2-pbp-jay.herokuapp.com/todolist/register/) |
[Login](https://tugas-2-pbp-jay.herokuapp.com/todolist/login/) |
[Create New Task](https://tugas-2-pbp-jay.herokuapp.com/todolist/addchores/)

**Kegunaan csrf_token pada elemen form dan apa yang terjadi apabila tidak ada potongan kode tersebut pada tag?**
Django mempunyai tag {% csrf_token %} yang bertujuan untuk men-generate token server side pada saat render halaman web. Token yang bersangkutan lalu di cross-check 
apabila ada request yang datang tetapi tidak memiliki token tersebut, maka request tersebut tidak dijalankan. Jika tidak ada potongan kode tersebut maka akan keluar 
kode status 403 Forbidden yang berarti akses ke sumber tersebut dilarang karena suatu alasan tertentu.

**Is it possible membuat elemen form secara manual, if so how?**
By default, form.as_table ngerender sebagai table cells yang di wrapped dalam tag html berupa tr
Apakah bisa membuat elemen form manually? Yes, tiap atribut pada models.py dapat kita beri lable seperti title, type dan name

> for ex:
```html
<th><input type="hidden" name="id" value="{{chores.id}}"><input type="submit" name="submit" value="Delete"/></th>
```

**Proses alur data dari submisi pada HTML form, penyimpanan pada database, hingga munculnya data user di HTML**
Ketika tombol submit ditekan, sistem mengirim sebuah request ke views.py untuk menyimpan kedalam database. Selanjutnya ada pengecekan apabila form tersebut is_valid() 
dan jika iya, gather cleaned_data dari masing masing atribut pada models by their own param dan save data" tersebut. Next ada views.py yang disini berperan sebagai 
redirector dan render halaman yang akan ditampilkan berupa HTML beserta data yang diinput oleh masing-masing user.

**Pengimplementasian Checklist**
- [x]	Membuat routing seperti todolist/ dan sub pathnya seperti todolist/login di urls.py app “todolist” dan project_django, serta add new installed apps “todolist” di settings.py
  ```python
  urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
  ]
  ```
- [x]	Membuat attributes pada models serta generate + initiate migrations baru
  ```python
  from django.db import models
  from django.contrib.auth.models import User

  class toDoList(models.Model):
      id = models.AutoField(primary_key=True)
      user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
      creation_date = models.DateField(auto_now=True)
      title = models.CharField(max_length=250)
      description = models.CharField(max_length=250)
      is_finished = models.BooleanField(default = False)
  ```
- [x]	Menambahkan fungsi register, login & logout_user, add_chores, mark & delete_chores
  ```python
  def add_chores(request):
    if request.method == "POST":
        form = ChoresForm(request.POST)
        if form.is_valid():
            data = toDoList(
                user = request.user,
                creation_date = datetime.datetime.now(),
                title = form.cleaned_data["name"],
                description = form.cleaned_data["description"]
            )
            data.save()
            return redirect('todolist:show_todolist')
    
    form = ChoresForm()
    context = {'form':form}
    return render(request, 'addchores.html', context)
  ```
- [x]	Membuat .html register, login, todolist, serta addchores
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>New Task / Chores Form</title>
  {% endblock meta %}

  {% block content %}  

  <div class = "addchores">

      <h1>New Task / Chores Form</h1>  

          <form method="POST" >  
              {% csrf_token %}  
              <table>  
                  {{ form.as_table }}  
                  <tr>  
                      <td></td>
                      <td><input type="submit" name="submit" value="Add Task / Chores"/></td>  
                  </tr>  
              </table>  
          </form>

      {% if messages %}  
          <ul>   
              {% for message in messages %}  
                  <li>{{ message }}</li>  
                  {% endfor %}  
          </ul>   
      {% endif %}

  </div>  

  {% endblock content %}
  ```
- [x]	Menambahkan routing baru untuk fungsi & .html diatas, serta redirectionnya
  ```python
  path('addchores/', add_chores, name='addchores'),
  path('markchores/', mark_chores, name='markchores'),
  path('deletechores/', delete_chores, name='deletechores')
  ```
- [x] Push to repo & deploy to Heroku

============================================================================================

**Perbedaan dari Inline, Internal, dan External CSS serta kelebihan dan kekurangan dari masing-masing style**

**Source :** 
[Niagahoster](https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/) | 
[W3schools](https://www.w3schools.com/css/css_selectors.asp)

~ Internal CSS
> adalah kode CSS yang ditulis di dalam tag style dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

> Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

(+) Kelebihan
- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
- Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
- Class dan ID bisa digunakan oleh internal stylesheet.

(-) Kekurangan
- Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
- Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

~ Eksternal CSS
> adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi css, File eksternal CSS biasanya diletakkan setelah bagian head pada halaman.

> Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

(+) Kelebihan
- Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
- Loading website menjadi lebih cepat.
- File CSS dapat digunakan di beberapa halaman website sekaligus.

(-) Kekurangan
- Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan - karena koneksi internet yang lambat.

~ Inline CSS
> adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

> Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.

(+) Kelebihan
- Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

(-) Kekurangan
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
  
**Mentions few tag HTML5**
@header representatif header sebuah doc atau section
@footer representatif footer sebuah doc atau section
@picture container untuk multiple image sources
@track text track dari atau dalam bentuk audio dan atau video
@svg mengallow Scalable Vector Graphics content dalam html doc

**Mentions few CSS selector type**
- Simple selectors (Based on name, id, class)
- Combinator selectors (Based on a specific relationship between them)
- Pseudo-class selectors (Based on a certain state)
- Pseudo-elements selectors (Based on part of an element)
- Attribute selectors (Based on an attribute / value)

**Pengimplementasian Checklist**
- [x]	Add Bootstrap dalam base.html
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js"></script>
  ```
- [x] Initiate juicer.css untuk setiap div classes pada html doc yang dicustomize seperti hal login, register, addchores, todolists, ascards & bonus hover cards
  ```html
  <div class="container-cards">
    {% for chores in todolist %}
    <div class="card p-1">
      <div class="card-body d-flex flex-column justify-content-between gap-2">
        <div class="card-content">
          <h5 class="card-title">{{chores.title}}</h5>
          <p class="card-text">{{chores.description}}</p>
          <p class="card-text fst-italic">{{chores.creation_date}}</p>
          {% if chores.is_finished %}
            <p class="card-text">&#10004</p>
          {% else %}
            <p class="card-text">&#10060</p>
          {% endif %}
        </div>
      </div>
    </div>
    ```
    
    ```css
    .card-text, .card-title {
      color: #ffffff;
    }

    .card-body {
      text-align: center;
      background-color: rgb(50, 50, 50);
      font-family: 'Lobster', cursive;
    }

    .card:hover {
      box-shadow: #000000;
      opacity: 0.8;
      scale: 1.05;
    }
    ```
- [x]	Add bootstrap-responsive.css dalam base.html
  ```html
  <link rel=”stylesheet” href=”css/bootstrap-responsive.css”>
  ```
