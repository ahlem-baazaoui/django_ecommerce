from django.urls import path
from . import views 
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('ecommerceapp/<int:memberid>/',views.membreviews, name='ecommerceapp')
]