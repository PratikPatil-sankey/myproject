from django.shortcuts import render
from rest_framework import status
# Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .authentication import KeycloakAuthentication

# class GenerateTokenAPIView(APIView):
#     authentication_classes = [KeycloakAuthentication]

#     def post(self, request):
#         token = request.auth.token
#         return Response({'token': token}, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from keycloak import KeycloakOpenID
class GenerateTokenAPIView(APIView):

    def get(self, request):
        keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/",
                                         client_id="abcde",
                                         realm_name="SankeyProject",
                                         client_secret_key="QEBuXDInVtmd59n95TqAnlK4F8j6fHA4")

        try:
       
            token = keycloak_openid.token(grant_type='client_credentials')
            access_token = token['access_token']
            print("Access Token:", access_token)
        
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error obtaining token:", e)
            return Response({"error": "Failed to obtain access token"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)