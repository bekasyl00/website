from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from blog import views
urlpatterns = [
    path('upload', views.upload_document, name='upload'),
    path('documents/', views.document_list, name='documents'),
    path('success', views.success, name='success'),  
    path('pronas',views.pronas,name='pronas'),
    path('', views.shownews.as_view() ,name='home'),
    path('news/add', views.creatnew.as_view(),name='news-add'),
    # path('doc',views.)
    # path('news/add/update', views.creatnew.as_view(),name='news-add'),
    path('news/<int:pk>', views.NewsDetail.as_view() ,name='news-detail'),
    path('news/<int:pk>/update', views.updatview.as_view() ,name='news-update')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

