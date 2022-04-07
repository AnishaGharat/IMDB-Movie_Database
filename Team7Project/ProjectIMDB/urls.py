from django.urls import path
from . import views
from .views import redirect_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'ProjectIMDB'
urlpatterns = [
                  path('', views.index, name='Home'),
                  path('about', views.about, name='About Us'),
                  path('?ref_=nv_home', views.index, name='Home'),
                  path('redirect', redirect_view),
                  path('browse-movies', views.movie_index, name='Browse'),
                  path('register', views.sign_up, name='Register'),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path("search/", views.filter_objects.as_view(), name="search"),
                  path('order_movies/', views.order, name="Order-Movie"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
