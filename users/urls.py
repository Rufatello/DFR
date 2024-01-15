from django.urls import path

from users.apps import UsersConfig
from users.views import CourseViewSet, LessonCreateApiView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView
from rest_framework.routers import DefaultRouter
app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'users', CourseViewSet, basename='user')

urlpatterns = [
    path('lessons/create/', LessonCreateApiView.as_view(), name='lesson-create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls