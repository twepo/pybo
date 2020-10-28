








# SELECT_RELATED 참조용

def campaign_list_SELECT_RELATED(request):

	queryset = Campaign.objects.all().select_related('category')[:5]

	for camp in queryset:
		pr(camp.category.kor_name)

	return HttpResponse("test", content_type="application/json")



# PREFETCH_RELATED :: 피자토핑테이블
from pybo.models import Book, Store

def campaign_list_PREFETCH_RELATED(request):

	queryset = Book.objects.all().prefetch_related('store_set')

	for book in queryset:
		pr(book.store_set.filter(id=1))

	return HttpResponse("test", content_type="application/json")






# TESTER
def campaign_list2(request):

	# channel = request.GET.get('channel', "")
	# category = request.GET.get('category', "")





	# queryset = Campaign.objects.select_related('category').all()
	queryset = Campaign.objects.all()


	# queryset = Campaign.objects.select_related('Category').values('title', 'subtitle','channel', 'category__eng_name','img_path','created_time').order_by('-created_time')

	# queryset = Campaign.objects.values('title', 'subtitle','channel', 'category__eng_name','img_path','created_time').order_by('-created_time')


	allowed_filters = ['category[]','channel[]']

	for filter_array_title in allowed_filters:

		filter_title = getArrayName(filter_array_title)

		# pr("filter_title",filter_title)

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




	# pr(queryset.title)
	# camps = []
	# for camp in queryset[:10]:  # queryset 평가
	# 	camps.append({
	# 		'id': camp.id,
	# 		'name': camp.title,
	# 		'category_title': camp.category.kor_name
	# 		}
	# 	)
	# pr(camps)


	# pr( camp_user )






	#data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
	# data = json.dumps(list(queryset[:5]), cls=DjangoJSONEncoder)

	data = serializers.serialize('json', queryset[:3])





	# pr("length")
	# pr(queryset.count())

	pr("sql :::::::::::::")
	pr(connection.queries)


	#return JsonResponse(data, safe=False)
	return HttpResponse(data, content_type="application/json")




