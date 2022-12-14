# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist, show_todolist_ascards, register, login_user, logout_user, add_chores, mark_chores, delete_chores, show_json, show_todolist_ajax, post_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addchores/', add_chores, name='addchores'),
    path('markchores/', mark_chores, name='markchores'),
    path('deletechores/', delete_chores, name='deletechores'),
    path('as-cards/', show_todolist_ascards, name='ascards'),
    path('json/', show_json, name="asjson"),
    path('ajax/', show_todolist_ajax, name="getajax"),
    path('ajax-post/', post_todolist_ajax, name="postajax")
]