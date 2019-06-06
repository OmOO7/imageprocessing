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
        'threshold': 0.20,
        'gpu':1.0
        }

tfnet = TFNet(options)






img = cv2.imread("d.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result=tfnet.return_predict(img)
print(result)

p_A_br_x = []
p_A_br_y = []
t_A_br_x = []
t_A_br_y = []





for i in range(0,len(result)):
    #if(result[i]['confidence']>0.544444):
    t1=(result[i]['topleft']['x'],result[i]['topleft']['y'])
    t2=(result[i]['bottomright']['x'],result[i]['bottomright']['y'])
    print(t1)
    print(t2)
    
    #A_bl_x=np.append(A_bl_x,bl_x)
    #A_bl_y=np.append(A_bl_y,bl_y)
   
    
    
    t_x=0
    t_y=0
    p_x=0
    p_y=0
    
    label=result[i]['label']
    x=0
        #print(p_max)
    if label=="pillar":
        br_x=(result[i]['bottomright']['x'])
        br_y=(result[i]['topleft']['x'])
        p_A_br_x=np.append(p_A_br_x,br_x)
        p_A_br_y=np.append(p_A_br_y,br_y)
        p_A_br_x=pd.Series(p_A_br_x)
        p_A_br_y=pd.Series(p_A_br_y)
   # A_bl_x=pd.Series(A_bl_x)
   # A_bl_y=pd.Series(A_bl_y)
        DF_pillar= pd.DataFrame([p_A_br_x,p_A_br_y])
        p_min=min(DF_pillar.iloc[0][0:])
        p_max=max(DF_pillar.iloc[1][0:])
        print(DF_pillar)
        pillar_b_x = DF_pillar.iloc[0][0:].min()
        pillar_b_y = DF_pillar.iloc[1][0:].max()
        print("pillar",DF_pillar.iloc[0][0:].min())
        print("pillar",DF_pillar.iloc[1][0:].max())
    if label == "truck":
        #p_min=min(DF.iloc[0][0:])
        #p_max=max(DF.iloc[1][0:])
        br_x=(result[i]['bottomright']['x'])
        br_y=(result[i]['topleft']['x'])
        t_A_br_x=np.append(t_A_br_x,br_x)
        t_A_br_y=np.append(t_A_br_y,br_y)
        t_A_br_x=pd.Series(t_A_br_x)
        t_A_br_y=pd.Series(t_A_br_y)
   # A_bl_x=pd.Series(A_bl_x)
   # A_bl_y=pd.Series(A_bl_y)
        DF_truck= pd.DataFrame([t_A_br_x,t_A_br_y])
        p_min=min(DF_truck.iloc[0][0:])
        p_max=max(DF_truck.iloc[1][0:])
        print(DF_truck)
        #print("pillar",DF_truck.iloc[0][0:].min())
        #print("pillar",DF_truck.iloc[1][0:].max())
        
        
        print("truck",DF_truck.iloc[0][0:].min())
        print("truck",DF_truck.iloc[1][0:].max())
        truck_b_x = DF_truck.iloc[0][0:].min()
        truck_b_y = DF_truck.iloc[1][0:].max()
        
        if truck_b_y > pillar_b_x and truck_b_x < pillar_b_y:
            print("br_x truck",truck_b_x)
            print("br_x pillar",pillar_b_x)
            print("br_y truck",truck_b_y)
            print("br_y pillar",pillar_b_y)
            print("true")
        else:
            print("false")
        
    
    
    img= cv2.rectangle(img,t1,t2,(0,255,0),7)
    img=cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,2),2)
   



       
#print(min(DF.iloc[0][0:]))

#print(max(DF.iloc[2][0:]))

'''
if label=="pillar":
        p_min=min(DF.iloc[0][0:])
        p_max=max(DF.iloc[1][0:])
        print(DF.iloc[0][0:].min())
        print(DF.iloc[1][0:].max())
if label == "truck":
        #p_min=min(DF.iloc[0][0:])
        #p_max=max(DF.iloc[1][0:])
        print(DF.iloc[0][0:].min())
        print(DF.iloc[1][0:].max())
      
'''


img= cv2.rectangle(img,t1,t2,(0,255,0),7)
img=cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,2),2)




        
        
        
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
