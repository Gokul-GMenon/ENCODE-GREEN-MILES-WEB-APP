from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer
from .models import DataField

class DataFieldSerializer(ModelSerializer):
    class Meta:
        model = DataField
        fields = '__all__'