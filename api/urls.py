from django.conf.urls import url
import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contents', views.ContentsViewSet)
router.register(r'folders', views.FoldersViewSet)
router.register(r'favors', views.FavorViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # url(r'^blog/$', post_list, name='post_list'),
    # url(r'^blog/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
    url(r'^', include(router.urls)),
]