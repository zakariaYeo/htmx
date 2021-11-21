from django.urls import path
from movies.views import *

app_name = 'movie'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

htmx_urlpatterns = [
    path('check_name', check_name, name='check_name'),
    path('add_film', add_film, name='add_film'),
    path('delete_film/<int:pk>/', delete_film, name='delete_film'),
    path('search_film', search_film, name='search_film'),
]

urlpatterns += htmx_urlpatterns