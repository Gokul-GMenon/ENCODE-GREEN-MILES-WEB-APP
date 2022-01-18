
from os import stat


def distance(start, end):

    import math

    result_sq = (end[0] - start[0])**2 + (end[1] - start[1])**2
    
    return math.sqrt(result_sq)
total_time= [0]*3
def update(state, duration):

    if state['a'] == 1:
        total_time[0] += duration
    if state['b'] == 1:
        total_time[1] += duration
    if state['c'] == 1:
        total_time[2] += duration
        
def timeCal(group):

    print('\nInside timecal\n')
    # for obj in group:
    #     print(group)
    locs_start = {'a': group[0][-1][0], 'b': group[1][-1][0], 'c': group[2][-1][0]}
    locs_end = {'a': group[0][-1][1], 'b': group[1][-1][1], 'c': group[2][-1][1]}
    import openrouteservice
    client = openrouteservice.Client(key='5b3ce3597851110001cf62489c813a54852e46cfaba5c882462e815d')
        

    # Centroid of the start coordinates
    ct_start_x = (group[0][0][0][0] + group[1][0][0][0] + group[2][0][0][0])/3
    ct_start_y = (group[0][0][0][1] + group[1][0][0][1] + group[2][0][0][1])/3

    # Centroid of the end coordinates
    ct_end_x = (group[0][0][1][0] + group[1][0][1][0] + group[2][0][1][0])/3
    ct_end_y = (group[0][0][1][1] + group[1][0][1][1] + group[2][0][1][1])/3

    # Calculating the mid point
    mid_x = (ct_start_x + ct_end_x)/2
    mid_y = (ct_start_y + ct_end_y)/2

    mid = (mid_x, mid_y)

    # Mapping the start routes
    d_a = distance(group[0][0][0], mid)
    d_b = distance(group[1][0][0], mid)
    d_c = distance(group[2][0][0], mid)

    start =[]

    if d_a > d_b and d_a > d_c:

        if d_b > d_c:
        
            start = ['a', 'b', 'c']
        
        else:
        
            start = ['a', 'c', 'b']
    
    elif d_b > d_c and d_b > d_a:
    
        if d_c > d_a:
    
            start = ['b', 'c', 'a']
    
        else:
    
            start = ['b', 'a', 'c']
    else:

        if d_a > d_b:
        
            start = ['c', 'a', 'b']
        
        else:
        
            start = ['c', 'b', 'a']

    # Mapping the end routes
    d_a = distance(group[0][0][1], mid)
    d_b = distance(group[1][0][1], mid)
    d_c = distance(group[2][0][1], mid)

    end =[]

    if d_a > d_b and d_a > d_c:

        if d_b > d_c:
        
            end = ['a', 'b', 'c']
        
        else:
        
            end = ['a', 'c', 'b']
    
    elif d_b > d_c and d_b > d_a:
    
        if d_c > d_a:
    
            end = ['b', 'c', 'a']
    
        else:
    
            end = ['b', 'a', 'c']
    else:

        if d_a > d_b:
        
            end = ['c', 'a', 'b']
        
        else:
        
            end = ['c', 'b', 'a']
    

    # Noting the starting times

    state = { 'a': 0, 'b': 0, 'c': 0 }
    start_dict = {'a': group[0][0][0], 'b': group[1][0][0], 'c': group[2][0][0]}

    for i in range (len(start)):
        state[start[i]] = 1

        if start[i] != start[-1]:

            res = client.directions((start_dict[start[i]], start_dict[start[i+1]]))

            update(state, res['routes'][0]['segments'][0]['duration'])
    
    # Noting the ending times
    state = { 'a': 1, 'b': 1, 'c': 1 }
    end_dict = {'a': group[0][0][1], 'b': group[1][0][1], 'c': group[2][0][1]}

    res = client.directions((start_dict[start[-1]], end_dict[end[0]]))

    total_time[0] += res['routes'][0]['segments'][0]['duration']
    total_time[1] += res['routes'][0]['segments'][0]['duration']
    total_time[2] += res['routes'][0]['segments'][0]['duration']

    state[end[0]] = 0

    for i in range(len(end)):

        if end[i] != end[-1]:

            res = client.directions((end_dict[end[i]], end_dict[end[i+1]]))

            update(state, res['routes'][0]['segments'][0]['duration'])
    
            state[end[i+1]] = 0
    route = locs_start[start[0]] + ' -> ' + locs_start[start[1]] + ' -> ' + locs_start[start[2]] + ' -> ' + locs_end[end[0]] + ' -> ' + locs_end[end[1]] + ' -> ' + locs_end[end[2]] + '\nTime for each passenger - ' +  str(total_time[0]/600) + ', ' + str(total_time[1]) + ', ' + str(total_time[2])
    return start, end, total_time, route
