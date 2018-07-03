from django.urls import path

from . import views

app_name = 'cake'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:recipe_id>/',views.detail, name='detail'),
    path('<int:recipe_id>/ingredients/', views.ingredients, name='ingredients'),
    path('<int:recipe_id>/rate/', views.rate, name='rate'),

]
