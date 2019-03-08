from django.contrib import admin

from .models import Experience, Character, CharacterExperiences

class ExperienceInline(admin.TabularInline):
    model = Character.experiences.through
    verbose_name = u'Experience'
    verbose_name_plural = u'Experiences'

class CharacterAdmin(admin.ModelAdmin):
    exclude = ("experiences", )
    inlines = (
        ExperienceInline,
    )

admin.site.register(Experience)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterExperiences)
