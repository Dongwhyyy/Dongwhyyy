from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Word, WordAdmin)
