from django.shortcuts import render , render_to_response , redirect 
from main.models import State , City
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from main.form import CitySearchForm , CreateCityForm ,CityEditForm


@login_required
def city_delete(request,pk):
	City.objects.get(pk=pk).delete()
	
	return redirect('/city_search/') 


@login_required
def city_edit(request, pk):

	request_context = RequestContext(request)
	context = {}

	city =City.objects.get(pk=pk)

	context['city']= city
	form = CityEditForm(request.POST or None , instance=city)
	context['form'] =form

	if form.is_valid():
		form.save()
		return redirect('/city_search/')

	return render_to_response ('city_edit.html', context, context_instance = request_context)






def city_create(request):
	request_context = RequestContext(request)
	context = {}

	city = City.objects.get(pk=pk)
	form = CityEditForm(request.POST or None , instance = city)
	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/state_search')
	return render_to_response ('city_edit.html', context, context_instance = request_context)


	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			return render_to_response('city_create.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form
		return render_to_response('city_create.html', context, context_instance=request_context)




def city_search(request):
	request_context = RequestContext(request)

	context = {}
	if request.method =='POST' :
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']
			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			return render_to_response('city_search.html',context, context_instance = request_context)

		else:
			context['valid'] = form.errors
			return render_to_response('city_search.html',context, context_instance = request_context)

	else:
		form= CitySearchForm()
		context['form'] =form
		return render_to_response('city_search.html', context, context_instance = request_context )




def state_list (request):
	context = {}
	states = State.objects.all()
	context['states'] = states
	return  render(request, 'state_list.html', context)


class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_object_name = 'states'


def state_detail(request, pk):
	context = {}
	states = state.objects.get(pk=pk)
	context['state'] = state
	return  render(request, 'state_detail.html', context)



class StateDetailView(DetailView):
	model = State
	Template_name = 'state_detail.html'
	context_object_name = 'states'


# def state_detail (request, name):

# 	state = State.objects.get(name=name)
# 	cities = state.city_set.all()
# 	text_string = '<h3> %s </h3>' % state.name

# 	for city in cities:
# 		try:
# 			text_string += '%s </br>' % city.name
# 		except Exception , e:
# 			print e

# 	return HttpResponse(text_string)


# def state_list (request):
# 	states = State.objects.all()
# 	state_list=[]

	
# 	for state in states:
# 		try:
# 			state_list.append("<a href= '/state_detail/%s'> %s -- %s </a> <br>" % ( state.name, state.name, state.statecapital.name))
# 		except Exception , e:
# 			print e

# 	return HttpResponse(state_list)

 
# # COPY FROM SALCK

# @csrf_exempt
# def get_search(request):

# 	get_var = request.GET.get('q', None)
# 	print request.GET
# 	print request.POST

# 	text_string = ''

# 	text_string += 'Search Term: %s <br>' % get_var

# 	text_string += """
# 	<form action="/get_search/" method="GET">

# 	Search Cities:
# 	<input type='text' name='q'>
# 	<br>

# 	<input type='submit' value="Submit">

# 	</form>

# 	""" 

# 	if get_var != None:
# 		cities =  City.objects.filter(name__icontains=get_var)
# 		for city in cities:
# 			text_string += '%s <br>' % city.name

# 	return HttpResponse(text_string)



# @csrf_exempt
# def get_post(request):

# 	get_var = request.GET.get('q', None)

# 	post_var = request.POST.get('q', None)

# 	print request.GET
# 	print request.POST

# 	text_string = ''

# 	text_string += 'Get Var: %s <br>' % get_var
# 	text_string += 'Post Var: %s <br>' % post_var

# 	text_string += """
# 	<form action="/get_post/" method="POST">

# 	Enter Var:
# 	<input type='text' name='q'>
# 	<br>

# 	<input type='submit' value="Submit">

# 	</form>

# 	""" 

# 	return HttpResponse(text_string)