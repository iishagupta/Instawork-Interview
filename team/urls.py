from django.urls import path
from .views import * 

urlpatterns = [
	path("", TeamView.as_view()),
	path("<int:member_id>/", TeamView.as_view()),
] 