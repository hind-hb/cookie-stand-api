from rest_framework import serializers
from cookie_stands.models import cookie_stands


class cookie_standsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cookie_stands
        fields = "__all__"
