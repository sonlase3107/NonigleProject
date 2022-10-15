from django.urls import path

from apps.emails.views import  renderCar, UnityAPIView
from apps.emails import views

urlpatterns = [
    path('unity', UnityAPIView.as_view()),
    path('render', views.renderCar, name='render')
]
