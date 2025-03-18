from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'),  # Define a view for the root URL
    path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
    path('snippets/<int:snippet_id>/comments/', comment_list, name='comment_list'),
]
