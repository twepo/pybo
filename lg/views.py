from django.core import serializers
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.core.paginator import Paginator,EmptyPage

from util import *

from .models import Campaign,Category,Channel
from django.db.models import Q

import json






def index(request):

	category_list = Category.objects.all()
	channel_list = Channel.objects.all()

	context = {"category_list": category_list,"channel_list": channel_list }

	return render(request, 'lg/index.html', context )




#DEBUG2
def index2(request):
	p("INDEX2")
	return render(request, 'lg/index2.html', {})


#DEBUG3
def index3(request):
	p("INDEX3")
	return render(request, 'lg/index3.html', {})













# @query_debugger
def campaign_list(request):



	queryset = Campaign.objects.values('id','title', 'subtitle','channel__eng_name', 'category__eng_name','img_path','created_time').order_by('-created_time')



	allowed_filters = ['category[]','channel[]']
	for filter_array_title in allowed_filters:
		filter_title = getArrayName(filter_array_title)
		# p("1-filter_title",filter_title)
		if len(filter_title):
			# p("2-i can check FILTER HEAD!(master)")
			q_objects = Q()
			for item in request.GET.getlist(filter_array_title):
				# p("3-i can check COMMING CATEGORYorCHANNEL")
				q_objects |= Q(**{filter_title+"__eng_name" : item})
				#q_objects.add(Q(category = cat),q_objects.OR)

			queryset = queryset.filter(q_objects)
	# p("4-QOBJECT : ",q_objects)


	search = request.GET.get('search','').split(' ')
	search_array = list(filter(None, search))
	# p("search_array : ", search_array)

	if len(search_array):
		q_objects = Q()
		for item in search_array:
			# p("for works--")
			q_objects &= Q(**{"title__icontains" : item})
		queryset = queryset.filter(q_objects)


	# p("QUERYSET : ",queryset)


	page = request.GET.get('page', '1')
	p("page : ", page)

	paginator = Paginator(queryset, 50)  # 페이지당 카운트
	last_page = paginator.num_pages
	try:
		page_obj = paginator.page(page)
	except EmptyPage:
		page_obj = ""

	p("last_page : ", last_page)





	# p("page_obj+list : ", list(page_obj) )

	json_set = {'data': list(page_obj) , 'last_page':last_page}
	data_set = json.dumps( json_set, cls=DjangoJSONEncoder )


	# p("DATA_SET : ", data_set)
	# p("length",queryset.count())
	p("sql :: ",connection.queries)


	return HttpResponse(data_set, content_type="application/json")















# @query_debugger
def campaign_list2(request):


	queryset = Campaign.objects.values('id','title', 'subtitle','channel__eng_name', 'category__eng_name','img_path','created_time').order_by('-created_time')


	allowed_filters = ['category[]','channel[]']
	for filter_array_title in allowed_filters:
		filter_title = getArrayName(filter_array_title)
		# p("filter_title",filter_title)
		if len(filter_title):
			# p("i can check FILTER HEAD!(master)")
			q_objects = Q()
			for item in request.GET.getlist(filter_array_title):
				# p("i can check COMMING CATEGORYorCHANNEL")
				q_objects |= Q(**{filter_title+"__eng_name" : item})
				#q_objects.add(Q(category = cat),q_objects.OR)

			queryset = queryset.filter(q_objects)



	#p("QOBJECT : ",q_objects)


	#data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
	data = json.dumps(list(queryset[:25]), cls=DjangoJSONEncoder)

	# p(data)
	# p("length",queryset.count())

	# p("sql :::::::::::::")
	# p(connection.queries)

	#return JsonResponse(data, safe=False)
	return HttpResponse(data, content_type="application/json")















def campaign_view(request):
	p("hello campgin_view")
	return render(request, 'lg/campaign_view.html', {})













from django import http
from django.http import Http404
from django.apps import apps
from django.shortcuts import get_list_or_404,get_object_or_404





from django.core.exceptions import ObjectDoesNotExist












def select_list(request,type):

	allowed_filters = ['category','channel']

	if type in allowed_filters:

		Model = apps.get_model('lg', type)
		queryset = Model.objects.all()
		data = serializers.serialize('json', queryset)

		return HttpResponse( data, content_type="application/json")

	else:
		raise Http404("잘못된 접근입니다")





























































from lg.models import Todo

class HomeView(TemplateView):
	template_name = 'lg/home.html'


class ApiTodoLV(ListView):
	model = Todo

	# def get(self,request,*args,**kwargs):
	#     tmpList=[
	# 			{'id': 1,'name': 'DJ김석훈', 'todo': 'Django 와 Vue.js 연동 프로그램을 만들고 있습니다.'},
	# 			{'id': 2,'name': 'DJ홍길동', 'todo': '이름을 안쓰면 홍길동으로 나와요...'},
	# 			{'id': 3,'name': 'DJ이순신', 'todo': '신에게는 아직 열두 척의 배가 있사옵니다.'},
	# 			{'id': 4,'name': 'DJ성춘향', 'todo': '그네 타기'},
	# 	]
	#	return JsonResponse(data=tmpList, safe=False)

	def render_to_response(self, context, **response_kwargs):
		todoList = list(context['object_list'].values())
		return JsonResponse(data=todoList, safe=False)













