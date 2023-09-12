from io import BytesIO
import matplotlib.pyplot as plt 
import base64
from io import BytesIO
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime
# from .utils import getplot
import re


def get_graph():
    buffer=BytesIO()
    buffer1=BytesIO()
    plt.savefig(buffer,format='png')
    plt.figure(facecolor='#ffffff')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    plt.clf()
  
    
    return graph
    

def getplot(df,per):
    k=0
    columnsplot=["date_count","date_pie","time_count","time_pie","day_count","day_pie","user_count","user_pie"]
    data={}
    
    plt.switch_backend("AGG")
    # userdata 
    # userpercent=df['user'].value_counts(normalize=True)*100
    # usercount=df['user'].value_counts()
    # usercount[userpercent>2.5].plot(kind="pie",autopct="%0.1f%%")
    # graph=get_graph()
    
    for i in df.columns:
        if i=="message":
            break
        count_percent=df[i].value_counts(normalize=True)*100
        count=df[i].value_counts()
    
        # plt.figure(figsize=(6, 10))
        # plt.figure(facecolor='white')
        plt.subplots_adjust(bottom=0.3)
        plt.title(i)
        
        
        
        # correctiondnndsndnsd
        if len(count[count_percent>per])>0:
            count[count_percent>per].plot(kind='bar')
        # else:
        #     count.plot(kind='bar')
            
            
        
        # plt.ylabel(i)
        
        
        graph=get_graph()
       
        
        data[columnsplot[k]]=graph

        
        k=k+1
        plt.title(i)
        
        if len(count[count_percent>per])>0:
            count[count_percent>per].plot(kind='pie',autopct="%0.1f%%")
        # else:
        #     count.plot(kind='bar')
        
        
        # count[count_percent>2.5].plot(kind='pie',autopct="%0.1f%%")
        
        graph=get_graph()
        
        # print(k)
        data[columnsplot[k]]=graph
        k=k+1
        
        
        
        
    
    
    
    
    
    return data







def message_to_df(file):
            # data=file
            data=file.read()
            data=data.decode('utf-8')
            
            
            

            datetime_pattern= r'\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2} - '
            date_time=re.findall(datetime_pattern,data)
            date=[]
            time=[]
            for i in date_time:
                date.append(i.split(",")[0])
                time.append(i.split(",")[1].replace("-","").replace(" ",""))
                
            
            df=pd.DataFrame({"date":date,"time":time})
            df['date']=pd.to_datetime(df['date'])
            df['day']=df['date'].dt.day_name()
            df['time']=pd.to_datetime(df['time'],format="%H:%M")
            df['date']=df['date'].dt.date
            df['time']=df['time'].dt.hour
            splitted_data=re.split(datetime_pattern,data)[1:]
            
            name=[]
            for i in splitted_data:
                match=re.search( r'(.+):',i)
                if (match):

                    name.append(match.group(1).split(":")[0].strip())
                else:
                    name.append("notification")
                    
            namedf=pd.DataFrame(name)
            df=pd.merge(df,namedf,right_index=True,left_index=True)
            df.rename(columns={0:"user"},inplace=True)
            
            # extracting the message
            message_pattern=r': ((?:(?!\([^)]*\)).)*)$'
            message=[]
            for i in splitted_data:
                message.append(re.split( r'(.+):',i)[-1])
                
            message_dataframe=pd.DataFrame({"message":message})
            df=pd.merge(df,message_dataframe,right_index=True,left_index=True)
            graph=getplot(df,2.5)
            # print(df)
            
            
            return graph,df
            
            
            
            
def databasedonhtml(userdata,file):
    data=file.read()
    data=data.decode('utf-8')
    
    datetime_pattern= r'\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2} - '
    date_time=re.findall(datetime_pattern,data)
    date=[]
    time=[]
    for i in date_time:
        date.append(i.split(",")[0])
        time.append(i.split(",")[1].replace("-","").replace(" ",""))
        
        
    df=pd.DataFrame({"date":date,"time":time})
    df['date']=pd.to_datetime(df['date'])
    df['day']=df['date'].dt.day_name()
    df['time']=pd.to_datetime(df['time'],format="%H:%M")
    df['date']=df['date'].dt.date
    df['time']=df['time'].dt.hour
    splitted_data=re.split(datetime_pattern,data)[1:]
    
    # print(df['date'])
    
    # df['date'] = df['date'].str.replace('.', '')
    
    name=[]
    for i in splitted_data:
        match=re.search( r'(.+):',i)
        if (match):

            name.append(match.group(1).split(":")[0].strip())
        else:
            name.append("notification")
            
    namedf=pd.DataFrame(name)
    df=pd.merge(df,namedf,right_index=True,left_index=True)
    df.rename(columns={0:"user"},inplace=True)
    
    # extracting the message
    message_pattern=r': ((?:(?!\([^)]*\)).)*)$'
    message=[]
    for i in splitted_data:
        message.append(re.split( r'(.+):',i)[-1])
        
    message_dataframe=pd.DataFrame({"message":message})
    df=pd.merge(df,message_dataframe,right_index=True,left_index=True)
    
    # df['date'] = df['date'].str.replace('.', '')
    
    # print(userdata)
    keytoremove=[]
    for i in userdata.keys():
        if userdata[i]=='':
            keytoremove.append(i)
    
    for i in keytoremove:
        # df.drop(columns=i)
        userdata.pop(i)
    
    # print(userdata)
    
    
    newdf=pd.DataFrame()
    for key,value in userdata.items():
        if key=='date':
            date_format = '%Y-%m-%d'
            date_object = datetime.strptime(userdata[key], date_format)
            # userdata[key]=userdata[key].replace('.','')
            # it show the problem in sept so 
            
            
            # print(userdata[key])
            # date_object = datetime.strptime(userdata[key], "%b %d, %Y")
            # print(date_object.date())
            # newdf=df[df["date"]==date_object.date()]
            userdata[key]=date_object.date()
        elif key=="time":
            time1=int(userdata[key])
            # newdf=df[df["time"]==time1]
            
            userdata[key]=time1
            # print(userdata)
        else:
            pass
            # print(value)
            # newdf=df[df[key]==value]
                
        
    
    # print(newdf)
    putthesedata=list(userdata.items())
    # print(putthesedata)
    print(len(putthesedata))
    
    if len(putthesedata)==1:
        key=putthesedata[0][0]
        value=putthesedata[0][1]
        newdf=df[df[key]==value]
        
    elif len(putthesedata)==2:
        newdf=df[(df[putthesedata[0][0]]==putthesedata[0][1]) & (df[putthesedata[1][0]]==putthesedata[1][1])]
    
    elif len(putthesedata)==3:
        newdf=df[(df[putthesedata[0][0]]==putthesedata[0][1]) & (df[putthesedata[1][0]]==putthesedata[1][1]) &(df[putthesedata[2][0]]==putthesedata[2][1])]
    
    elif len(putthesedata)==4:
        newdf=df[(df[putthesedata[0][0]]==putthesedata[0][1]) & (df[putthesedata[1][0]]==putthesedata[1][1]) &(df[putthesedata[2][0]]==putthesedata[2][1]) & (df[putthesedata[3][0]]==putthesedata[3][1])]
    
    
    graph=getplot(newdf,0)

    
   
        
       
            
        
    

    
    

    
    
    return df,newdf,graph
    

    
    
    
    
    
    
    
    
    
    
    
    








    
    
    
    
    
    
    
    
    
    