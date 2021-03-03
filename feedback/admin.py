from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    # model = FeedBack
    list_display = ["id", "name", "text", "answer", "screen", "user", "date", "phone", "email"]
    list_editable = ["answer"]
    list_per_page = 3
    