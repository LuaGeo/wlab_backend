from django.urls import path
from myapp.views import PredictCancerView, PredictCardiacView, PredictDiabetesView, PredictFoieView, PredictRenalView

urlpatterns = [
    path('predict/cancer/', PredictCancerView.as_view(), name='predict_cancer'),
    path('predict/cardiac/', PredictCardiacView.as_view(), name='predict_cardiac'),
    path('predict/diabetes/', PredictDiabetesView.as_view(), name='predict_diabetes'),
    path('predict/foie/', PredictFoieView.as_view(), name='predict_foie'),
    path('predict/renal/', PredictRenalView.as_view(), name='predict_renal'),
]