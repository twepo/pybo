from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect, reverse, resolve_url


from ..models import Question,Book,Store,Employee,Department

# from util import *


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






from django.db.models import Q, Count



import logging

logger = logging.getLogger('pybo')

print(">>>")
print(__name__)
# pybo는.. 로거명이다.
# 이걸로 logger.debug, logger.error, logger.warning

# 이 로거 객체는.. 이제 이걸로 info,warning,error,debug 메소드를 쓸 수 있다..!
'''
def index(request):

	# logger.info("INFO 레벨로 출력한다!")
	# logger.warning("warning 레벨로 출력한다!")
	# logger.error("error 레벨로 출력한다!")
	# logger.debug("debug 레벨로 출력한다!")
	
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
'''











minusfunc = lambda a,b : a-b


def detail(request, question_id):

	print("hello im detail")
	question = get_object_or_404(Question, pk=question_id)
	context = {"question": question}

	print("--work--")

	# resolve_url은 reverse고.. reverse에서 args=[self.id] 를 간략화한 버전이다!
	# print( resolve_url('pybo:detail', question_id) )
	
	# print( resolve_url(question) )
	# print( redirect(question) )

	# 사실 resolve_url이 필요한건.. 맨 뒤 name이다.!


	return render(request, "pybo/question_detail.html", context)



from django.views.generic import CreateView
from pybo.models import Todo
from django.urls import reverse_lazy
from pybo.forms import TodoForm



from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import QuestionSerializer, TodoSerializer 


@api_view(['GET'])
def apiOverview(request):
	api_urls = {'sucks':'sucks'}
	return Response(api_urls)
	

@api_view(['GET'])
def questionList(request):
	questions = Question.objects.all()
	serializer = QuestionSerializer(questions, many=True)
	return Response(serializer.data)
	
@api_view(['GET'])
def todoList(request):
	todos = Todo.objects.all()
	serializer = TodoSerializer(todos, many=True)
	return Response(serializer.data)



@api_view(['GET'])
def questionDetail(request,pk):
	questions = Question.objects.get(id=pk)
	serializer = QuestionSerializer(questions, many=False)
	return Response(serializer.data)

@api_view(['POST'])
#THIS only allow POST
def questionCreate(request):
	serializer = QuestionSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)




@api_view(['POST'])
def todoCreate(request):
	serializer = TodoSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
	

@api_view(['POST'])
def todoUpdate(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance = todo, data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
	



@api_view(['DELETE'])
def todoDelete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	return Response("your data is fucked! okay!")
	#ah.. Response는 아예 그 template를 만들어줌 











class TodoCreateView(CreateView):
	model = Todo
	# fields = '__all__'
	form_class = TodoForm
	success_url = reverse_lazy('pybo:home')

	# template_name = 'pybo/todo_former.html'
	template_name_suffix = '_create_form'

	def get_context_data(self,**kwargs):
		context = super(TodoCreateView,self).get_context_data(**kwargs)
		
		context['todos'] = Todo.objects.all()

		# 보면 context호출시 모든..todo가 호출되고 있다..!

		return context

	# def form_invalid(self, form):
	# 	print("invalid..stop!")

	def form_valid(self,form):
		print("valid.. proceed")
		return super().form_valid(form)


from django.http import HttpResponse
from django.views import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World! IM GET!')

    def POST(self, request, *args, **kwargs):
        return HttpResponse('Hello, World! IM POST!')











