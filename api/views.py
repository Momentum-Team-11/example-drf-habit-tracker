import datetime
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from habit_tracker.models import DailyRecord, Habit
from .custom_permissions import IsHabitOwner
from .serializers import (
    DailyRecordForHabitCreateSerializer,
    DailyRecordReadableSerializer,
    DailyRecordWritableSerializer,
    HabitListSerializer,
    HabitDetailSerializer,
)

# Create your views here.
class HabitListView(ListCreateAPIView):
    permission_classes = [IsHabitOwner]
    serializer_class = HabitListSerializer

    def get_queryset(self):
        return self.request.user.habits.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsHabitOwner]
    serializer_class = HabitDetailSerializer

    def get_queryset(self):
        return self.request.user.habits.all()


class DailyRecordCreateView(CreateAPIView):
    permission_classes = [IsHabitOwner]
    serializer_class = DailyRecordForHabitCreateSerializer

    def perform_create(self, serializer):
        habit = get_object_or_404(Habit, pk=self.kwargs["pk"])
        serializer.save(habit=habit, date=datetime.date.today())


class DailyRecordListCreateView(ListCreateAPIView):
    serializer_class = DailyRecordReadableSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            serializer_class = DailyRecordReadableSerializer
        else:
            serializer_class = DailyRecordWritableSerializer
        return serializer_class

    def get_queryset(self):
        month = self.kwargs["month"]
        day = self.kwargs["day"]
        year = self.kwargs["year"]
        date = datetime.date(year, month, day)
        return DailyRecord.objects.filter(habit__user=self.request.user, date=date)

    def perform_create(self, serializer):
        year, month, day = self.kwargs.values()
        date = datetime.date(year, month, day)
        serializer.save(date=date)
