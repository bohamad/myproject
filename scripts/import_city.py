#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from main.models import State , City

City.objects.all().delete()
states = State.objects.all()

dir_path = os.path.dirname(os.path.abspath(__file__)) 
city_csv= os.path.join(dir_path + '/zip_code_states.csv')
csv_file = open(city_csv, 'r')

#print csv_file

reader = csv.DictReader(csv_file)

for row in reader:

	try:
		state , created = State.objects.get_or_create(abbreviation = row['state'])
	
	except Exception , e :
		print  e
		print state.name


	new_city, created = City.objects.get_or_create(name = row['city'])
	new_city.zip_code =row['zip_code']
	new_city.longitude = row['longitude']
	new_city.latitude = row['latitude']
	new_city.country = row['county']
	new_city.state = state

	try:
		new_city.save()
	except Exception, e :
		print e
		print  new_city.name
	#new_city, created = City.objects.get_or_create(name = row['city'], state = state_.abbreviation)

	#new_city.zip_code =row['zip_code']
	#new_city.longitude = row['longitude']
	#new_city.latitude = row['latitude']
	#new_city.country = row['county']
	#new_city.state = state



