from django.conf.urls import url
from .views import apis, user_apis

urlpatterns = [
    url(r'^api/get/course/code$', apis.get_courses_by_code),
]
