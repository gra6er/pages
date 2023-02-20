from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]
