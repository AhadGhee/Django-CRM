
from django.urls import path
from . import views

#Anytime you in Django you want to create a new homepage (About, contact, etc.), It is a three step process
#1. create actual template file
#2. Create the html page
#3. Create a URL 
#4. Create a view

#View - A view in Django is just a Python function (or class) that receives a request and returns a response.
#Template File - A template is just an HTML file stored in your project’s templates/ folder.
#Template = HTML file, View = Python code to load it, URL = web address to reach it.


urlpatterns = [
    path('', views.home, name='home'),
   # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),  
    # it is called login_user bc login is a function we imported
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    
]
