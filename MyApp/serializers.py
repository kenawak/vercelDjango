from rest_framework import serializers
from .models import College, Departments


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = College
        fields = [
            'id',
            'name',
            'description',
            'image_upload',  # Corrected field name (typo in original code)
            'image_url',
            'location',
            'map_link',
            'stream',
            'gpa',
            'website',
            'Telegram',
            'departments',
        ]

