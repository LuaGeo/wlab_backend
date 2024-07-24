from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import predict_cancer, predict_cardiac, predict_diabetes, predict_foie, predict_renal
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class PredictCancerView(APIView):
    def post(self, request):
        data = request.data
        logger.debug(f"Reçu des données pour cancer: {data}")
        features = pd.DataFrame([data['features']])
        prediction = predict_cancer(features)
        return Response({'prediction': prediction}, status=status.HTTP_200_OK)

class PredictCardiacView(APIView):
    def post(self, request):
        data = request.data
        logger.debug(f"Reçu des données pour cardiac: {data}")
        features = pd.DataFrame([data['features']])
        prediction = predict_cardiac(features)
        return Response({'prediction': prediction}, status=status.HTTP_200_OK)
    
class PredictDiabetesView(APIView):
    def post(self, request):
        data = request.data
        logger.debug(f"Reçu des données pour diabètes: {data}")
        features = pd.DataFrame([data['features']])
        prediction = predict_diabetes(features)
        return Response({'prediction': prediction}, status=status.HTTP_200_OK)
    
class PredictFoieView(APIView):
    def post(self, request):
        try:
            data = request.data
            logger.debug(f"Reçu des données pour maladie du foie: {data}")
            features = pd.DataFrame([data['features']])
            logger.debug(f"Features dataframe: {features}")
            prediction = predict_foie(features)
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Erreur lors de la prédiction de la maladie du foie : {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PredictRenalView(APIView):
    def post(self, request):
        try:
            data = request.data
            logger.debug(f"Reçu des données pour maladie des reins: {data}")
            features = pd.DataFrame([data['features']])
            logger.debug(f"Features dataframe: {features}")
            prediction = predict_renal(features)
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Erreur lors de la prédiction de la maladie des reins : {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)