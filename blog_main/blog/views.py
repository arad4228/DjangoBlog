from django.shortcuts import render
# Create your views here.

# CBV를 위한 라이브러리.
from django.views.generic import ListView, DetailView

# url 패턴에서 실행하는 함수
from .models import Post

# Class Based Views (CBV)
class PostList(ListView):
    model = Post # 모델 객체 설정.
    ordering = '-pk' # 정렬 방식 설정 = pk의 역순.

class PostDetail(DetailView):
    model = Post

# 템플릿 이름을 강제하는 방법.
# template_name = 'blog/index.html'
# 하지만, name convention에 익숙해진 사람들에게 혼선을 줄 수 있어, 지정한 대로 하는 것이 생산성이 높다.

# Function views를 위해 만든 함수들
#
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )