from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),


    path('', views.home,name="home"),
    # path('customer/', views.customer,name="customer"),
    path('customer/<str:pk>/', views.customer,name="customer"),
    path('products/', views.products,name="products"),
    path('create_order/<str:pk>',views.createOrder,name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),

]  