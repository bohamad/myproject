#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from main.models import State , StateCapital

State.objects.all().delete()
StateCapital.objects.all().delete()

states= State.objects.all()

dir_path = os.path.dirname(os.path.abspath(__file__)) 
states_csv= os.path.join(dir_path + '/states.csv')
csv_file = open(states_csv,'r')

print csv_file

reader = csv.DictReader(csv_file)

for row in reader:
	new_state, created = State.objects.get_or_create(name=row['state'])
	new_state.abbreviation = row['abbrev']
	new_state.save()

	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])

	new_capital.state = new_state
	new_capital.longitude = row['longitude']
	new_capital.latitude = row['latitude']
	new_capital.population = row['population']

	try:
		new_capital.save()
	except Exception , e :
		print e + new_capital.name



#print  os.path.dirname(os.path.abspath(__file__)) +'/states.csv'
#print '%s/States.csv' %dir_path
#print os.path.join (dir_path, 'states.csv')
