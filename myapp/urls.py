from django.urls import path
from .views import GenerateTokenAPIView

urlpatterns = [
    path('', GenerateTokenAPIView.as_view(), name='generate_token'),
]
