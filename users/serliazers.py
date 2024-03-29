from rest_framework import serializers

from users.models import Course,Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'descriptions',)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

