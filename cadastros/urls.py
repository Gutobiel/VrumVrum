# from . import views
# from django.urls import path
# from .views import register

# from .views import cadastro, editar_usuario, excluir_usuario, lista_usuarios

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('update-user/<int:pk>/', views.update_user, name='update_user'),
#     path('delete-user/<int:pk>/', views.delete_user, name='delete_user'),
#     path('user-list/', views.user_list, name='user_list'),

# ]

from django.urls import path
from .views import GroupCreateView, GroupDeleteView, GroupListView, GroupUpdateView, RegisterView, UpdateUserView, DeleteUserView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('delete-user/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
    path('user-list/', UserListView.as_view(), name='user_list'),


    path('group-create/', GroupCreateView.as_view(), name='group_create'),
    path('group-update/<int:pk>/', GroupUpdateView.as_view(), name='group_update'),
    path('group-delete/<int:pk>/', GroupDeleteView.as_view(), name='group_delete'),
    path('group-list/', GroupListView.as_view(), name='group_list'),


]
