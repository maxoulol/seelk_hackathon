from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bitcoin.models import Bitcoin
from bitcoin.serializers import BitcoinSerializer
import requests

@api_view(['GET'])
def get_bitcoin_value(request):
    if request.method == 'GET':
        url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
        headers = {'X-CoinAPI-Key' : 'C6E7CFDC-C09A-4C24-B33F-AF3A1AD6AA01'}
        response = requests.get(url, headers=headers)

        bitcoin = response.json()
        #print("response ")
        #print(bitcoin)
        #serializer = BitcoinSerializer(bitcoin, many = True)
        #bitcoin = requests.request('GET', 'https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=C6E7CFDC-C09A-4C24-B33F-AF3A1AD6AA01')
        #serializer = BitcoinSerializer(bitcoin, many = True)
        #return Response(serializer.data)
        return Response(bitcoin)
