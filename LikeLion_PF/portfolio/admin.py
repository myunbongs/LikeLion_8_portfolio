from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','title','author', 'updated']
    raw_id_fields = ['author']

admin.site.register(Portfolio, PortfolioAdmin)
