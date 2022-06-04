from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
    path('dinos/', views.DinosList.as_view(), name='dino_list'),
    path('dinos/dino/<int:pk>', views.DinoDetailView.as_view()),
    path('dinos/dino/<str:letter>', views.DinosFilterList.as_view(), name='letter_list'),

    path('generate/dinos/form/<str:dino_name>', views.DinoCreateView.as_view(), name='view_generate'),
    path('generate/dinos/new', views.DinoCreate.as_view(), name='generated_dino_new'),
    path('generate/dinos/save/<str:dino_name>', views.DinoSave.as_view(), name='generated_dino_save'),
    path('generate/dinos/all', views.GeneratedDinoList.as_view(), name='generated_dino_list'),

]
