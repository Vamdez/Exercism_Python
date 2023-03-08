"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    [first, second, one, *rest] = each_wagons_id
    response = one, *missing_wagons, *rest, first, second
    return list(response)


def add_missing_stops(from_to, **stops):
    from_to["stops"] = list(stops.values())
    return from_to


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    resp = zip(*wagons_rows)
    return list(map(list, resp))

