from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('decks/', include('decks.urls')),
    path('cards/', include('cards.urls'))
]
