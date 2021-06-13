def pixlev(r,g,b,per):
    if r+r*per/100 <=255:
        r=r+r*per/100
    else:
        r=255
    if g+g*per/100 <=255:
        g=g+g*per/100
    else:
        g=255
    if b+b*per/100 <=255:
        b=b+b*per/100
    else:
        b=255
    return r,g,b

def ymin(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0: 
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centery=centery-1
    return im

def xmax(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0:
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx+1
    return im

def xmin(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0 :
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx-1
    return im

def ymax(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0  :     
            r,g,b=im[centery,centerx]    
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centery=centery+1
    return im

def yminxmax(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0  :
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx+1
            centery=centery-1
    return im

def xminymax(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0  :
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx-1
            centery=centery+1
    return im

def xminymin(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0  :
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx-1
            centery=centery-1
    return im


def xmaxymax(im,centerx,centery,per):
    for i in range(0,per):
        per=per-1
        if per>=0  :
            r,g,b=im[centery,centerx]
            r,g,b=pixlev(r,g,b,per)
            im[centery,centerx]=[r,g,b] 
            centerx=centerx+1
            centery=centery+1
    return im
