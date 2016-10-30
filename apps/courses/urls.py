from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^add_course$', views.add_course, name='add_course' ),
    url(r'^del_course/(?P<id>\d+)$', views.del_course, name='del_course' ),
    url(r'^del_prompt/(?P<id>\d+)$', views.del_prompt, name='del_prompt' ),
    url(r'^enroll/(?P<id>\d+)$', views.enroll, name='enroll' ),
    # url(r'^show_course/(?P<id>\d+)$', views.show_course, name='show_course' ),
    # url(r'^edit_course/(?P<id>\d+)$', views.edit_course, name='del_course' ),
]
