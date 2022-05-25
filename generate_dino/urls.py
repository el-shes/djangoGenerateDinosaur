from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
    path('dinos/', views.DinosList.as_view(), name='dino_list'),
    path('dinos/dino/<int:pk>', views.DinoDetailView.as_view()),
    path('dinos/dino/<str:letter>', views.DinosFilterList.as_view(), name='letter_list'),

    path('generated/dinos/new', views.DinoCreate.as_view(), name='generated_dino_new'),
    path('generated/dinos/', views.GeneratedDinoList.as_view(), name='generated_dino_list'),

]
