from django.contrib import admin

from pulse_survey.survey.models import Feedback, Result

admin.site.register(Result)
admin.site.register(Feedback)
