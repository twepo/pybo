


from rest_framework import serializers
from .models import Question, Todo



        
class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields ='__all__'    



class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields ='__all__'    