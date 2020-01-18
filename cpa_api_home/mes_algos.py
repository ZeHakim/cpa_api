from math import *
import math
import numpy

def distance(a,b):   
    sq1 = (a[0]-b[0])*(a[0]-b[0])
    sq2 = (a[1]-b[1])*(a[1]-b[1])
    return math.sqrt(sq1 + sq2)
    
def ritter_algo(points):
    if (len(points)<1): return []
    rest = points.copy()
    dummy = points[0]
    p = dummy.copy()
    for s in rest:
        if (distance(dummy,s) > distance(dummy,p)):
            p = s.copy()
    q = p.copy()
    for s in rest:
        if (distance(p,s) > distance(p,q)):
            q = s.copy()
    cX = 0.5*(p[0] + q[0])
    cY = 0.5*(p[1] + q[1])
    cRadius = 0.5*distance(p,q)
    rest.remove(p)
    rest.remove(q)
    while (len(rest) != 0):
        s=rest[0].copy()
        rest.remove(s)
        distanceFromCToS = sqrt((s[0]-cX)*(s[0]-cX)+(s[1]-cY)*(s[1]-cY))
        if (distanceFromCToS <= cRadius): continue
        
        cPrimeRadius = 0.5*(cRadius+distanceFromCToS)
        alpha = cPrimeRadius/distanceFromCToS
        beta = (distanceFromCToS-cPrimeRadius)/distanceFromCToS
        cPrimeX = alpha*cX+beta*s[0]
        cPrimeY = alpha*cY+beta*s[1]
        cRadius = cPrimeRadius
        cX = cPrimeX
        cY = cPrimeY
    
    return [[cX, cY],[cRadius]]
    

def triangle_contient_point(a,b,c,x):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]
    xp = x[0]
    yp = x[1]
    c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
    c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
    c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
    res = (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0)
    return (res) 

def cross_product(p, q,s,t):
    return ((q[0]-p[0])*(t[1]-s[1])-(q[1]-p[1])*(t[0]-s[0]))
  

def quick_hull_algo(points):
    if (len(points) < 4):
        return points

    ouest = points[0].copy()
    sud = points[0].copy()
    est = points[0].copy()
    nord = points[0].copy()

    for p in points:
        if (p[0]<ouest[0]): 
            ouest=p
        if (p[1]>sud[1]): 
            sud=p
        if (p[0]>est[0]): 
            est=p
        if (p[1]<nord[1]): 
            nord=p

    resultat = []
    resultat.append(ouest)
    resultat.append(sud)
    resultat.append(est)
    resultat.append(nord)

    rest = points.copy()
    restA = points.copy()
    for i in range(0,len(rest)):        
        if (triangle_contient_point(ouest,sud,est,rest[i]) or triangle_contient_point(ouest,est,nord,rest[i])):      
            el = rest[i]
            restA.remove(el)
            #i = i-1

    rest = restA.copy()
    
    for i in range(0,len(resultat)):
        a = resultat[i]
        b = resultat[(i+1)%len(resultat)]
        ref = resultat[(i+2)%len(resultat)]

        signeRef = cross_product(a,b,a,ref)
        maxValue = 0
        maxPoint = a

        for  p in points: 
            piki = cross_product(a,b,a,p)
            if (signeRef*piki<0 and abs(piki)>maxValue):
                maxValue = abs(piki)
                maxPoint = p
        if (maxValue!=0):
            restB = rest.copy()
            for j in range(0,len(rest)):
                if (triangle_contient_point(a,b,maxPoint,rest[j])):
                    el = rest[j]
                    rest.remove(el)
                    j = j-1

        resultat.insert(i+1,maxPoint)
        i = i-1
                
    return resultat
    if (len(points) < 4):
        return points

    ouest = points[0]
    sud = points[0]
    est = points[0]
    nord = points[0]

    for p in points:
        if (p[0]<ouest[0]): 
            ouest=p
        if (p[1]>sud[1]): 
            sud=p
        if (p[0]>est[0]): 
            est=p
        if (p[1]<nord[1]): 
            nord=p

    resultat = []
    resultat.append(ouest)
    resultat.append(sud)
    resultat.append(est)
    resultat.append(nord)

    rest = resultat.copy()
    for i in range(0,len(rest)):
        if (triangle_contient_point(ouest,sud,est,rest[i])) | triangle_contient_point(ouest,est,nord,rest[i]):
            el = rest[i]
            rest.remove(el)
            i = i-1
    
    for i in range(0,len(resultat)):
        a = resultat[i]
        b = resultat[(i+1)%len(resultat)]
        ref = resultat[(i+2)%len(resultat)]

        signeRef = cross_product(a,b,a,ref)
        maxValue = 0
        maxPoint = a

        for  p in points: 
            piki = cross_product(a,b,a,p)
            if (signeRef*piki<0 & abs(piki)>maxValue):
                maxValue = abs(piki)
                maxPoint = p
        if (maxValue!=0):
            for j in range(0,len(rest)):
              if (triangle_contient_point(a,b,maxPoint,rest[j])):
                  el = rest[j]
                  rest.remove(el)
                  j = j-1

              resultat.insert(i+1,maxPoint)
              i = i-1
                
    return resultat

def convexe_algo(points):
    sample = numpy.asarray(points, dtype=numpy.float32)
    link = lambda a,b: numpy.concatenate((a,b[1:]))
    edge = lambda a,b: numpy.concatenate(([a],[b]))

    def dome(sample,base): 
        h, t = base
        dists = numpy.dot(sample-h, numpy.dot(((0,-1),(1,0)),(t-h)))
        outer = numpy.repeat(sample, dists>0, axis=0)
            
        if len(outer):
            pivot = sample[numpy.argmax(dists)]
            return link(dome(outer, edge(h, pivot)),
                        dome(outer, edge(pivot, t)))
        else:
            return base

    if len(sample) > 2:
        axis = sample[:,0]
        base = numpy.take(sample, [numpy.argmin(axis), numpy.argmax(axis)], axis=0)
        return link(dome(sample, base),
                    dome(sample, base[::-1]))
    else:
        return sample.toliste()
    