from django.conf.urls import  url
from django.urls import path,include
from .views import leaderboard,question ,question_home,question_details,language_details,detail_list,attempt
import tinymce
urlpatterns = [
                       url(r'^leaderboard/$', leaderboard, name='leaderboard'),
                       url(r'^$', question_home, name='home'),
                       url(r'^(?P<qno>\d+)/$', question, name='question'),
                       url(r'^(?P<qno>\d+)/details/$', question_details, name='question_details'),
                       url(r'^language/(?P<lno>\d+)/details/$', language_details, name='language_details'),
                       url(r'^detail_list/', detail_list, name='detail_list'),
                       url(r'^attempt/(?P<att>\d+)/$', attempt, name='attempt'),    
                       path('tinymce/', include('tinymce.urls')),
]
