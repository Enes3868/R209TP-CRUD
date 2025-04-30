from django . urls import path
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('/affiche/<int:id>/',views.read),
    path('VUE_Affiche_all/', views.VUE_Affiche_all),
    path('/update/<int:id>/',views.update),
]