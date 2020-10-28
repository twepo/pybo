"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from django.conf import settings
from django.conf.urls import include, url

from pybo.views import base_views


from lg import views


urlpatterns = [

    path("admin/", admin.site.urls),
    # path("pybo/", include("pybo.urls")),
    path("common/",include("common.urls")),
    # path('', views.index, name='index'),

    path('', include('lg.urls')),

]


# pybo 매핑은 위에서 되어있기 때문에,
# pybo 에서는 따로 매핑하지 않아도 된다.



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



# 장고 예약 변수임.. 404 오류시, 사용자가 정의한 뷰함수를 호출하는 변수!

handler404 = 'common.views.page_not_found'