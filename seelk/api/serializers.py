from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

#class AlertSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Alert
#        fields = ['time', 'price']
#class BitcoinSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Bitcoin
#        fields = ['time', 'asset_id_base', 'asset_id_quote', 'rate']
