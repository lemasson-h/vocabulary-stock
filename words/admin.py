from django.contrib import admin
from .models import User, FrenchGrade, EnglishGrade, Word

class WordAdmin(admin.ModelAdmin):
    exclude = ('french_grade', 'english_grade')
    list_display = ('english_word', 'french_word', 'user')

class WordInline(admin.StackedInline):
    model = Word
    extra = 1
    exclude = ('french_grade', 'english_grade')

class UserAdmin(admin.ModelAdmin):
    inlines = [WordInline]


admin.site.register(FrenchGrade)
admin.site.register(EnglishGrade)
admin.site.register(Word, WordAdmin)
admin.site.register(User, UserAdmin)
# Register your models here.
