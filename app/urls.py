from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.home),
    path("skills/", views.skills, name="skills"),
    path("connect/", views.connect, name="connect"),
    # path("blog/", views.blog, name="blog"),
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
