from django.urls import path

from .api.accounts import (
    search_steam_players,
    get_steam_player,
    get_steam_player_friends,
    get_steam_player_recent_games,
    get_steam_player_owned_games,
    get_steam_player_level,
    get_steam_player_badges,
    get_steam_player_community_badges,
    get_steam_player_public_info,
    create_account
)

urlpatterns = [
    path('search/<str:search>', search_steam_players),
    path('player/<str:steamid>', get_steam_player),
    path('player/<str:steamid>/friends', get_steam_player_friends),
    path('player/<str:steamid>/recent_games', get_steam_player_recent_games),
    path('player/<str:steamid>/owned_games', get_steam_player_owned_games),
    path('player/<str:steamid>/level', get_steam_player_level),
    path('player/<str:steamid>/badges', get_steam_player_badges),
    path('player/<str:steamid>/badges/<int:badgeid>', get_steam_player_community_badges),
    path('player/<str:steamid>/info', get_steam_player_public_info),
    path('create_player/<str:steamid>', create_account)
]
