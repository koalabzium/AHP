import json
import math

data = json.load(open('agusi.json'))
print(type(data["alternatives"]))
def decode_alternatives():
    alternatives=[]
    for i in data["alternatives"]:
        alternatives.append(i)
    return alternatives

alternatives=decode_alternatives()

def decode_reszte(data) :
    matrix = []
    lista=[]
    for i in data:
        #print(type(i))
        if type(data[i]) == dict:
            decode_reszte(data[i])
        lista.append(data[i])
    data.clear()

    print(lista)



'''import numpy as np
from scipy.stats import gmean


def toeigenvalue(data):
    for k, v in data.items():
        if isinstance(v, dict):
            toeigenvalue(v)
        else:
            if k!='alternatives':
                sqrt=int(math.sqrt(len(v)))
#                print(v)
                v=np.asmatrix(v)
                v=v.reshape(sqrt,sqrt)
#                print(v,0)
                v=gmean(v, axis=1)
#                print(v)
                v=(v.T).tolist()
                lista=[]
#                print(lista)
                for x in v:
                    for y in x:
                        lista.append(y)
                lista=np.asarray(lista)
                i=0
#                print(lista)
                suma=sum(lista)
#                print(suma)
                while i<lista.size:
                    lista[i]=lista[i]/suma
                    i=i+1
                data[k]=lista
                del lista
#                print(data[k])
    return data

def sumeigenvalue(data,lista):
    for k, v in data.items():
        if isinstance(v, dict):
           global parent_k
           global finalvector
           finalvector=0
           parent_k=k
           sumeigenvalue(v,lista)
        else:
            if k!='alternatives':
                if k=='matrix':
                    finalvector=0
                    i=0
                    critvector=v
                else:
                    finalvector=finalvector+critvector[i]*v
                    i=i+1
                    if i==critvector.size:
                        lista.append((parent_k, finalvector))
            
def replace_dict(data,lista):
    for k,v in data.items():
        for element in lista:
            if k==element[0]:
                data[k]=element[1]
    if isinstance(v, dict):
        data=v
        replace_dict(data,lista)

            
def choose_alternative(data):    
    new=toeigenvalue(data)
    while isinstance(new['Goal'], dict):    
        sumeigenvalue(new,lista)
        replace_dict(new,lista)
    i=0
    start=new['Goal'][0]
    for element in new['Goal']:
        if element >start:
            start=element
            i=i+1
    print(new['Goal'])
    print("Najlepszą opcją wedlug geo jest: {}".format(new['alternatives'][i]))




f=open('model.json', 'r')
data=json.load(f)
global lista
lista=[]
choose_alternative(data)
'''

'''# -*- coding: utf-8 -*-

import json
import math
import numpy as np
from numpy import linalg as LA

def toeigenvalue(data):
    for k, v in data.items():
        if isinstance(v, dict):
            toeigenvalue(v)
        else:
            if k!='alternatives':
                sqrt=int(math.sqrt(len(v)))
                v=np.asmatrix(v)
                v=v.reshape(sqrt,sqrt)
                v=LA.eig(v)
#                print(v)
                a=v[0][0]
                i=0
                for value in v[0]:
                    if value>a:
                        a=value
                        i=i+1
                vector=v[1][0:sqrt,i]
                v=(vector.T).tolist()
                lista=[]
                for x in v:
                    for y in x:
                        lista.append(y)
                print(lista[-1])
                z=0
                while z < len(lista):
                    lista[z]=lista[z]/lista[-1]
                    z=z+1
                lista=np.asarray(lista)
                data[k]=lista
    return data

def sumeigenvalue(data,lista):
    for k, v in data.items():
        if isinstance(v, dict):
           global parent_k
           global finalvector
           finalvector=0
           parent_k=k
           sumeigenvalue(v,lista)
        else:
            if k!='alternatives':
                if k=='matrix':
                    finalvector=0
                    i=0
                    critvector=v
                else:
                    finalvector=finalvector+critvector[i]*v
                    i=i+1
                    if i==critvector.size:
                        lista.append((parent_k, finalvector))
            
def replace_dict(data,lista):
    for k,v in data.items():
        for element in lista:
            if k==element[0]:
                data[k]=element[1]
    if isinstance(v, dict):
        data=v
        replace_dict(data,lista)

            
def choose_alternative(data):    
    new=toeigenvalue(data)
    global lista
    lista=[]
    while isinstance(new['Goal'], dict):    
        sumeigenvalue(new,lista)
        replace_dict(new,lista)
    i=0
    start=new['Goal'][0]
    for element in new['Goal']:
        if element >start:
            start=element
            i=i+1
    print(new['Goal'])
    print("Najlepszą opcją jest wdl eigen jest: {}".format(new['alternatives'][i]))




f=open('dane.json', 'r')
data=json.load(f)
choose_alternative(data)
'''

    return 0

decode_reszte(data["obiad"])

