from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from cybersecurity.tema3.api.views import day_list, day_list_pet, positive_pet, negative_pet, neutral_pet,\
    hashtag_pet, positive_pet_all, negative_pet_all, neutral_pet_all, hashtag_pet_all

app_name = "tema3"
urlpatterns = [
    path("", login_required(TemplateView.as_view(template_name='pages/Firebase.html')), name="tema3"),
    path('day/', login_required(day_list), name="day_pet"),
    path('day/<str:pk>', login_required(day_list_pet), name="best_day_pet"),
    path('positive/', login_required(positive_pet_all), name="pos_pet"),
    path('positive/<str:pk>', login_required(positive_pet), name="best_pos_pet"),
    path('negative/', login_required(negative_pet_all), name="neg_pet"),
    path('negative/<str:pk>', login_required(negative_pet), name="best_neg_pet"),
    path('neutral/', login_required(neutral_pet_all), name="neu_pet"),
    path('neutral/<str:pk>', login_required(neutral_pet), name="best_neu_pet"),
    path('hashtags/', login_required(hashtag_pet_all), name="hashtag_pet"),
    path('hashtags/<str:pk>', login_required(hashtag_pet), name="best_hashtag_pet"),
]
