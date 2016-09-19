#   meetings/admin.py
#   Patrick W. Montgomery
#   created: 9/19/2016

#   import statements
from django.contrib import admin
from .models import Minutes


admin.site.register(Minutes)