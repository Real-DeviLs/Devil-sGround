from django.conf.urls import  url
from .views import home,unauthorized,register
from .views import logout_user
urlpatterns = [
                       url(r'^$', home, name='home'),
                       # url(r'^contest/(?P<pk>\d+)/$', 'manage', name='manage'),
                       url(r'^unauthorized/$', unauthorized, name='403'),
                       url(r'^register/$', register, name='register'),
                       url(r'^logout/$', logout_user, name='logout'),
]
