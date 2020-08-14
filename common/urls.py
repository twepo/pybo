from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

#  as로 닉네임을 정해서. auth_views 로 밑에서 사용한다.


app_name = 'common'

urlpatterns = [
    path("login/",
         auth_views.LoginView.as_view(
                template_name="common/login.html",
                redirect_authenticated_user=True),
                name="login"),
    
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
]



# 아..template_name을 원래 view에서 해주는데, 여기서 간단하게 가능하다.
# > urls는 function조립기야.

# 이때 그냥하면 LoginView에서 template를 확인하고 없으면 에러를 발생시킨다.
