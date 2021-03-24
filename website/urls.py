from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import login,logout 
from contest.views import login_user
urlpatterns =           [
                       url(r'^', include('contest.urls')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^question/', include(('question.urls','questions'), namespace='question')),
                       url(r'^login/$', login_user, name='login'),
                       
                        ]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
