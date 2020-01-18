from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
#from django.http import Http404
import random

from cpa_api_home.mes_algos import quick_hull_algo, ritter_algo,convexe_algo

list1X = [77, 113, 94, 101, 88, 93, 77, 95, 139, 102, 47, 145, 67, 153, 130, 79, 126, 158, 158, 89, 70, 129, 136, 104, 133, 116, 141, 132, 132, 121, 101, 98, 143, 47, 124, 104, 79, 52, 100, 132, 83, 58, 146, 40, 155, 134, 91, 130, 89, 120, 69, 53, 138, 71, 151, 62, 145, 87, 78, 68, 130, 99, 44, 147, 59, 89, 149, 122, 150, 61, 84, 151, 108, 46, 144, 47, 55, 50, 138, 75, 99, 158, 48, 103, 111, 121, 78, 45, 101, 136, 134, 130, 51, 128, 117, 59, 130, 52, 107, 132, 102, 40, 48, 130, 149, 120, 41, 119, 82, 156, 121, 114, 139, 48, 128, 139, 80, 49, 80, 143, 148, 87, 86, 70, 45, 111, 146, 117, 159, 42, 145, 159, 151, 44, 77, 70, 83, 124, 68, 93, 70, 158, 121, 101, 119, 96, 51, 63, 83, 86, 65, 75, 109, 123, 73, 132, 92, 40, 47, 126, 68, 66, 81, 54, 109, 157, 72, 63, 68, 154, 68, 142, 123, 97, 54, 84, 81, 52, 100, 70, 57, 107, 60, 93, 83, 135, 71, 83, 147, 146, 81, 88, 92, 119, 104, 130, 61, 102, 93, 153]
list1Y = [89, 36, 141, 154, 164, 169, 109, 167, 119, 137, 139, 147, 48, 104, 153, 75, 134, 45, 67, 36, 160, 54, 145, 87, 68, 168, 42, 95, 144, 44, 136, 138, 38, 163, 52, 119, 127, 88, 85, 157, 133, 123, 138, 154, 46, 161, 112, 122, 59, 37, 75, 78, 147, 100, 116, 108, 83, 54, 43, 111, 59, 167, 138, 108, 144, 152, 102, 163, 147, 155, 152, 164, 42, 156, 75, 35, 101, 113, 162, 92, 154, 54, 55, 72, 123, 68, 125, 162, 148, 92, 107, 95, 157, 143, 115, 151, 144, 74, 73, 152, 140, 53, 142, 96, 88, 65, 125, 149, 58, 51, 45, 132, 138, 131, 159, 140, 121, 138, 142, 89, 47, 96, 89, 169, 140, 137, 55, 72, 146, 106, 76, 118, 74, 125, 150, 148, 105, 145, 107, 38, 112, 88, 61, 91, 152, 162, 108, 101, 131, 48, 152, 46, 81, 100, 145, 83, 91, 58, 88, 43, 90, 75, 155, 158, 118, 123, 130, 123, 48, 132, 34, 88, 73, 94, 91, 160, 149, 142, 126, 42, 36, 146, 115, 145, 105, 34, 63, 56, 90, 134, 61, 96, 82, 66, 142, 113, 168, 138, 53, 95]
liste1 = []
for i in range(0,len(list1X)):
    liste1.append([list1X[i],list1Y[i]])
