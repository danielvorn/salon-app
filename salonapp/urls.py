from django.urls import path
from salonapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('salons/', views.SalonList.as_view()),
    path('salons/<int:pk>/', views.SalonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
