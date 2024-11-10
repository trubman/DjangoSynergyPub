from django.urls import path

# from Homework.views import todo_list
# from Homework.views import humans, get_profession, human_view, add_human
from Homework.views import test_hw
from Homework.views import HomeHuman, HumanByProfession, ViewHuman, AddHuman
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('humans/', cache_page(60)(HomeHuman.as_view()), name='humans'),
    path('humans/', HomeHuman.as_view(), name='humans'),
    path('profession/<int:profession_id>/', HumanByProfession.as_view(), name='profession'),
    path('human/<int:pk>/', ViewHuman.as_view(), name='human_view'),
    path('human/add_human/', AddHuman.as_view(), name='add_human'),
    path('test_hw/', test_hw, name='test_hw'),
    # path('cinderella/', todo_list),
    # path('humans/', humans, name='humans'),
    # path('profession/<int:profession_id>/', get_profession, name='profession'),
    # path('human/<int:human_id>/', human_view, name='human_view'),
    # path('human/add_human/', add_human, name='add_human'),
]

