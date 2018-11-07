# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:54:51 2018

@author: Anshit Vishwakarma
"""

import cv2
import numpy as np
from pynput.mouse import Button, Controller
import wx
mouse=Controller()

app=wx.App(False)
(sx,sy)=wx.GetDisplaySize()
(camx,camy)=(320,240)

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])

cam=cv2.VideoCapture(0)
cam.set(3,camx)
cam.set(4,camy)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

mLocOld=np.array([0,0])
mouseLoc=np.array([0,0])
DampingFactor=2
#mouseLoc=mLocOld+(targetLoc-mLocOld)/DampingFactor

pinchFlag=0

while True:
    ret, img=cam.read()
    
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(imgHSV,lowerBound,upperBound)
    
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    
    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    if(len(conts)==2):
        if (pinchFlag==1):
            pinchFlag=0
            mouse.release(Button.left)
        x1,y1,w1,h1=cv2.boundingRect(conts[0])
        x2,y2,w2,h2=cv2.boundingRect(conts[1])
        x1=int(x1)
        y1=int(y1)
        x2=int(x2)
        y2=int(y2)
        h1=int(h1)
        h2=int(h2)
        w1=int(w1)
        w2=int(w2)
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        cx1=x1+w1/2
        cy1=y1+h1/2
        cx2=x2+w2/2
        cy2=y2+h2/2
        cx1=int(cx1)
        cx2=int(cx2)
        cy1=int(cy1)
        cy2=int(cy2)
        cv2.line(img, (cx1,cy1),(cx2,cy2),(255,0,0),2)
        cx=(cx1+cx2)/2
        cy=(cy1+cy2)/2
        cx=int(cx)
        cy=int(cy)
        cv2.circle(img, (cx,cy),2,(0,0,255),2)
        mouseLoc=mLocOld+((cx,cy)-mLocOld)/DampingFactor
        mouse.position=(int(sx-(mouseLoc[0]*sx/camx)),int(mouseLoc[1]*sy/camy))
        while mouse.position!=(int(sx-(mouseLoc[0]*sx/camx)),int(mouseLoc[1]*sy/camy)):
            pass
        mLocOld=mouseLoc
        
    elif(len(conts)==1):
        if (pinchFlag==0):
            pinchFlag=1
            mouse.press(Button.left)
        x,y,w,h=cv2.boundingRect(conts[0])
        x=int(x)
        y=int(y)
        w=int(w)
        h=int(h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx=x+w/2
        cy=y+h/2
        cx=int(cx)
        cy=int(cy)
        cv2.circle(img,(cx,cy),int((w+h)/4),(0,0,255),2)
        mouseLoc=mLocOld+((cx,cy)-mLocOld)/DampingFactor
        mouse.position=(int(sx-(mouseLoc[0]*sx/camx)),int(mouseLoc[1]*sy/camy))
        while mouse.position!=(int(sx-(mouseLoc[0]*sx/camx)),int(mouseLoc[1]*sy/camy)):
            pass
        mLocOld=mouseLoc
        
    
    
    #cv2.imshow("maskClose",maskClose)
    #cv2.imshow("maskOpen",maskOpen)
    #cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(5)
    