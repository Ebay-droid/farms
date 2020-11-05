from django.urls import path
from . import views

urlpatterns = [
    
    path('farms/',views.Farms.as_view()),
    path('farms/<farm_id>/',views.FarmDetail.as_view()),
    path('farms/<farm_id>/animals',views.Animal.as_view()),
    path('farms/<farm_id>/animals/<animal_id>',views.AnimalDetail.as_view()),

]
