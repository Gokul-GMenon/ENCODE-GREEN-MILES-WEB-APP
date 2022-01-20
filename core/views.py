from datetime import date
from http.client import HTTPResponse
from operator import le
from os import getloadavg
from pydoc import doc
import re
from time import time
from urllib import response
from Mapping import caller
from django.db import reset_queries
# from django.http import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import DataFieldSerializer
from .models import DataField
from .forms import data, reg
# from core import serializers
# Create your views here.
pk = DataField.objects.first().id
def add(request):
    global pk
    count= DataField.objects.last()
    print(request.method)
    if request.method == 'POST':
        
        form = reg(request.POST)
        
        print('\n\nHi')
        
        print('\n\n',form,'\n\n')
        if form.is_valid():
            # print("Hiiii")
            name = form.cleaned_data['name']
            ph = form.cleaned_data['ph']
            print('\nname',name)
            # Entering
            obj = DataField()
            obj.name = name
            obj.ph_no = ph
            obj.no=0
            pk = obj.id=count.id+1
            # pk = DataField.objects.all().count()
            obj.save()
            # print('\n\n',temp,'\n\n')
            return redirect('home')
    else:
        print('hi')
        form = reg()

    return render(request, 'core/add.html', {'form': form})
    # obj = DataField.objects.all()
    # names = []
    # ids = []
    # for i, user in enumerate(obj, start=1):
    #     ids.append(i)
    #     names.append(user.name)


def home(request):
    global pk
    # obj = DataField.objects.get(id = str(1))
    # print('\nName1 ', obj.name)
    # obj = DataField.objects.get(id = str(2))
    # print('Name2 ', obj.name)
    # obj = DataField.objects.get(id = str(3))
    # print('Name3 ', obj.name)
    # obj = DataField.objects.get(id = str(4))
    # print('Name4 ', obj.name)
    # obj = DataField.objects.get(id = str(5))
    # print('Name5 ', obj.name)
    return render(request, 'core/index.html', {'pk': pk})

def cab1(request, pk):
    global t
    t=0
    if request.method == 'POST':
        
        form = data(request.POST)

        # print('\n\n',form,'\n\n')
        if form.is_valid():
            # print("Hiiii")
            start = form.cleaned_data['start']
            date = form.cleaned_data['date']
            end = form.cleaned_data['end']
            time = form.cleaned_data['time']
            
            # Updating
            obj = DataField.objects.get(id = pk)
            obj.time = str(time)
            print("\n",str(data),'\n ')
            obj.date = str(date)
            obj.end = end
            obj.start = start
            obj.save()
            # print('\n\n',temp,'\n\n')
            return redirect('cab2', pk)
    else:
        # print('hi')
        form = data()
        
    return render(request, 'core/sharecab.html', {'form': form, 'pk': pk})

def checktime(time, curr_time):
    val = 0
    from datetime import datetime
    FMT = "%H:%M:%S"
    # print('\ntime-',time)
    # print('current-',curr_time,'\n')

    tdelta1 = str(datetime.strptime(time, FMT) - datetime.strptime(curr_time, FMT))
    tdelta2 = str(datetime.strptime(curr_time, FMT) - datetime.strptime(time, FMT))

    # print('\ntdelta1- ',str(tdelta1))
    # print('tdelta2- ',tdelta2,'\n')

    if len(tdelta1) == 7:
       if int(tdelta1[:-6]) <=1:
        val = 1 
    elif len(tdelta2) == 7:
        if int(tdelta2[:-6]) <=2:
            val = 1
    return val

final = ''
ids = []
t = 0
def load(pk):
    global final, ids, t
    t=0
    id = int(pk)-1
    start = []
    end = []
    ids.append(int(pk))
    curr_user = DataField.objects.get(id=pk)
    start.append(curr_user.start)
    end.append(curr_user.end)
    cur__time = curr_user.time
    print('\n\n')
    data = DataField.objects.all()
    
    for obs in data:
        id+=1
        # print('id ',id)
        if id == int(pk):
            # print('hi')
            continue

        if curr_user.date != obs.date:
            continue
        # print('id ', id,' pk ', pk,' ',' obs.name - ',obs.name,'\n')
        time = obs.time
        val = checktime(time, cur__time)
        if val==1:
            ids.append(id)
            start.append(obs.start)
            end.append(obs.end)
            # print(obs.name)

    print('start - ',start)
    if len(start) != 3:
        return -1
    print('end - ',end)
    final =  caller.call(start, end)
    print(final)
    ids =list(set(ids))
    print(ids)
    # return redirect('cab3')
    final = list(final)
    print(type(final))
    return 0
x = -1
dict = []
ids_selected = []

