from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import predict
import pandas as pd

class PredictView(APIView):
    def post(self, request):
        data = request.data
        features = pd.DataFrame([data['features']])
        prediction = predict(features)
        return Response({'prediction': prediction[0]}, status=status.HTTP_200_OK)
