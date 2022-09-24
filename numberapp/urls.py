from django.urls import path
from.import views
urlpatterns = [
    path('',views.fun,name='fun'),
    path('add',views.addition,name='add'),
    path('index',views.indexfun,name='index'),
    ]
