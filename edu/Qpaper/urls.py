from django.urls import path
from . import views

urlpatterns=[
    path('', views.alltourse, name='alltourse'),
    path('user', views.user, name='user'),
    path('Login', views.Login, name='Login'),
    path('index', views.index, name='index'),
    path('logout', views.logout_view, name='logout' ),
    path('about', views.about, name='about'),
    # path('booking', views.booking, name='booking'),
    path('ourtourse', views.ourtourse, name='ourtourse'),
    path('bookingform/<int:id>', views.bookingform, name='bookingform'),
    path('toursview', views.toursview, name='toursview'),
    path('contact', views.contact, name='contact'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('search', views.search, name='search'),
    path('menu', views.user_booking_details, name='menu'),
    path('deals', views.deals, name='deals'),
    path('favoriteplace', views.favoriteplace, name='favoriteplace'),
    path('filtersearch', views.filtersearch, name='filtersearch'),
    path('updatehotel', views.updatehotel, name='updatehotel'),
    
    #path('send_email', views.send_email, name='send_email'),
]