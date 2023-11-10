from geopy.distance import geodesic
from oauth_app.models import *
from .models import *

# User must be within this many meters of the objective to discover it
DESTINATION_RADIUS = 20


# Returns distance in meters
def geo_distance(lat_0, lon_0, lat_1, lon_1):
    point_0 = (lat_0, lon_0)
    point_1 = (lat_1, lon_1)
    return geodesic(point_0, point_1).kilometers * 1000


def get_hint(request, guess_lat, guess_lon):
    try:
        active_game = ActiveGame.objects.get(user=request.user)
    except ActiveGame.DoesNotExist:
        return False
    game = active_game.game

    prev_dist = geo_distance(active_game.last_latitude, active_game.last_longitude, game.latitude, game.longitude)
    guess_dist = geo_distance(guess_lat, guess_lon, game.latitude, game.longitude)

    if guess_dist < prev_dist:
        active_game.curr_hint = "H"
    else:
        active_game.curr_hint = "C"

    active_game.hint_counter += 1
    # Set as new last location so next hint can be checked against it
    active_game.last_latitude = guess_lat
    active_game.last_longitude = guess_lon

    if guess_dist < DESTINATION_RADIUS:
        active_game.is_finished = True

    active_game.save()
    return True