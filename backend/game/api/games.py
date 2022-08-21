from django.http import JsonResponse
from rest_framework.decorators import api_view
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY", "")
steam = Steam(KEY)


@api_view(['GET'])
def search_games(request, search):

    games = steam.apps.search_games(search)
    return JsonResponse(games)


@api_view(['GET'])
def get_game_details(request, gameid):
    game = steam.apps.get_app_details(gameid)
    return JsonResponse(game)


@api_view(['GET'])
def get_game_player_stats(request, gameid, steamid):
    stats = steam.apps.get_user_stats(steamid, gameid)
    return JsonResponse(stats)

