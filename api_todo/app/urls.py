from django.urls import path
from app.views import todo_detail_change_and_delete, TodoListAndCreate #, todo_list 

urlpatterns = [
    # path('',todo_list),
    path('',TodoListAndCreate.as_view()),
    path('<int:pk>/', todo_detail_change_and_delete),
]