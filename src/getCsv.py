from picoscenes import  Picoscenes
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

PERSON="lky"
KIND="Phase"
#

path='./'+PERSON
path_list=os.listdir(path)
path_list.sort(key=lambda x:int(x[13:18]))

flag=0
for filename in path_list:
    nameD="./data/"+PERSON+"/"+KIND+"/"+"D"+str(flag)+".csv"
    with open(nameD,mode="w",encoding="utf-8-sig",newline="") as f:
        writer=csv.writer(f)
        tmpN=path+"/"+filename
        frames = Picoscenes(tmpN)
        aPacket=len(frames.raw)
        ePacket=[]
        for i in range(0,aPacket-1):
            if(frames.raw[i].get("RxSBasic").get("timestamp")==0 ): 
                ePacket.append(i)
        for n in range(0,114,2):
            mags=np.zeros(len(ePacket))
            x=0
            for i in ePacket:
                mags[x]=round(frames.raw[i].get("CSI").get(KIND)[n],4)
                x=x+1
            writer.writerow(mags)
    flag=flag+1
        
            

