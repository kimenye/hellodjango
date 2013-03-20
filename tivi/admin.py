from tivi.models import Show
from django.contrib import admin

class ShowAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

admin.site.register(Show, ShowAdmin)