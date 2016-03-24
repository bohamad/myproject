from django.contrib import admin
from main.models import State , StateCapital , City

# Register your models here.

class StateAdmin(admin.ModelAdmin):
	list_display = ('name','abbreviation')
	search_field=('name')

class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name','state')
	search_field=('name')



admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(City)