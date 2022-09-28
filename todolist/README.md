HerokuApp Link : 
[Main Menu](https://tugas-2-pbp-jay.herokuapp.com/todolist/) |
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
