from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Human, Profession
from .forms import HumanForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


def test_hw(request):
    objects = Human.objects.all()
    pagination = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = pagination.get_page(page_num)
    return render(request, 'homework/test_hw.html', {'page_obj': page_objects})


class HomeHuman(ListView):
    model = Human
    context_object_name = 'humans'
    template_name = 'homework/humans.html'
    extra_context = {'title': " "}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список человеков'
        return context

    def get_queryset(self):
        return Human.objects.filter(is_adult=True).select_related('profession')


class HumanByProfession(ListView):
    model = Human
    context_object_name = 'humans'
    template_name = 'homework/profession.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profession'] = Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'],
                                   is_adult=True).select_related('profession')


class ViewHuman(DetailView):
    model = Human
    context_object_name = 'human'
    template_name = 'homework/human_view.html'


class AddHuman(LoginRequiredMixin, CreateView):
    form_class = HumanForm
    template_name = 'homework/add_human.html'
    login_url = '/admin/'


# def humans(request):
#     humans = Human.objects.all()
#     # professions = Profession.objects.all()
#     context = {
#         'humans': humans,
#         'title': 'Список человеков',
#         # 'professions': professions,
#     }
#     return render(request, 'homework/humans.html', context=context)
#
#
# def get_profession(request, profession_id):
#     humans = Human.objects.filter(profession_id=profession_id)
#     # professions = Profession.objects.all()
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'humans': humans,
#         # 'professions': professions,
#         'profession': profession,
#     }
#     return render(request, 'homework/profession.html', context=context)
#
#
# def human_view(request, human_id):
#     human = get_object_or_404(Human, pk=human_id)
#     context = {
#         'human': human,
#     }
#     return render(request, 'homework/human_view.html', context=context)
#
#
# def add_human(request):
#     if request.method == 'POST':
#         form = HumanForm(request.POST)
#         if form.is_valid():
#             human = form.save()
#             return redirect(human)
#     else:
#         form = HumanForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'homework/add_human.html', context=context)


# def todo_list(request):
#     print(request)
#     return HttpResponse('<ul>'
#                         '<li>Перебери чечевицу</li>'
#                         '<li>Отдели её от гороха</li>'
#                         '<li>Познай самою себя</li>'
#                         '</ul>')

