from django.urls import path,re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('test/', views.testing, name='home'),
    path('content/', views.content, name='content'),
    path('form/', views.formview, name='formview'),
    # path('author/', views.AuthorList.as_view(), name='authorlist'),
    # path('author/<int:id>/', views.Authorview.as_view(), name='author_view'),
    # re_path(r'^(?P<version>(v1|v2))/authors/$', views.AuthorList.as_view(), name='authorlist'),
    # re_path(r'^(?P<version>(v1|v2))/authors/(?P<pk>[0-9]+)/$', views.Authorview.as_view(), name='author_view'),
    re_path(r'^$', views.AuthorList.as_view(), name='authorlist'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.Authorview.as_view(), name='author_view'),
    path('update/<int:id>/', views.updatebook, name='BookUpdate'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]