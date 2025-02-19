from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('home/', views.home, name='home'),
    path('booking/', views.BookingCreateView.as_view(), name='booking'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),  
]

