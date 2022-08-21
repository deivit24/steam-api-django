from datetime import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from steam import Steam
from decouple import config

from ..models import Account

KEY = config("STEAM_API_KEY", "")
steam = Steam(KEY)


@api_view(['GET'])
def search_steam_players(request, search):
    accounts = Account.objects.all()
    players = steam.users.search_user(search)
    return JsonResponse(players)


@api_view(['GET'])
def get_steam_player(request, steamid):
    try:
        account = Account.objects.get(steamid=steamid)
    except Account.DoesNotExist:
        account = None
    player = steam.users.get_user_details(steamid)["player"]

    if not account:
        _save_player_to_db(player)

    return JsonResponse(player)


@api_view(['GET'])
def create_account(request, steamid):
    try:
        Account.objects.get(steamid=steamid)
        return JsonResponse({"status": status.HTTP_403_FORBIDDEN, "message": "Player already in DB"})
    except Account.DoesNotExist:
        player = steam.users.get_user_details(steamid)["player"]

        _save_player_to_db(player)

        return JsonResponse(player)


@api_view(['GET'])
def get_steam_player_friends(request, steamid):
    friends = steam.users.get_user_friends_list(steamid)
    return JsonResponse(friends)


@api_view(['GET'])
def get_steam_player_recent_games(request, steamid):
    recent_games = steam.users.get_user_recently_played_games(steamid)
    return JsonResponse(recent_games)


@api_view(['GET'])
def get_steam_player_owned_games(request, steamid):
    owned_games = steam.users.get_owned_games(steamid)
    return JsonResponse(owned_games)


@api_view(['GET'])
def get_steam_player_level(request, steamid):
    level = steam.users.get_user_steam_level(steamid)
    return JsonResponse(level)


@api_view(['GET'])
def get_steam_player_badges(request, steamid):
    badges = steam.users.get_user_badges(steamid)
    return JsonResponse(badges)


@api_view(['GET'])
def get_steam_player_community_badges(request, steamid, badgeid):
    badges = steam.users.get_community_badge_progress(steamid, badgeid)
    return JsonResponse(badges)


@api_view(['GET'])
def get_steam_player_public_info(request, steamid):
    info = steam.users.get_account_public_info(steamid)
    return JsonResponse(info)


def _save_player_to_db(player):
    account = Account(
        steamid=player["steamid"],
        personaname=player["personaname"],
        communityvisibilitystate=player["communityvisibilitystate"],
        profilestate=player["profilestate"],
        profileurl=player["profileurl"],
        avatar=player["avatar"],
        avatarmedium=player["avatarmedium"],
        avatarfull=player["avatarfull"],
        avatarhash=player["avatarhash"],
        lastlogoff=datetime.fromtimestamp(player["lastlogoff"]),
        primaryclanid=player["primaryclanid"],
        timecreated=datetime.fromtimestamp(player["timecreated"]),
        personastateflags=player["personastateflags"],
        loccountrycode=player["loccountrycode"]
    )
    account.save()
