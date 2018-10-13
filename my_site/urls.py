from django.conf.urls import url
from my_site.views import account
from my_site.views import course
urlpatterns = [

    url(r'^auth/$', account.LoginAuth.as_view()),
    url(r'^register/$', account.Register.as_view()),
    url(r'^freecourse/$', course.GetFreeCourseList.as_view()),
    url(r'^seniorcourse/$', course.GetSeniorCourseList.as_view()),
    url(r'^shoppingcar/$', account.Shopping_Car.as_view()),
    url(r'^payment/$', account.Payment.as_view()),
    url(r'^alipay/$', account.Alipay.as_view()),
    url(r'^test/$', account.test),
]
