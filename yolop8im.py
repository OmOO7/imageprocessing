import numpy as np
import cv2
from darkflow.net.build import TFNet
#import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
#%config InlineBackend.figure_format-'jpg'
#image 2 class using pillar and car
options = {
        'model': 'cfg/yolov2-tiny-voc-2c.cfg',
        'load':1060,
        'threshold': 0.4,
        'gpu':1.0
        }

tfnet = TFNet(options)

img = cv2.imread("line37.jpg")
#img = cv2.imread("line37.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result=tfnet.return_predict(img)
print(result)

A_br_x = []
A_br_y = []
A_bl_x = []
A_bl_y = []


for i in range(0,len(result)):
    #if(result[i]['confidence']>0.544444):
    t1=(result[i]['topleft']['x'],result[i]['topleft']['y'])
    t2=(result[i]['bottomright']['x'],result[i]['bottomright']['y'])
    br_x=(result[i]['bottomright']['x'])
    br_y=(result[i]['bottomright']['y'])
    bl_x=(result[i]['topleft']['x'])
    bl_y= br_y
    
    A_br_x=np.append(A_br_x,br_x)
    A_br_y=np.append(A_br_y,br_y)
    A_bl_x=np.append(A_bl_x,bl_x)
    A_bl_y=np.append(A_bl_y,bl_y)
    
    
    
    t_x=0
    t_y=0
    p_x=0
    p_y=0
    
    label=result[i]['label']
    x=0
    A_br_x=pd.Series(A_br_x)
    A_br_y=pd.Series(A_br_y)
    A_bl_x=pd.Series(A_bl_x)
    A_bl_y=pd.Series(A_bl_y)


    DF= pd.DataFrame([A_br_x,A_br_y,A_bl_x,A_bl_y])

    DF_pillar = pd.DataFrame([A_bl_x,A_br_x])
    
    DF_truck = pd.DataFrame([A_bl_x,A_br_x])
    '''
    if label=="pillar":
        p_min=min(DF.iloc[0][0:])
        p_max=max(DF.iloc[2][0:])
        #print(p_min)
        #print(DF)
        print("max",DF_pillar.iloc[0][0:].max())
        print("min",DF_pillar.iloc[1][0:].min())
        
        p_br_x = DF_pillar.iloc[0][0:].max()
        p_bl_x = DF_pillar.iloc[1][0:].min()
        
    if label == "truck":
        print(DF)
        #print(DF_truck)
        print(DF_truck.iloc[0][0:].min())
        print(DF_truck.iloc[1][0:].max())
        t_bl_x = DF_truck.iloc[0][0:].min()
        t_br_x = DF_truck.iloc[1][0:].max()
        '''
    '''
    if label=="pillar":
        n = []
        for i in range((len(result))):
            n=np.max(br_y)
            x=x+1
        label="pillar"+str(x)
            #print(label)
            #e= np.max(n[i])
         
        print("br_y",n)
    '''
    img= cv2.rectangle(img,t1,t2,(0,255,0),7)
    img=cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,2),2)
    
       
#print(min(DF.iloc[0][0:]))

#print(max(DF.iloc[2][0:]))
p_br_x = 0
p_bl_x  =0

'''       
if t_bl_x > p_bl_x and  t_br_x < p_br_x :
    print("true")
else:
    print("false")
    #print(p_max)
    '''






        
        
        
        #t_x=x_x
        #t_y=x_y
        
    #if label=="pillar":
        
        
        #for i in range((len(result))):
            #n = 0
             #b =x_y
            # c.insert(n,x_y)
               
             #n+1
        
             
             
             #a=collections.Counter(c)
             #print("A",a)
             #for j in a
             
             
        
            
        
            
        #print("b",b)
        
        
           


plt.imshow(img)
plt.show()

        



    #if(result[i]['confidence']>0.544444):
