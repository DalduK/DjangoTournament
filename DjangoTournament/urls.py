"""DjangoTournament URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import tournament.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tournament.views.home, name='home'),
    path('register/', tournament.views.register_page, name='register'),
    path('login/', tournament.views.login_page, name='login'),
    path('logout/', tournament.views.logout_page, name='logout'),
    path('create/', tournament.views.create_tournament, name='create'),
    path('create/<int:id>/', tournament.views.confirm_tournament, name='confirm'),
    path('list/', tournament.views.list_all_tournaments, name='list'),
    path('userlist/', tournament.views.list_user_tournaments, name='userlist'),
    path('bracket/<int:id>/', tournament.views.tournament_bracker, name='bracket'),
    path('editbracket/<int:id>/', tournament.views.edit_tournament_bracker, name='editbracket'),
    path('score/<int:id>/', tournament.views.pair_score, name='score'),
    path('delete/<int:id>/', tournament.views.delete, name='delete'),
]
