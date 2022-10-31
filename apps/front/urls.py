from django.urls import path

from apps.front import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/', views.PostView.as_view(), name='post'),
    path('blog-list/', views.BlogListView.as_view(), name='all_blog'),
]
