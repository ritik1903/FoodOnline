from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/',views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),

    #category CRUD
    #Add Category
    path('menu-builder/category/add/', views.add_category, name='add_category'),
    #edit Category
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    #delete category
    path('menu-builder/category/delete/<int:pk>/',views.delete_category, name='delete_category',),
    
    #fooditem CRUD
    #Add FoodItem
    path('menu-builder/food/add/',views.add_food, name='add_food'),
    #Edit FoodItem
    path('menu-builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    #delete FoodItem
    path('menu-builder/food/delete/<int:pk>/', views.delete_food, name='delete_food'),
]