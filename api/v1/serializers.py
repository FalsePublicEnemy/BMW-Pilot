from rest_framework import serializers
from base.models import Vehicle
from base.models import Test


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    @classmethod
    def serialize(cls, instance: '...', many: bool) -> dict:
        return cls(instance, many=many).data


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
