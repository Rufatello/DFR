from django.contrib import admin
from users.models import User, Lesson, Course

admin.site.register(User)


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('pk', 'title', 'descriptions',)


@admin.register(Course)
class Lesson(admin.ModelAdmin):
    list_display = ('pk', 'title', 'descriptions',)
