"""
Main function to decide the best possible route
"""

"""
Function to sort all the residents in ascending order of the travel time
"""
# from dis import dis
# from distutils.errors import DistutilsClassError
# from logging import lastResort
# from math import dist
# from operator import le
# from time import time
# from turtle import distance
import openrouteservice
    
client = openrouteservice.Client(key='5b3ce3597851110001cf62489c813a54852e46cfaba5c882462e815d')


def sort_time(data):
    sorted = []

    for i in range(len(data)):
        sorted.append([data[i][1], i])
    print(sorted, '\n\n')
    for i in range(len(data)-1):
        for j in range(0, len(data)-i-1):
            if sorted[j][0] > sorted[j+1][0]:
                temp = sorted[j]
                sorted[j] = sorted[j+1]
                sorted[j+1] = temp
    
    # Printing of the sorted data
    print(sorted)

"""
We've to look for all combinations to see the minimum time it would take for all the customers to get a route. We've to make sure it doesn't take 
more than 40% extra time for the longest and the second longest customers. Also as we search we indice from the longest to the shortest. So we 
start from the longest and seach for the shorter ones. In ideal case, our customer will end up in the shortest path grouped with two larger ones.
But if an ideal scenario was not found, we've to save the most efficient one in that case and start searching by upgrading our customer to the larger 
route. Our priority is to end up with less than 40% extra time for all customers and in the worst scenario, to maintain the shortest time for the 
longest travelling customer.
"""

# Denotes the final group which is assigned. group is ordered in such a way that it will contain the longest passenger at the top down to the 
# shortest
group = []

"""
We return the time calculated, and the difference in distance travelled with the first and the second passenger. This shows the distance that is 
not shared by the first passenger in the whole trip
We also return an integer which denote whether the total time was kept within the 40% threshold 
"""

def sort(ls):

    # sorting all except the last one in descending order
    for i in range(0, len(ls)-2):
        for j in range(0, len(ls)-i-2):
            if ls[j][0][-1]<ls[j+1][0][-1]:
                temp = ls[j+1]
                ls[j+1] = ls[j]
                ls[j] = temp


def checkTime(group):#, cond):
    
    from Mapping.timeCalReal import timeCal
    # from Mapping.timeCalReal import timeCal

    start, end, total_time, route = timeCal(group)
    og_time = [0]*3
    
    res = client.directions(group[0][0])
    og_time[0] = res['routes'][0]['segments'][0]['duration']

    res = client.directions(group[1][0])
    og_time[1] = res['routes'][0]['segments'][0]['duration']
    
    res = client.directions(group[2][0])
    og_time[2] = res['routes'][0]['segments'][0]['duration']    

    # coords = (group[0][0][0], group[1][0][0])                               # Member 1b-2b
    # res = client.directions(coords)
    # total_time.append(res['routes'][0]['segments'][0]['duration'])          # For member 1
    # dist.append(res['routes'][0]['segments'][0]['distance'])
    
    # coords = (group[1][0][0], group[2][0][0])                               # Member 2b-3b
    # res = client.directions(coords)
    # total_time[0] += res['routes'][0]['segments'][0]['duration']            # For member 1
    # dist[0] += res['routes'][0]['segments'][0]['distance']
    # total_time.append(res['routes'][0]['segments'][0]['duration'])          # For member 2
    # dist.append(res['routes'][0]['segments'][0]['distance'])
    
    # coords = (group[2][0][0], group[2][0][1])                               # Member 3b-3e
    # res = client.directions(coords)
    # total_time[0] += res['routes'][0]['segments'][0]['duration']            # For member 1
    # dist[0] += res['routes'][0]['segments'][0]['distance']
    # total_time[1] += (res['routes'][0]['segments'][0]['duration'])          # For member 2
    # total_time.append(res['routes'][0]['segments'][0]['duration'])          # For member 3
    # dist[1] += res['routes'][0]['segments'][0]['distance']
    
    # coords = (group[2][0][1], group[1][0][1])                               # Member 3e-2e
    # res = client.directions(coords)
    # total_time[0] += res['routes'][0]['segments'][0]['duration']            # For member 1
    # total_time[1] += res['routes'][0]['segments'][0]['duration']            # For member 2
    # dist[0] += res['routes'][0]['segments'][0]['distance']
    # dist[1] += res['routes'][0]['segments'][0]['distance']
    
    # coords = (group[1][0][1], group[0][0][1])                               # Member 2e-1e
    # res = client.directions(coords)
    # total_time[0] += res['routes'][0]['segments'][0]['duration']            # For member 1
    # dist[0] += res['routes'][0]['segments'][0]['distance']
    # if cond == 0:

    if total_time[0] <= (140/100)*og_time[0]:
        if total_time[1] <= (140/100)*og_time[1]:
            if total_time[2] <= (140/100)*og_time[2]:
                return 0, list(zip(total_time, og_time)), start, end, route
            else:
                return 1, list(zip(total_time, og_time)), start, end, route
    
        else:
            return 2, list(zip(total_time, og_time)), start, end, route
    else:
        return 3, list(zip(total_time, og_time)), start, end, route


