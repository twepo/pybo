from django.shortcuts import render



def index(request):

	print("hello LG indexview")

	return render(request,'lg/index.html',{})

