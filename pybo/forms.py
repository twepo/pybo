from django import forms
from pybo.models import Question, Answer, Comment





# forms..는 폴더이름이다 이기야
# 이 안에다가. requeest.post를 집어넣는다.

# AnswerForm( .. requeest.POST ..< -- CONTENT내용을 여기다)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용'
            }





class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content','subject')
        
    

    
    


from pybo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields='__all__'

    

        
    





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content'}
        
        labels = {
            'content':'눼용'
        }
        
    
    





































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    