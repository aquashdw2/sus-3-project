from django.contrib import admin

from survey import models


admin.site.register(models.SurveySimple)
admin.site.register(models.SurveyChoices)
