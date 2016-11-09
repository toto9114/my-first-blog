from django.conf.urls import url
from .views import blog_api
from .views import blog_page

urlpatterns = [
    url(r'^$', blog_api.as_view(), name='post_list'),
]