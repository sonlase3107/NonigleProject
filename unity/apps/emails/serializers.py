from rest_framework import serializers

from apps.emails.models import  Unity


class UnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unity
        fields = '__all__'
