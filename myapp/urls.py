from django.urls import path
from myapp.views import PredictView

urlpatterns = [
    path('predict/', PredictView.as_view(), name='predict'),
]