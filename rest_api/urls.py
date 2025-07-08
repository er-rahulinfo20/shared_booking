from django.urls import path, include, re_path
from django.contrib import admin
from rest_api.views import MasterClasses, BookingClass

admin.autodiscover()

urlpatterns = [

    # ----------- IN USE -----------------------
    re_path(r'^classes/?$', MasterClasses.as_view()),
    re_path(r'^book/?$', BookingClass.as_view()),
    re_path(r'^bookings/?$', BookingClass.as_view()),


]
