from django.core import serializers
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection

from util import *

from .models import Campaign,Category,Channel
from django.db.models import Q

import json




def index(request):
	pr("hello LG indexview")
	return render(request, 'lg/index.html', {})


def campaign_view(request):
	pr("hello campgin_view")
	return render(request, 'lg/campaign_view.html', {})




#DEBUG
def index2(request):
	pr("hello LG indexview22")
	return render(request, 'lg/index2.html', {})






def campaign_list(request):

	channel = request.GET.get('channel', "")
	category = request.GET.get('category', "")
	pr("lol channel : ")
	pr(channel)
	pr("lol cate! : ")
	pr(category)


	queryset = Campaign.objects.values('title', 'subtitle','channel', 'category',
										'img_path','created_time').order_by('-created_time')


	allowed_filters = ['category[]','channel[]']

	for filter_array_title in allowed_filters:

		filter_title = getArrayName(filter_array_title)

		pr("filter_title")
		pr(filter_title)

		if len(filter_title):

			#pr("i can check category HEAD!")
			q_objects = Q()
			for item in request.GET.getlist(filter_array_title):
				#pr("i can check INNER CATEGORY")

				q_objects |= Q(**{filter_title : item})
				#q_objects.add(Q(category = cat),q_objects.OR)

			queryset = queryset.filter(q_objects)

	#pr("QOBJECT : ")
	#pr(q_objects)


	data = json.dumps(list(queryset[:5]), cls=DjangoJSONEncoder)
	#data = json.dumps(list(queryset), cls=DjangoJSONEncoder)


	pr(data)

	pr("length")
	pr(queryset.count())

	pr("sql :::::::::::::")
	pr(connection.queries)


	#return JsonResponse(data, safe=False)
	return HttpResponse(data, content_type="application/json")










from django.views.generic.list import ListView
from django.views import generic
from django.core import serializers
from django import http


class AJAXListMixin(object):

		#def dispatch(self, request, *args, **kwargs):
			#if not request.is_ajax():
				# raise http.Http404("hello-AJAX ONLY VIEW")
			#return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)

		def get_queryset(self):
			return (
				super(AJAXListMixin, self)
				#.get_queryset().filter(eng_name='living')
				.get_queryset().all()
			)


		def get(self, request, *args, **kwargs):
			pr("request : ", self.get_queryset())
			pr("kwargs2", kwargs)
			return http.HttpResponse(serializers.serialize('json', self.get_queryset()))




class get_list(AJAXListMixin, generic.ListView):
	model = Category














'''
def get_list(request,type):
	#pr("getlist works")
	#pr(Category)
	queryset = Category.objects.all()
	pr(queryset)
	data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
	return HttpResponse( data, content_type="application/json")
'''









































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