list2X = [124, 93, 132, 162, 144, 116, 140, 169, 166, 63, 128, 154, 35, 86, 95, 88, 48, 60, 99, 101, 166, 126, 93, 121, 112, 178, 59, 35, 148, 93, 182, 164, 177, 111, 72, 50, 111, 40, 49, 52, 32, 181, 177, 178, 52, 123, 146, 78, 137, 78, 145, 54, 171, 128, 118, 99, 139, 83, 163, 136, 65, 85, 108, 163, 103, 37, 49, 69, 49, 89, 67, 134, 115, 149, 84, 162, 165, 91, 93, 148, 179, 139, 166, 181, 145, 132, 119, 89, 40, 165, 167, 180, 31, 163, 184, 112, 127, 126, 87, 117, 52, 128, 158, 81, 146, 91, 36, 131, 85, 178, 52, 176, 121, 170, 65, 174, 131, 123, 173, 118, 45, 158, 95, 77, 178, 163, 188, 74, 121, 112, 135, 81, 87, 95, 43, 114, 38, 131, 118, 186, 71, 149, 135, 58, 99, 164, 169, 151, 163, 157, 62, 95, 137, 86, 114, 127, 70, 53, 126, 159, 34, 69, 46, 117, 134, 90, 148, 91, 128, 120, 39, 66, 37, 99, 76, 167, 31, 50, 60, 108, 131, 125, 47, 86, 184, 99, 70, 60, 148, 141, 161, 151, 59, 78, 172, 51, 131, 67, 76, 108, 59, 154, 182, 118, 125, 128, 176, 181, 158, 177, 83, 60, 133, 161, 55, 83, 99, 171, 77, 95, 122, 76, 90, 143, 40, 178, 96, 188, 60, 98, 137, 110, 145, 87, 54, 83, 61, 179, 69, 106, 170, 122, 99, 98, 178, 178, 157, 73, 108, 121, 58, 38, 101, 30, 130, 187, 51, 85, 32, 144, 107, 183, 97, 162, 41, 41, 166, 121, 96, 129, 47, 185, 122, 67, 173, 135, 42, 117, 140, 71, 96, 160, 114, 160, 87, 104, 159, 94, 156, 35, 163, 63, 174, 70, 156, 70, 55, 175, 123, 64]
list2Y = [113, 153, 182, 102, 135, 84, 104, 45, 77, 203, 132, 111, 83, 111, 64, 64, 109, 205, 71, 179, 158, 215, 55, 26, 113, 192, 98, 113, 135, 212, 211, 208, 177, 166, 119, 190, 51, 132, 181, 31, 134, 163, 204, 72, 219, 148, 205, 160, 97, 219, 100, 83, 105, 148, 184, 41, 99, 117, 158, 105, 138, 173, 112, 79, 198, 161, 182, 59, 112, 189, 201, 205, 108, 205, 151, 216, 188, 219, 181, 162, 47, 47, 86, 216, 28, 177, 55, 40, 183, 209, 37, 50, 95, 43, 113, 51, 52, 207, 190, 78, 123, 124, 187, 178, 124, 106, 97, 218, 79, 199, 144, 137, 188, 101, 114, 152, 106, 121, 126, 104, 188, 164, 204, 105, 65, 54, 29, 194, 215, 74, 198, 103, 212, 194, 86, 44, 187, 68, 194, 106, 206, 24, 165, 124, 51, 40, 61, 66, 156, 154, 67, 136, 158, 24, 215, 179, 97, 78, 184, 202, 70, 198, 46, 125, 59, 134, 179, 121, 112, 145, 29, 73, 152, 197, 59, 121, 124, 202, 112, 201, 167, 170, 25, 72, 149, 69, 119, 218, 142, 204, 134, 160, 98, 42, 47, 179, 120, 125, 141, 130, 192, 149, 160, 180, 198, 147, 158, 42, 42, 91, 76, 25, 195, 43, 199, 80, 41, 152, 66, 39, 71, 198, 59, 68, 200, 183, 32, 33, 171, 43, 37, 59, 189, 34, 126, 179, 90, 198, 20, 55, 47, 193, 130, 126, 56, 88, 88, 119, 140, 28, 92, 84, 151, 35, 83, 38, 29, 117, 147, 120, 25, 33, 30, 172, 200, 179, 113, 60, 193, 144, 142, 144, 210, 110, 92, 76, 56, 46, 78, 117, 187, 160, 161, 65, 63, 155, 117, 191, 23, 25, 104, 53, 90, 98, 126, 92, 134, 92, 62, 21]
liste2 = []
for i in range(0,len(list2X)):
    liste2.append([list2X[i],list2Y[i]])

liste3 = [[79, 65], [86, 117], [113, 88], [141, 55], [128, 82], [122, 68], [84, 100], [142, 96], [99, 107], [110, 41], [87, 77], [149, 46], [63, 45], [56, 50], [123, 36]]
liste3X = []
liste3Y = []

res = []




def index(request):
    return render (request, 'base.html')


def generate(request,string):
    l = liste1
    print(string)
    if(string == "list1"):
        print("dans if list1************ {}".format(string))
        l = liste1
    elif( string == "list2"):
        print("dans if ***********list2********** {}".format(string))
        l = liste2
    elif( string == "list3"):
        print("dans if *******list3****** {}".format(string))
        l = liste3
    elif (isinstance(int(string), int)): 
        print("dans if avec nombre ****** {}".format(string))
        l = generate_points(int(string))

  
    return render(request, 'generate.html',{'points': l, 'list':res})

def generate_points(nbr):
    radius = 200
    rangeX = (15, 150)
    rangeY = (20, 80)
    qty = int(nbr)  

    points = []
    i = 0
    while i<qty:
        point = []
        point.append(random.randrange(*rangeX))
        point.append(random.randrange(*rangeY))
        points.append(point)
        i += 1

    return points


def get_points(request,nbr):
    points = generate_points(nbr)
    return render(request, 'generate.html',{'points': points})


def quickHull(request,string='list1'):
    l = liste1
    print(string)
    if(string == "list1"):
        print("dans if list1************ {}".format(string))
        l = liste1
    elif( string == "list2"):
        print("dans if ***********list2********** {}".format(string))
        l = liste2
    elif( string == "list3"):
        print("dans if *******list3****** {}".format(string))
        l = liste3
    elif (isinstance(int(string), int)): 
        print("dans if avec nombre ****** {}".format(string))
        l = generate_points(int(string))

    res = quick_hull_algo(l)
    return render(request, 'quickhull.html',{'points': l, 'list':res})
    

def ritter(request,string='list1'):
    l = liste1
    print(string)
    if(string == "list1"):
        print("dans if list1************ {}".format(string))
        l = liste1
    elif( string == "list2"):
        print("dans if ***********list2********** {}".format(string))
        l = liste2
    elif( string == "list3"):
        print("dans if *******list3****** {}".format(string))
        l = liste3
    elif (isinstance(int(string), int)): 
        print("dans if avec nombre ****** {}".format(string))
        l = generate_points(int(string))

    res = ritter_algo(l)
    
    return render(request, 'ritter.html',{'points': l, 'list':res})
    

def convexe(request,string='list1'):
    l = liste1
    print(string)
    if(string == "list1"):
        print("dans if list1************ {}".format(string))
        l = liste1
    elif( string == "list2"):
        print("dans if ***********list2********** {}".format(string))
        l = liste2
    elif( string == "list3"):
        print("dans if *******list3****** {}".format(string))
        l = liste3
    elif (isinstance(int(string), int)): 
        print("dans if avec nombre ****** {}".format(string))
        l = generate_points(int(string))

    res = convexe_algo(l)
    ress = []
    for i in res:
        re = []
        re.append(i[0])
        re.append(i[1])
        ress.append(re)
    
    
    return render(request, 'quickhull.html',{'points': l, 'list':ress})