from math import sin, cos, sqrt, atan2, radians
from shapely.geometry import Polygon


def calculate_distance(_distance1:list, _distance2:list):
    
    # Approximate radius of earth in km
    R = 6373.0

    lat1 = _distance1[0]
    lon1 = _distance1[1]

    lat2 = _distance2[0]
    lon2 = _distance2[1]

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return round(distance,3)


def overlap_percentage(outer_polygon, inner_polygon):
    """Calculates the percentage of a polygon that overlaps with another polygon."""

    outer_polygon = Polygon(outer_polygon)
    inner_polygon = Polygon(inner_polygon)

    ratio = outer_polygon.intersection(inner_polygon).area / inner_polygon.area
    return round(ratio * 100, 2)


def get_location_data(_location_name, _dataset):

    _position = None
    _return = None

    for i, val in enumerate(_dataset):
        if val['name'] == _location_name:
            _position = i

    if _position is not None:
        _return = _dataset[_position]

    return _return


