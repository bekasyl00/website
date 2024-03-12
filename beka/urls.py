from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users import views as usviews
from django.contrib.auth import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('reg/',usviews.register,name='reg'),
    path('user/',views.LoginView.as_view(template_name='users/user.html'),name='user'),
    path('rofil/',usviews.profil ,name='profil'),
    path('exit/',views.LogoutView.as_view(template_name='users/exit.html'),name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)