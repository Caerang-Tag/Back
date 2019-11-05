from django.urls import path,include
from . import views

urlpatterns = [
	path('Latte/', views.Latte_intro),
	path('Raon/', views.Raon_intro),
	path('Tag/', views.Tag_intro),
	path('Core/', views.Core_intro),
	path('club/', views.club_intro),
]