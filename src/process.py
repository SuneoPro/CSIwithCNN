import numpy as np
import pandas as pd# 读数据函数
# testee为被测试者代号 有arc ctj lky
# dType为数据类型 有Mag和Phase
def ReadData(testee, dType, fileNum):
    dataList = list()
    for i in range(0, fileNum):
        fileName = 'D' + str(i)
        pathName = 'data/' + testee + '/' + dType + '/' + fileName +".csv"
        data = pd.read_csv(pathName, header = None)
        dataList.append(data)
    #print(len(dataList))
    #print(dataList[50])
    return dataList

arcMag = ReadData('arc', 'Mag', 351)
ctjMag = ReadData('ctj', 'Mag', 162)
lkyMag = ReadData('lky', 'Mag', 350)

dataMag = list()

def dataMagPre(dataName):
    l = len(dataName)
    for i in range(0, l):
        rowL = dataName[i].shape[1]
        if rowL < 500:
            continue
        else:
            temp = np.array(dataName[i])[:,:500]
            dataMag.append(temp)
            
dataMagPre(arcMag)

dataMagPre(ctjMag)

dataMagPre(lkyMag)

dataMagArray = np.array(dataMag)

tmp1 = np.zeros((341,1))
tmp2 = np.zeros((162,1)) + 1
tmp3 = np.zeros((328,1)) + 2
labelsArray = np.append(tmp1, (np.append(tmp2, tmp3, axis = 0)), axis = 0)

for i in range(0, 831):
    for j in range(0, 57):
        for k in range(0, 500):
            if dataMagArray[i, j, k] > 356:
                dataMagArray[i, j, k] = 356

mi = ma = dataMagArray[0, 0, 0]

for i in range(0, 831):
    for j in range(0, 57):
        for k in range(0, 500):
            if dataMagArray[i, j, k] < mi:
                mi = dataMagArray[i, j, k]
            if dataMagArray[i, j, k] > ma:
                ma = dataMagArray[i, j, k]
                
NdataMagArray=np.zeros((1662,57,250))

xxx=0

for i in range(0,1662):
    xxx=int(i/2)
    for j in range(0,57):
        if i%2==0:
            for k in range(0,250):
                NdataMagArray[i,j,k]=dataMagArray[xxx,j,k]
        if i%2==1:
            for k in range(250,500):
                NdataMagArray[i,j,k-250]=dataMagArray[xxx,j,k]
                
dataMagArray=NdataMagArray
