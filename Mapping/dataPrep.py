
"""
To append the database with the time data for all the people
"""

"""
    FORMAT OF DATA INPUT
    data = [
        [ ((long1, lat1), (long2, lat2)) ]
    ]

    FORMAT OF DATA RETURN
    data = [
        [ ((long1, lat1), (long2, lat2)), TIME_FOR_TRAVEL, DISTANCE ]
    ]
"""

def prep(names):
    import openrouteservice
    
    from geopy.geocoders import Nominatim
    locator = Nominatim(user_agent = "myapp")

    client = openrouteservice.Client(key='5b3ce3597851110001cf62489c813a54852e46cfaba5c882462e815d')
    data = []
    for name in names:
        start, end = name

        location_start = locator.geocode(start)
        location_end = locator.geocode(end)
        obj = ((location_start.longitude, location_start.latitude), (location_end.longitude, location_end.latitude))
        res = client.directions(obj)
        
        data.append([obj, res['routes'][0]['segments'][0]['distance'], res['routes'][0]['segments'][0]['duration'], name])

    return data

# def dataPrep(data, names):
    
#     import openrouteservice
#     client = openrouteservice.Client(key='5b3ce3597851110001cf62489c813a54852e46cfaba5c882462e815d')
        
#     loc = list(zip(data, names))
    
#     for obj, name in loc:
    
#         res = client.directions(obj)
#         data.append([obj, res['routes'][0]['segments'][0]['distance'], res['routes'][0]['segments'][0]['duration'], name])

#     return data

# data = [
#   [((76.9423829, 8.5186064), (75.7846487, 11.248138))],
#   [((76.9423829, 8.5186064), (75.7846487, 11.248138))],
  
# ]
# print('\n', timeCal(data), '\n')
        
