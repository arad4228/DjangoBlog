from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

# CBV를 위한 라이브러리.
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# url 패턴에서 실행하는 함수
from .forms import CommentForm
from .models import Post, Category, Tag



# Post C,U Class Based Views (CBV)
class PostCreate(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = Post
    fields = ['title', 'hook_msg','content','head_image','attached_file','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_msg','content','head_image','attached_file','category', 'tags']

    template_name = "blog/post_form_update.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied

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
        context['comment_form'] = CommentForm
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

def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'Categories': Category.objects.all(),
        'No_Categoriy_Post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)

def addComment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_Form = CommentForm(request.POST)
            if comment_Form.is_valid():
                # commit = false가 없으면 바로 DB에 저장된다.
                comment = comment_Form.save(commit=False)
                comment.post=post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    return None

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