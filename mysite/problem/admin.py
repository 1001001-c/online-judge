from django.contrib import admin

# Register your models here.

from .models import ProblemPost

admin.site.register(ProblemPost)

from .models import SubmitPost

admin.site.register(SubmitPost)