from django.core import serializers
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection

from util import *

from .models import Campaign
from django.db.models import Q

import json




def index(request):
	print("hello LG indexview")
	return render(request, 'lg/index.html', {})


def campaign_view(request):
	print("hello campgin_view")
	return render(request, 'lg/campaign_view.html', {})










def campaign_list(request):



	#channel = request.POST.getlist('channel[]', "")
	#category = request.POST.getlist('category[]', "")

	#print("lol channel : ")
	#print(channel)

	#print("lol cate! : ")
	#print(category)



	queryset = Campaign.objects.values('title', 'subtitle','channel', 'category',
										'img_path','created_time').order_by('-created_time')


	allowed_filters = ['category[]','channel[]']

	for filter_array_title in allowed_filters:
		filter_title = getArrayName(filter_array_title)

		if len(filter_title):
			print("i can check category HEAD!")
			q_objects = Q()
			for item in request.POST.getlist(filter_array_title):
				print("i can check INNER CATEGORY")

				q_objects |= Q(**{filter_title : item})
				#q_objects.add(Q(category = cat),q_objects.OR)

			queryset = queryset.filter(q_objects)

	#print("QOBJECT : ")
	#print(q_objects)



	#data = json.dumps(list(queryset[:5]), cls=DjangoJSONEncoder)
	data = json.dumps(list(queryset), cls=DjangoJSONEncoder)


	print(data)


	print("length")
	print(queryset.count())

	print("sql :::::::::::::")
	print(connection.queries)




	return HttpResponse(data, content_type="application/json")

















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
