from django.urls import path
from django.views.decorators.cache import cache_page

from News.views import HomeNews, NewsByCategory, ViewNews, AddNews
# from News.views import register, user_login, user_logout
from News.views import test
# from News.views import index, get_category, view_news, add_news

urlpatterns = [
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('', index, name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news/', AddNews.as_view(), name='add_news'),
    # path('news/add_news/', add_news, name='add_news'),
    path('test/', test, name='test'),
    # path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]

