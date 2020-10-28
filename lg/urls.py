from django.urls import path, reverse_lazy

from . import views


app_name = "lg"


urlpatterns = [


	path('', views.index, name="index" ),

	path('2/', views.index2, name="index2" ),
	path('3/', views.index3, name="index3" ),


	path('campaign/', views.campaign_view, name="campaign_view" ),






	path("api/campaign_list/", views.campaign_list, name="campaign_list"),

	path("api/select_list/<str:type>", views.select_list, name="select_list"),
	#path("api/select_list/<str:type>", views.select_list.as_view(), name="select_list"),



	path('home/', views.HomeView.as_view(), name="home" ),

	path("api/todo/list", views.ApiTodoLV.as_view(), name="list"),




]

