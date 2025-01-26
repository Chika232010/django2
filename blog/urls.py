from django.urls import path
from .views import alist, feedblog, detail_blog

urlpatterns = [
    path('', alist, name='home'),
    path('form', feedblog, name='form'),
    path('detail/<int:pk>/', detail_blog, name='detail')
]
