from django.urls import path, re_path
from .views import *


urlpatterns = [ #пути url, идут во views.py
    path('', Home.as_view(), name='home'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('buyprog/', BuyProg.as_view(), name='buyprog'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
]


