from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^filecarver/get_form/$', views.get_filecarver_config_form, name='chopshop_service-views-get_filecarver_config_form'),
    url(r'^filecarver/(?P<pcap_md5>.+?)/$', views.run_filecarver, name='chopshop_service-views-run_filecarver'),
]
