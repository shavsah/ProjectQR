from django.urls import path
from .views import index, signup, user_data, save_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('user_data/', user_data, name='user_data'),
    path('save_path/', save_path, name='save_path')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
