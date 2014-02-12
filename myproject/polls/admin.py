from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]
	fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})]

admin.site.register(Poll, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
