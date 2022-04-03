"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path("habits/", views.HabitListView.as_view(), name="api_habit_list"),
    path(
        "habits/<int:pk>",
        views.HabitDetailView.as_view(),
        name="api_habit_detail",
    ),
    path(
        "habits/<int:pk>/results",
        views.DailyRecordCreateView.as_view(),
        name="api_habit_daily_records",
    ),
    path(
        "results/<int:year>/<int:month>/<int:day>",
        views.DailyRecordListCreateView.as_view(),
        name="api_habit_daily_records_by_date",
    ),
    path("api-auth/", include("rest_framework.urls")),
]
