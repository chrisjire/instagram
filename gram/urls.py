from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PostCreateView


urlpatterns=[
    url('^$', views.welcome, name = 'welcome'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^profile/edit/$',views.edit, name='edit'),
    # url(r'^new/post/$', views.new_post, name = 'new-post'),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='aboutuser'),
    url(r'^search/',views.search_results, name='search_results'),
    # url(r'^user/(?P<user_id>\d+)$', views.user, name='user'),
    # url(r'^search/', views.search_results, name='search_results')
    url(r'^new/post/$', PostCreateView.as_view(), name = 'new-post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)