"""
The structure of final list: 
    It is a list of dictionaries
        {
            'items': 3 membered tuple containing the indices of the people that has been grouped
            'val':  Number denoting the efficiency of the group with respect to traveller 1 and traveller 2
            'total_time':   Amount of total time the first user has to travel
        }
"""
final_list = []

# Function to check all the combinations and to prepare the final list. 
# "ls" is the list sorted by the longest distance except for the last value which is of the customer 

def final_prep(ls):
    
    i=0             # Indicates where the current user is
    
    j=0             # To loop thorugh the rest
    while True:

        # If the customer is considered the shortest
        if i==0:

            if ls[j][0][-1]<ls[-1][0][-1]:
                i=2
                continue
            else:
                if i!= 1:
                    # print(len(ls))
                    if ls[j+1] == ls[-1]:
                        break
                    # print('done') 
                    for k in range(j+1, len(ls)-1):
                        if ls[k][0][-1]<ls[-1][0][-1]:
                            i=1
                            j=-1
                            break
                        else:
                            group = [ls[j][0], ls[k][0], ls[-1][0]]
                            val, times, start, end, route = checkTime(group)
                            final_list.append({'start': start, 'end': end, 'val': val, 'times': times, 'route': route})
                    
                    j+=1
        elif i==1:
            
            if ls[j][0][-1]<ls[-1][0][-1]:
                i=2
                j=0
                continue
            else:
                for k in range(j+1, len(ls)-1):
                    group = [ls[j][0], ls[-1][0], ls[k][0]]
                    val, times, start, end, route = checkTime(group)
                    final_list.append({'start': start, 'end': end, 'val': val, 'times': times, 'route': route})
                
                    
                j+=1
                if ls[j+1] == ls[-1]:
                    break

        elif i==2:
            
            for k in range(j+1, len(ls)-1):
                group = [ls[-1][0], ls[j][0], ls[k][0]]
                val, times, start, end, route = checkTime(group)
                final_list.append({'start': start, 'end': end, 'val': val, 'times': times, 'route': route})
            break
    return

def route(data, cusInd):    

    # To filter out all members who are more than 15kms away as this will reduce computation by a large margin
    list_15 = []

    for i in range(len(data)):
        
        if i == cusInd:
            continue
        
        coords = (data[i][0][0], data[cusInd][0][0])
        res = client.directions(coords)
        # print(res['routes'][0]['segments'][0]['distance']/10000)
        if res['routes'][0]['segments'][0]['distance']/10000 <= 40:
            list_15.append([data[i], i])
            # print([data[i], i])        
        
    # Appending the current users data
    list_15.append([data[cusInd], cusInd])
    # print(list_15)
    # Sorting the list
    sort(list_15)

    for item in list_15:
        print(item)

    # Creating the final list
    final_prep(list_15)


    return final_list
"""
This will be the output from the timeCal fucntion. This is passed onto the sorting algorithm while remembering the indice of our original customer
"""
# data = [
#         [((76.9423829, 8.5186064), (75.7846487, 11.248138)), 22044.7, 374278.6],
#         [((76.9423829, 8.5186064), (75.7846487, 11.248138)), 220, 374278.6],
#     ]
# route(data, 3)