from my_site import models
from rest_framework import serializers


class FreeCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FreeCourse
        fields = "__all__"


class SeniorCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SeniorCourse
        fields = "__all__"

