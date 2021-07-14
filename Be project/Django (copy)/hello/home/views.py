from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from googlesearch import search 
import streamlit as st
import matplotlib.pyplot as plt 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns
from glob import glob
import os
# Create your views here.


def index(request):
	return render(request, 'index.html')

def external(request):
	context={}
	l1=[]
	count=1
	if(request.method) =='POST':
		query=request.POST['search']
		a=20
		for j in search(query, num=10, stop=a, pause=2):
			try:
				r= requests.get(j)
				htmlContent =r.content
				soup= BeautifulSoup(htmlContent,'html.parser')
				table=soup.find_all('table')
				if(str(len(table))!='0'):	
					l1.append(str(count)+".  "+j)
					count=count+1
					print(j)
			except:
				continue
					

				

		final_string = '\n'.join(l1)
		context['var']=final_string
		a1=1
		for j in search(query, num=10, stop=a, pause=2):
			try:
				a2=str(a1)
				a3=a2+".csv"
				r= requests.get(j)
				htmlContent =r.content
				soup= BeautifulSoup(htmlContent,'html.parser')
				table=soup.find_all('table')
				if(str(len(table))!='0'):	
					l1.append(str(count)+".  "+j)
					try:
						df=pd.read_html(j)
					except:
						continue
					for i in df:
						i.to_csv(a3)
					a1=a1+1
			except:
				continue
						
		"""
		stock_files=sorted(glob('*.csv'))
	pd.concat((pd.read_csv(file).assign(filename=file)for file in stock_files), ignore_index=True)
	df=pd.read_csv("1.csv")+pd.read_csv("2.csv")+pd.read_csv("2.csv")+pd.read_csv("3.csv")+pd.read_csv("4.csv")+pd.read_csv("5.csv")+pd.read_csv("6.csv")
	df.to_csv('final_data.csv')		
		"""
	return render(request, 'index.html', context)

def plot(request):
	
	os.system('cd -')
	os.system('streamlit run visual.py')	
	
	

