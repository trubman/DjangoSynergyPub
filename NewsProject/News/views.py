from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from unicodedata import category
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .models import News, Category


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация прошла успешно')
#             # return redirect('login')
#             user = form.save()
#             login(request, user)
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'news/register.html', { 'form': form })
#
#
# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Ошибка авторизации')
#     else:
#         form = UserLoginForm()
#     return render(request, 'news/login.html', {'form': form})
#
#
# def user_logout(request):
#     logout(request)
#     return redirect('login')



def test(request):
    objects = ['john', 'paul', 'george', 'ringo', 'john1', 'paul1', 'george1', 'ringo1']
    pagination = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = pagination.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'news/home_news_list.html'
    extra_context = {'title': "Главная"}
    mixin_group = 'hello world'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        # context['mixin_group'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/home_news_list.html'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context=context)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item,
#     }
#     return render(request, 'news/view_news.html', context=context)


class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'news/add_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = News.objects.create(
#                 **form.cleaned_data
#             )
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'news/add_news.html', context=context)


# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for i in news:
#         res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p></div>\n<hr>\n'
#     return HttpResponse(res)