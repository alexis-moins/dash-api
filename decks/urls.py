from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.DeckListCreateView.as_view()),
    path('<int:id>', views.DeckRetrieveView.as_view()),

    path('<int:deck>/cards/', include('cards.urls')),

    path('update/<int:id>/', views.DeckUpdateView.as_view()),
    path('delete/<int:id>/', views.DeckDeleteView.as_view()),
]
