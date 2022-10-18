from django.urls import path
from .views import (Doador_Create, Doador_Update,
    Doador_Delete, Doador_List)

urlpatterns = [
    path('', Doador_Create.as_view()),
    path('update/<int:pk>', Doador_Update.as_view()),
    path('delete/<int:pk>', Doador_Delete.as_view()),
    path('list/', Doador_List.as_view()),
]