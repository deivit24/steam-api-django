from django.urls import path

from .api.games import (
    search_games,
    get_game_details,
    get_game_player_stats
)

urlpatterns = [
    path('search/<str:search>', search_games),
    path('<int:gameid>', get_game_details),
    path('<int:gameid>/accounts/<str:steamid>', get_game_player_stats),

]
