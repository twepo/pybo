from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

from util import *


# def index(request):

# 	print("LIST WORKS")

# 	print("okay helloworld")
# 	print(Question.objects.filter(subject__contains="sO"))

# 	page = request.GET.get('page','1')
# 	question_list = Question.objects.order_by('-create_date')
# 	paginator = Paginator(question_list,20)
# 	page_obj = paginator.get_page(page)
# 	context = {'question_list':page_obj}

# 	return render(request,'pybo/question_list.html',context)





# IT IS EDITED VERSION



from django.db.models import Q, Count



def index(request):
	
	page = request.GET.get('page',1)
	kw = request.GET.get('kw','')
	so = request.GET.get('so','recent')

	if so == "recommend":
		question_list = Question.objects.annotate(
			r_count = Count('voter'),
			cr_count = Count('voter'),
		).order_by('-r_count','-create_date').distinct()


	elif so == "question":
		question_list = Question.objects.annotate(
			q_count = Count('answer')
		).order_by('-q_count','-create_date').distict()
	else:
		question_list = Question.objects.order_by('-create_date')

	print( Question.objects.values() )	

	if kw:
		question_list = question_list.filter(
			Q(subject__icontains = kw) |
			Q(content__icontains = kw) |
			Q(author__username__icontains = kw) |
			Q(answer__author__username__icontains = kw)
		)


	paginator = Paginator(question_list,15)
	page_obj = paginator.get_page(page)


	context = {'question_list':page_obj, 'page':page,'kw':kw,'so':so}
	return render(request,'pybo/question_list.html',context)


























































































minusfunc = lambda a,b : a-b


def detail(request, question_id):


	# print(Question.objects.all())
	# print("--------------------")
	# print(Question.objects.filter(id=25))
	# print("--------------------")
	# print(Question.objects.filter(subject__contains="my"))
	# print("--------------------")
	# print(Question.objects.get(id=25))
	# print("--------------------")
	# print(get_object_or_404(Question,pk=25))


	
	question = get_object_or_404(Question, pk=question_id)
	context = {"question": question}
	return render(request, "pybo/question_detail.html", context)



