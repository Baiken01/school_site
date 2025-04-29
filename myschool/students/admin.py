from django.contrib import admin
from .models import Gallery



admin.site.register(Gallery)

from .models import Project

admin.site.register(Project)