def cab2(request, pk):
    global t
    val = 0
    if t== 0:
        val = load(pk)
    if val == -1:
        return redirect('retry', pk)
    t+=1
    global ids, ids_selected, x, dict

    ids_selected = []
    x += 1
    print('\n\n\tfinal\n',final) 
    print('\nx ',x)
    if x == len(final):
        return redirect('retry', pk)
    acc = 0
    name = []
    start = []
    end = []
    time = []
    
    for i in range(len(ids)):
        flag = 0
        print('\n ids[i] - ',ids[i])
        obj = DataField.objects.get(pk = str(ids[i]))
        
        
        for item in final[x]['route']:
            # print('\nitem', item)
            if obj.start == item:
        
                ids_selected.append(str(ids[i]))
                flag = 1
                break
        
        if flag == 1:

            name.append(obj.name)
            start.append(obj.start)
            end.append(obj.end)
            time.append(obj.time)
    
    print('dict ',dict)
    dict = {'name1': name[0], 'name2': name[1], 'name3': name[2], 'start1': start[0], 'start2': start[1], 'start3': start[2], 'end1': end[0], 'end2': end[1], 'end3': end[2], 'time1': time[0], 'time2': time[1], 'time3': time[2]}
    
    return render(request, 'core/sharecab_2.html', {'pk': pk, 'route': final, 'name1': name[0], 'name2': name[1], 'name3': name[2], 'start1': start[0], 'start2': start[1], 'start3': start[2], 'end1': end[0], 'end2': end[1], 'end3': end[2], 'time1': time[0], 'time2': time[1], 'time3': time[2]})

def write_to_file(data, ids):
    import os
    
    gp = 0
    # while True:
    #     if os.path.isdir(os.path.join('txt_data', 'data_' + gp + '.txt')):
    #         gp += 1
    #     else:
    #         gp +=1
    #         break

    to_save = {'names': [data['name1'], data['name2'], data['name3']],
                'starts': [data['start1'], data['start2'], data['start3']],
                'ends': [data['end1'], data['end2'], data['end3']],
                'times': [data['time1'], data['time2'], data['time3']],
                'date': data['date'], 'group': gp}

    import json
    json_data = json.dumps(to_save, indent=4)

    for id in ids:
        obj = DataField.objects.get(id=id)
        obj.bookings = json_data
        obj.save()
    # with open(os.path.join('txt_data', 'data_' + gp + '.txt'), "w") as outfile:
    #     outfile.write(json_data)

def cab3(request, pk):
    # pk=1

    c_ids = ids_selected
    c_dict = dict

    # Removing those data from the database

    for i in range(len(c_ids)):
        obj = DataField.objects.get(id= c_ids[i])
        # import json
        # dat = json.loads(obj.bookings)
            
        c_dict['date'] = obj.date
        obj = DataField.objects.get(id= c_ids[i])
        obj.date=None
        obj.time=None
        obj.start=None
        obj.end=None
        obj.no= obj.no+1
        obj.save()
    print('\n',c_dict,'\n')
        
    write_to_file(c_dict, c_ids)
    
    for i in range(len(c_ids)):
        obj = DataField.objects.get(id = c_ids[i])
        c_dict['ph'+str(i+1)] = obj.ph_no
    c_dict['pk'] = pk
    print(c_dict)
    return render(request, 'core/shareacab_3.html', c_dict)

def profile(request, pk):
    global final
    # For extracting information from the database
    print('name - ',DataField.objects.last().id)
    data = DataField.objects.get(id=str(pk))
    name = data.name
    start =[]
    no = data.no
    ph = data.ph_no
    print('\nNOOO',no)
    if no != 0:
        print('\nNOOO',no)
        name = data.name
        ph = data.ph_no
        time = data.time
        start = data.start
        end = data.end
        no = data.no
        profile = []
        route=date=''
        if no!= 0:
            obj = DataField.objects.get(id =pk)
            import json
            dat = json.loads(obj.bookings)
            print(dat)
            date = dat['date']
            start1 = dat['starts'][0]
            start2 = dat['starts'][1]
            start3 = dat['starts'][2]
            end1 = dat['ends'][0]
            end2 = dat['ends'][1]
            end3 = dat['ends'][2]
            route = start1 + '->' + start2 + '->' + start3 + '->' + end1 + '->' + end2 + '->' + end3  


        data= {'name': name, 'ph': ph, 'time': time, 'start': start, 'end': end, 'no': no, 'date':date, 'route':route, 'pk':pk}
    else:
        data = {'name': name, 'ph': ph, 'no': no, 'pk': pk}
    return render(request, 'core/userprofile.html', data)

def retry(request, pk):

    return render(request, 'core/retry.html', {'pk': pk})