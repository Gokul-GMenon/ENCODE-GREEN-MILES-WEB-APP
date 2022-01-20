# from geopy.geocoders import Nominatim
# from openrouteservice import os
# import nominatim
# start = ['Ulloor', 'Pattom', 'Kaniyapuram', 'Vattappara']
# end = ['Kazhakkoottam', 'Menamkulam', 'Sreekariyam', 'Aakkulam']
# start = ['Shoranur', 'Pathirippala', 'Kulappully', 'Cheruthuruthi']
# end = ['Kolazhy', 'Guruvayur', 'Kunnamkulam', 'Wadakkanchery']
def call(start, end):
    flag = 0
    for place in start:
        try:
            
            from geopy.geocoders import Nominatim
            # import nominatim
            locator = Nominatim(user_agent = "myapp")
            # print('Hi')
            location = locator.geocode(place)
            location.longitude
        except:
            print(place, ' is not available')
            flag = 1

    for place in end:
        try:
            from geopy.geocoders import Nominatim
            locator = Nominatim(user_agent = "myapp")
            location = locator.geocode(place)
            location.longitude
        except:
            print(place, ' is not available')
            flag = 1
    if flag ==1:
        return 1
    routes = list(zip(start, end))

    from dataPrep import prep

    data = prep(routes)
    # loc = []

    # location_start1 = locator.geocode(start1)
    # location_end1 = locator.geocode(end1)

    # location_start2 = locator.geocode(start2)
    # location_end2 = locator.geocode(end2)

    # location_start3 = locator.geocode(start2)
    # location_end3 = locator.geocode(end3)

    # location_start4 = locator.geocode(start3)
    # location_end4 = locator.geocode(end4)

    # names = []

    # loc.append(((location_start1.longitude, location_start1.latitude), (location_end1.longitude, location_end1.latitude)))
    # names.append((start1, end1))

    # loc.append(((location_start2.longitude, location_start2.latitude), (location_end2.longitude, location_end2.latitude)))
    # names.append((start2, end2))

    # loc.append(((location_start3.longitude, location_start3.latitude), (location_end3.longitude, location_end3.latitude)))
    # names.append((start3, end3))

    # loc.append(((location_start4.longitude, location_start4.latitude), (location_end4.longitude, location_end4.latitude)))
    # names.append((start4, end4))

    # print(loc)
    # loc = list(zip(loc, names))
    # data = [] 
    # for obj, name in loc:
        
    #     res = client.directions(obj)
    #     data.append([obj, res['routes'][0]['segments'][0]['distance'], res['routes'][0]['segments'][0]['duration'], name])

    from route_decide import route
    # print(data)
    final = route(data, 0)

    return final
    # for obj in final:
    #     print(obj['route'])

# print(data)