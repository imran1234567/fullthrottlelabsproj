from rest_framework import serializers

from projectapp.models import Search


class SearchModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = [
            'name',
            'custom_number'
        ]