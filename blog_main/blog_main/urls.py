"""blog_main URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

# 처리할 패턴을 넣기.
# url 패턴들 목록 - 상위에 있을 수록 특별한 Case, 아래일수록 일반적인 Case
# 위에서 부터 패턴 매칭을 하므로
urlpatterns = [
    path('blog/', include('blog.urls')),
    # include는 django.urls 라이브러리에 존재, import 해줘야 한다.
    # 해당 패턴을 사용하는 것을 cunsume이라고 한다.
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('single_pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)