from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('mealPlan', views.meal_plan, name='meal_plan'),
    path('mealPlan/generate/<int:client_id>', views.generate_mealPlan, name='generate_mealPlan'),

    path('client', views.create_client, name='create_client'),
    path('client/<int:pk>', views.client_handler, name='client_handler'),
]
