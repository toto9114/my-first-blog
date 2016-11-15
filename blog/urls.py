from django.conf.urls import url
# from .views import PostList, PostDetail
from .views import PostViewSet
import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blog', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # url(r'^blog/$', post_list, name='post_list'),
    # url(r'^blog/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
    url(r'^', include(router.urls)),
]

