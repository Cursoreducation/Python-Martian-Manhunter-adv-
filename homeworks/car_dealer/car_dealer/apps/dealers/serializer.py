from rest_framework import serializers

from apps.dealers.models import Dealer, City, Country
from apps.users.serializer import UserSerializer


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['name','code']

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, read_only=True)

    class Meta:
        model = City
        fields = ['name', 'country']


class DealerSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Dealer
        fields = ['id','title','email','city','user']