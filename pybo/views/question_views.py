from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect, reverse, resolve_url
from django.urls import reverse_lazy,resolve


from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question



@login_required(login_url="common:login")

def question_create(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():

			question = form.save(commit=False)
			question.author = request.user
			question.create_date = timezone.now()
			question.save()

			return redirect("pybo:index")
	else:
		form = QuestionForm()
		context = {'form':form}
		return render(request,'pybo/question_form.html',context)




from django.http import HttpResponse, HttpResponseRedirect

@login_required(login_url = "common:login")
def question_modify(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	
	if request.method == "POST":
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			
			question = form.save(commit=False)
			question.author = request.user
			question.modify_date = timezone.now()

			question.save()
			# return redirect("pybo:detail",question_id = question.id)
			print("--works 근데 그냥 question을 호출하면 되자나?")
			print( resolve_url(question) )

			# return redirect(question)
			# return HttpResponseRedirect("/pybo/about/")
			return HttpResponseRedirect("http://www.naver.com")



		# 만약 쓴제대로 다면 이렇게 된다.		 
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

			


	else:
		form = QuestionForm(instance=question)
		context = {'form':form}
	
	return render(request,'pybo/question_form.html',context)
	
			
@login_required(login_url="common:login")
def question_delete(request,question_id):
	
	question = get_object_or_404(Question,pk=question_id)
	if request.user != question.author:
		print('fuckyoff you are not hime')
	question.delete()
	return redirect("pybo:index")

	
from django.http import HttpResponse














from django.views.generic import TemplateView
from django.views.generic import DetailView


# templateView는 argument 안에 들어간다.


class AboutView(TemplateView):
	template_name = "pybo/about.html"





	



# class BookView(DetailView):
#     template_name = "book.html"
#     def get_context_data(self, **kwargs):
# 		""" get_context_data let you fill the template context """
#         context = super(BookView, self).get_context_data(**kwargs)
#         # Get Related publishers
#         context['publishers'] = self.object.publishers.filter(is_active=True)
#         return context






def hresponse_view(request):
    return HttpResponse("HRESPONSE WORKS : 이건 템플레이트가 필요없음")



def reverse_view(request,question_id):
	print("hello im reverse view!")
	# print( reverse("pybo:reverse", args=[question_id]) )
	return HttpResponse( reverse("pybo:reverse", args=[question_id]) )



def resolveurl_view(request,question_id):
	return HttpResponse( resolve_url("pybo:resolveurl_view",question_id) )
	


def redirect_view(request,question_id):
	print("hello im redirect view!")
	print( redirect('pybo:reverse', question_id) )
	return redirect('pybo:reverse', question_id)

def reverselazy_view(request,question_id):
	return HttpResponse( reverse_lazy("pybo:reverse",args=[question_id]) )
	


def resolve_view(request,question_id):
	return HttpResponse("works!")













