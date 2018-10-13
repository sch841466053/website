from django.contrib import admin
from my_site import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.UserToken)
admin.site.register(models.FreeCourse)
admin.site.register(models.SeniorCourse)