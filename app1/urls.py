from django.urls import path
from . views import *
urlpatterns = [
    path('',home,name = 'home'),  #blank inside ' ' : landing page
    path('delete/<int:id>',delete_todo,name='deleteabc'),

]