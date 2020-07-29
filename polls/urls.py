from django.urls import path

from .views import HomePageView, AboutPageView

# Since here we are using views at class level therefore we have to use as_view() after class name in the url

urlpatterns = [

    path('about/', AboutPageView.as_view(), name="about"),
    path('', HomePageView.as_view(), name="home"),
]
