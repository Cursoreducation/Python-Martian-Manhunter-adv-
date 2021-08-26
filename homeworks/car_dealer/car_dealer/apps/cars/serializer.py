from rest_framework import serializers

from apps.cars.models import Car, Model, Brand
from apps.dealers.serializer import DealerSerializer

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['name']

class ModSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = Model
        fields = ['brand','name']


class CarSerializer(serializers.ModelSerializer):
    model = ModSerializer(many=False, read_only=True)
    dealer = DealerSerializer(many=False, read_only=True)

    class Meta:
        model = Car
        fields = ['id','dealer','model','color','slug','price','description','number','engine_power']