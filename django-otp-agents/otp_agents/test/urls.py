from django.conf.urls import url
import django.contrib.auth.views

import django_otp.views
import otp_agents.views

from . import views


urlpatterns = [
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^verify/$', django_otp.views.login),
    url(r'^trust/$', otp_agents.views.login),
    url(r'^logout/$', django.contrib.auth.views.logout),

    url(r'^otp/$', views.otp_view),
    url(r'^otp2/$', views.otp_view_2),
    url(r'^pickle/$', views.pickle_view),
    url(r'^otp_advised/$', views.otp_advised_view),
    url(r'^otp_advised_2/$', views.otp_advised_view_2),
    url(r'^agent/$', views.agent_view),
]
