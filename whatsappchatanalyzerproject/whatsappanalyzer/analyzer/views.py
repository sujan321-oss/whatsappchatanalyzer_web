from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest

from io import BytesIO
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from .utils import getplot
from .utils import message_to_df,databasedonhtml
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from analyzer.models import WhatsAppFile


from pathlib import Path




import re



def uploadsection(request):
    graph={}
    response=""
    df=pd.DataFrame()
    if (request.method=="POST"):
        if 'file' in request.FILES:
            
            file=request.FILES['file']
            
          
            
            unique_identifier=str(uuid.uuid4())
            WhatsAppFile(file=file,uniqueidentifier=unique_identifier).save()
            
            
            response=redirect('analyze/')
            response.set_cookie("unique_identifier",unique_identifier)
            
            

            return response
            
             
    return render(request,'uploadsection.html')
    







def showthedata(request):
    df=""
    graph={}
    user=[]
    time=[]
    day=[]
    date=[]
    datafromhtml=[]
    user=time=day=date=''
  
    data=request.COOKIES.get("unique_identifier",None)
    # print(data)
    if (data==None):
        return redirect('/')
    else:
        if request.method=="POST":
            user=request.POST.get('user','')
            time=request.POST.get('time','')
            day=request.POST.get('day','')
            date=request.POST.get('date','')
            
        newdata=WhatsAppFile.objects.get(uniqueidentifier=data)
# if all the field are empty then show the all the graph
        if user=='' and time=='' and day=='' and date=='':
            # newdata=WhatsAppFile.objects.get(uniqueidentifier=data)
        # print(newdata.file)
            graph,df=message_to_df(newdata.file)
            user=df['user'].unique()
            time=df["time"].unique()
            day=df['day'].unique()
            df['date']=df['date'].apply(lambda x:x.strftime("%Y-%m-%d"))
            date=df['date'].unique()
            
#  if user select the any field show required graph
        else:
            # datafromhtml=[user,time,day,date]
            datafromhtml={"user":user,"time":time,"day":day,"date":date}
            
            
            # call the data based on html function
            # df option is used to show the option values if else condition satisfy
            df_option,df,graph=databasedonhtml(datafromhtml,newdata.file)
            # graph,df=message_to_df(newdata.file)
            
            # graph,newdf=message_to_df(newdata.file)
            user=df_option['user'].unique()
            time=df_option["time"].unique()
            day=df_option['day'].unique()
            df_option['date']=df_option['date'].apply(lambda x:x.strftime("%Y-%m-%d"))
            date=df_option['date'].unique()
            
        # print(df) 
        
            
            
       
            
            
        
        
        # print(user)
        
        
    

    return render(request,"optionpage.html",{"dataframe":df.to_html,"graph":graph,"user":user,"time":time,"date":date,"day":day,"date":date})






    







