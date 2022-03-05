from django.urls import path
from .views import SnackDetailView,SnackListView,SnackCreateView,SnackDeleteView,SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list' ),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('new/', SnackCreateView.as_view(), name='snack_create' ),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='snack_delete'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='snack_update' ),
]