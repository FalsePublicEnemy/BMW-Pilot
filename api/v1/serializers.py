from rest_framework import serializers
from base.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    @classmethod
    def serialize(cls, instance: '...', many: bool) -> dict:
        return cls(instance, many=many).data
