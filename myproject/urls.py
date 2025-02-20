"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from  finance import views

urlpatterns = [
    path('admin/', admin.site.urls),
		
    #Auth
	path('signup/', views.signup_user, name='signupuser'),
	path('login/', views.login_user, name='loginuser'),
	path('logout/', views.logout_user, name='logoutuser'),
	
    #Finance
	path('', views.home, name='home'),	
	path('add-transaction/', views.add_transaction, name='add_transaction'),	
	path('current/', views.current_finance, name='current_finance'),
]
 