from django.urls import path,include
from .views import Places

urlpatterns = [
    path('', Places.as_view(),name="api"),
	path('<int:id>/', Places.as_view()),
]
