from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Portfolio

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_list, name='portfolio_list'),
    path('upload/', PortfolioCreateView.as_view(), name='portfolio_upload'),
    path('detail/<int:pk>/',DetailView.as_view(model=Portfolio, template_name='portfolio/detail.html'),
         name='portfolio_detail'),
    path('delete/<int:pk>/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('update/<int:pk>/', PortfolioUpdateView.as_view(), name='portfolio_update'),
]