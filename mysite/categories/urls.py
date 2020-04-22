from django.urls import path

from . import views

app_name = 'categories'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('', views.index, name='index'),
    path('add', views.new_category, name='add'),
    path('<int:pk>/', views.detail_category, name='detail'),
    path('edit/<int:pk>/', views.edit_category, name='edit'),
    path('delete/<int:pk>', views.delete_category, name='delete'),
]