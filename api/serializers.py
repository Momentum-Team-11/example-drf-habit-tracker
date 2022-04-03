from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from habit_tracker.models import Habit, DailyRecord, User


class HabitListSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = ("pk", "name", "goal", "created_at")


class DailyRecordReadableSerializer(ModelSerializer):
    habit = SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = DailyRecord
        fields = ("pk", "habit", "result", "date")


class DailyRecordWritableSerializer(ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = ("habit", "result")


class DailyRecordForHabitCreateSerializer(ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = ["result"]


class HabitDetailSerializer(ModelSerializer):
    daily_results = DailyRecordReadableSerializer(
        many=True, read_only=True, source="records"
    )

    class Meta:
        model = Habit
        fields = ("name", "goal", "daily_results")
