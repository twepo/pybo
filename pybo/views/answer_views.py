
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer

from util import *



@login_required(login_url="common:login")

def answer_create(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():


			# question.answer_set.create(
			# 	content = request.POST.get('content'),
			# 	create_date = timezone.now(),
			# 	author = request.user
			# )

			answer = form.save(commit=False)
			answer.author = request.user
			answer.create_date = timezone.now()
			answer.question = question
			answer.save()

			return redirect("{}#answer_{}".format(
				resolve_url('pybo:detail',question_id=question.id),
				answer.id
			))



	else:
		form = AnswerForm()
		context = {'form':form}
	return render(request,'pybo/detail.html',context)































	
	
	
	
@login_required(login_url="common:login")
	
def answer_modify(request,answer_id):
	answer = get_object_or_404(Answer,pk=answer_id)
	if request.method == "POST":
		form = AnswerForm(request.POST,instance= answer)
		if form.is_valid():
			answer = form.save(commit=False)
			answer.author = request.user
			answer.modify_date = timezone.now()
			answer.save()
			
			# print("DONE : anser :")
			# pprint(vars(answer.question))

			print("modify works")

			return redirect("{}#answer_{}".format(
				resolve_url('pybo:detail',question_id = answer.question.id),
				answer.id
			))
			
			
	else:
		form = AnswerForm(instance=answer)
	context = {'form':form}
	return render(request,'pybo/answer_form.html',context)
	
	
	
	
	
@login_required(login_url="common:login")

def answer_delete(request,answer_id):
	answer = get_object_or_404(Answer,pk=answer_id)
	if answer.author != request.user:
		print("you wrong user. you are hacker?")
	
	else:
		answer.delete()
		print("delete done .. lol !")
	return redirect("pybo:detail",question_id= answer.question.id)

