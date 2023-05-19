from django.urls import path
from core.views import frontpage, shop, signup
from product.views import product
from django.contrib.auth import views



urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),


]