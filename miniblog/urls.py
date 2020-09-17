"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login' ),
    path('home/', views.home, name='home' ),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('signup/', views.user_signup, name='signup' ),
    path('logout/', views.user_logout, name='logout' ),
    path('addpost/', views.add_post, name='addpost' ),
    path('updatepost/<int:id>/', views.update_post, name='updatepost' ),
    path('deletepost/<int:id>/', views.delete_post, name='deletepost' ),
    path('value/<int:my_id>/<int:rvolt>/<int:rcurrent>/<int:yvolt>/<int:ycurrent>/<int:bvolt>/<int:bcurrent>/<int:battery>/', views.sign_up1, name='value'),
    
    path('showdata/', views.showdata, name='showdata'),
    path('ron_data/<int:my_id>/<str:my_value>/', views.ron_data, name='ron_data'),
    path('roff_data/<int:my_id>/<str:my_value>/', views.roff_data, name='roff_data'),
    path('yon_data/<int:my_id>/<str:my_value>/', views.yon_data, name='yon_data'),
    path('yoff_data/<int:my_id>/<str:my_value>/', views.yoff_data, name='yoff_data'),
    path('bon_data/<int:my_id>/<str:my_value>/', views.bon_data, name='bon_data'),
    path('boff_data/<int:my_id>/<str:my_value>/', views.boff_data, name='boff_data'),
    path('showdataindividual/<int:my_id>/', views.showdataindividual_data, name='showdataindividual'),
]
