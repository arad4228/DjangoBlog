from django.shortcuts import render
# Create your views here.

# CBV를 위한 라이브러리.
from django.views.generic import ListView, DetailView

# url 패턴에서 실행하는 함수
from .models import Post, Category

# Class Based Views (CBV)
class PostList(ListView):
    model = Post        # 모델 객체 설정.
    ordering = '-pk'    # 정렬 방식 설정 = pk의 역순.

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = Post.objects.filter(category=None).count()
        return context

def show_category_posts(request, slug):
    if slug=='no-category' :  # 미분류 카테고리
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category = category)
    context = {
        'Categories' :Category.objects.all(),
        'No_Categoriy_Post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
        'post_list' : post_list
    }
    return render(request,'blog/post_list.html', context)

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
