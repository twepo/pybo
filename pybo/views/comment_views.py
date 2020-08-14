


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment









@login_required(login_url="common:login")
def comment_create_question(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	if request.method=="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.question = question
			comment.author = request.user
			comment.create_date = timezone.now()
			comment.save()

			return redirect("{}#comment_{}".format(
					resolve_url('pybo:detail',question_id=question.id),
					comment.id
			))

	else:
		form = CommentForm()
		
	context = {'form':form}
	return render(request,'pybo/comment_form.html',context)





















@login_required(login_url="common:login")
def comment_modify_question(request,comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.modify_date = timezone.now()
			comment.save()

			print("cmt / question / edit works")
			return redirect("{}#comment_{}".format(
				resolve_url('pybo:detail',question_id=comment.question.id),
				comment.id
			))


	else:
		form = CommentForm(instance = comment)
	context ={'form':form}

	return render(request,'pybo/comment_form.html',context)

	  



@login_required(login_url="common:login")
def comment_delete_question(request,comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	if comment.author != request.user:
		print("CANNOT DELETE")
	else:
		comment.delete()
	print("EVERYTHING IS OKAY,BUT HOW TO GET DELTED DATA?")
	print(comment.question)
	print(comment.question.id)
	return redirect("pybo:detail" , question_id = comment.question.id)














@login_required(login_url="common:login")
def comment_create_answer(request,answer_id):
	answer = get_object_or_404(Answer,pk=answer_id)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.answer = answer
			comment.author = request.user
			comment.create_date = timezone.now()
			comment.save()

			return redirect("{}#comment_{}".format(
				resolve_url('pybo:detail',question_id = comment.answer.question.id),
				comment.id
			))

	else:
		form = CommentForm()
	context = {'form':form}
	return render(request,'pybo/comment_form.html',context)












@login_required(login_url="common:login")
def comment_modify_answer(request, comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.modify_date = timezone.now()
			comment.save()

			return redirect("{}#comment_{}".format(
				resolve_url("pybo:detail",question_id=comment.answer.question.id),
				comment.id
			))

	else:
		form = CommentForm(instance=comment)
	context = {'form':form}
	return render(request,'pybo/comment_form.html',context)		
	



@login_required(login_url="common:login")
def comment_delete_answer(request,comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	if request.user != comment.author:
		print("you cannot DELETE HIM")
	else:
		comment.delete()
	return redirect("pybo:detail", question_id = comment.answer.question.id)
	












