from django.conf.urls import url
from Momo import settings
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^login/', views.loginv, name="login"),
    url(r'^logout/', views.logoutv, name="logout"),
    url(r'^$', views.home, name='home'),
    url(r'^display_document', views.display_document, name='display_document'),
    url(r'^model_form_upload/', views.model_form_upload, name='model_form_upload'),
    url(r'^signup/$', views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)