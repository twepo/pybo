from django.urls import path, reverse_lazy

from .views import base_views, question_views, answer_views, comment_views, vote_views, q_views

from django.views.generic import CreateView
from pybo.models import Question, Todo






app_name = "pybo"

urlpatterns = [



    path('q_list/', q_views.q_list,name="q_list" ),




    path('api/', base_views.apiOverview,name="api-overview" ),


    path('q-list/', base_views.questionList,name="question-list" ),
    path('q-detail/<str:pk>/', base_views.questionDetail,name="question-detail" ),

    path('q-create/', base_views.questionCreate,name="question-create" ),

    path('t-list/', base_views.todoList,name="todo-list" ),
    path('t-create/', base_views.todoCreate,name="todo-create" ),

    path('t-update/<str:pk>/', base_views.todoUpdate,name="todo-update" ),
    path('t-delete/<str:pk>/', base_views.todoDelete,name="todo-delete" ),















    # path("home/", CreateView.as_view(model=Todo, fields=['title'], success_url=reverse_lazy('home')), name="home"),

    path("hssome/", base_views.TodoCreateView.as_view(), name="home"),




















    path("", base_views.index, name='index'),
    path("<int:question_id>/", base_views.detail, name="detail"),

    path("question/create/", question_views.question_create, name="question_create"),
    path("question/modify/<int:question_id>/", question_views.question_modify, name="question_modify"),
    path("question/delete/<int:question_id>/", question_views.question_delete, name="question_delete"),

    path("answer/create/<int:question_id>/", answer_views.answer_create, name="answer_create"),
    path("answer/modify/<int:answer_id>/", answer_views.answer_modify, name="answer_modify"),
    path("answer/delete/<int:answer_id>/", answer_views.answer_delete, name="answer_delete"),

    path("comment/create/question/<int:question_id>/", comment_views.comment_create_question, name="comment_create_question"),
    path("comment/modify/question/<int:comment_id>/", comment_views.comment_modify_question, name="comment_modify_question"),
    path("comment/delete/question/<int:comment_id>/", comment_views.comment_delete_question, name="comment_delete_question"),
    path("comment/create/answer/<int:answer_id>", comment_views.comment_create_answer, name="comment_create_answer"),
    path("comment/modify/answer/<int:comment_id>", comment_views.comment_modify_answer, name="comment_modify_answer"),
    path("comment/delete/answer/<int:comment_id>", comment_views.comment_delete_answer, name="comment_delete_answer"),



    path("vote/question/<int:question_id>/", vote_views.vote_question, name="vote_question"),
    path("vote/answer/<int:answer_id>", vote_views.vote_answer, name="vote_answer"),



    path("about/", question_views.AboutView.as_view(), name="about"),





    path("hresponse//", question_views.hresponse_view, name="hresponse"),
    path("reverse/<int:question_id>", question_views.reverse_view, name="reverse"),
    path("resolve_url/<int:question_id>", question_views.resolveurl_view, name="resolveurl_view"),
    path("redirect_view/<int:question_id>", question_views.redirect_view, name="redirect_view"),
    path("reverse_lazy/<int:question_id>", question_views.reverselazy_view, name="reverselazy_view"),
    path("resol/<int:question_id>", question_views.resolve_view, name="resolve_view"),



]
