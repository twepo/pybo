

from .base_views import *








def q_list(request):


	''' v1 SELECT REATARDED WAY >> '''
	# question_list = Question.objects.all()
	# for question in question_list:
	# 	print(question.subject, question.author.username ) 



	''' v1 SELECT_RELATED WAY '''
	# 연결할때는 Question에 있는 ForeginKey로 연결해준다!
	# question_list = Question.objects.all().select_related('author')
	# for question in question_list:
	# 	print(question.subject, question.author.username )




	''' V2 CHOI'S SELECT RETARD WAY '''
	# employees = Employee.objects.all()
	# for employee in employees:
	# 	print(employee.department.name)


	''' V2 CHOI'S SELECT_RELATED  WAY '''
	employees = Employee.objects.all().select_related('department')
	for employee in employees:
		print(employee.department.name)





	''' PREFETCH RETARED WAY '''
	# books = Book.objects.all()
	# for book in books:
	# 	print(book.store_set.all())
	



	''' PREFETCH RETARED WAY '''
	# books = Book.objects.all().prefetch_related('store_set')
	# for book in books:
	# 	print(book.store_set.all())


	







	return render(request,'pybo/q_list.html',{})






