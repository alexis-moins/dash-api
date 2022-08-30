from django.urls import path
from . import views


urlpatterns = [
    path('', views.CardListCreateView.as_view()),
    path('<int:id>', views.CardRetrieveView.as_view()),
    # path('update/<int:id>/', views.DeckUpdateView.as_view()),
    # path('delete/<int:id>/', views.DeckDeleteView.as_view())
]
