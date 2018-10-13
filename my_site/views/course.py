from rest_framework.views import APIView
from rest_framework.response import Response
from my_site import models
from my_site.serializers.course_serializer import FreeCourseSerializer, SeniorCourseSerializer
from utils.auth import Auth
from django_redis import get_redis_connection


class GetFreeCourseList(APIView):

    def get(self,request,*args,**kwargs):
        ret = {"code":1000}
        queryset = models.FreeCourse.objects.all()
        ser = FreeCourseSerializer(instance=queryset,many=True)
        ret["data"] = ser.data
        # print(ret)
        return Response(ret)


class GetSeniorCourseList(APIView):
    authentication_classes = [Auth, ]

    def get(self,request,*args,**kwargs):

        ret = {"code":1000}
        queryset = models.SeniorCourse.objects.all()
        ser = SeniorCourseSerializer(instance=queryset,many=True)
        ret["data"] = ser.data
        # print(ret)
        return Response(ret)

