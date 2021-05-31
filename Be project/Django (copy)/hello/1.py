import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns


#set the style for seaborn
sns.set_style('darkgrid')

st.title(' Data Visualiztion Dashboard');

@st.cache
def load_data(nrows):
    data = pd.read_csv("final.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


global numeric_columns
try:
	numeric_columns=data.select_dtypes(['float64','float32','int32','int64']).columns
	print(numeric_columns)
except Exception as e:
	print(e)
	st.write(" please upload file to the apploication .")

#selector
st.sidebar.title("selector")

#type of graph
visualisation=st.sidebar.selectbox('select a chart type',('scatterplot','Pie Chart','Line chart','Barchart','Area Chart','Histogram','jointplot'))

# create scatterplot
if visualisation=='scatterplot':
	select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
	print(select_box1)
	select_box2=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	#scatter=sns.relplot(x=select_box1,y=select_box2,data=data)
	plot=px.scatter(data_frame=data,x=select_box1,y=select_box2)
	st.plotly_chart(plot)

#create pie chart	
elif visualisation=='Pie Chart':

	fig=px.pie(data,values='Avg',names='Year',title='Pie Chart')  #work to be completed
	fig.show()

#create a line chart 	
elif visualisation=='Line chart':
	st.title("Line Chart")
	st.line_chart(data)

#create a bar chart
elif visualisation=='Barchart':
	#select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
	#select_box2=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	#st.bar_chart(data)
	#ax=sns.barplot(x=select_box1,y=select_box2,data=data)
	#st.pyplot(ax)
	#select_box5=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	st.title("Bar graph")
	fig=px.bar(data,x='runs',y='year',width=800,height=400)
	fig.show()

#create a area chart
elif visualisation=='Area Chart':
	st.title("Area chart")
	st.area_chart(data)

#create a histogram
elif visualisation=='Histogram':
	st.title("Histogram")
	select_box=st.sidebar.selectbox(label='feature',options=numeric_columns)
	histogram_slider=st.sidebar.slider(label="Number of Bins",min_value=5,max_value=100, value=30)
	sns.displot(data[select_box], bins=histogram_slider)
	st.pyplot()

#create a join plot
elif visualisation=='jointplot':
	st.title("jointplot")
	select_box4=st.sidebar.selectbox(label='x axis',options=numeric_columns)
	select_box5=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	print(select_box4)
	sns.jointplot(x=select_box4,y=select_box5,data=data)
	st.pyplot()
	st.set_option('deprecation.showPyplotGlobalUse', False)

	
	#fig=plt.hist(select_box3,bins=20 ,color ='green')
elif visualisation	== 'MIX CHART':
	select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
	select_box4=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	select_box9=st.sidebar.selectbox(label='z axis',options=numeric_columns)
	hist_data =[select_box1,selectbox4,select_box9]
	group_labels=['group 1','group 2','group 3']
	fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
	st.plotly_chart(fig, use_container_width=True)


	
	



#try n Error
#col=st.sidebar.selectbox("Select a column",data.columns)
#visualisation=st.sidebar.selectbox('select a chart type',('Bar Chart','Pie Chart','Line chart'))
#selected_country=data[data['noc']==country_select]
#st.markdown("## **country Level analysis**")

#visualisation=="Bra Chart":
#st.bar_chart(data)

#st.title("Bar graph")
#st.bar_chart(data)
#st.line_chart(data)

#fig=px.pie(data,values='total',names='noc',title='Pie Chart')
#fig.show()
#fig=px.bar(data,x='noc',y='total')
#fig.show()
#hm=sns.heatmap(data=data)
#plt.show(hm)
#def get_total_dataframe(df):
	#total_dataframe=pd.DataFrame({
	#'position':['gold','silver','Bronze'],
	#'total':(data.iloc[0]['gold'],
	#data.iloc[0]['silver'],data.iloc[0]['bronze'])})
	#return total_dataframe
#country_total=get_total_dataframe(selected_country)	
#if visualisation=='Bar chart' :
	#state_total_graph=px.bar(country_total,x="Name of country",y="count")
	#st.plotly_chart(state_total_graph)
#if visualisation=='line chart' :
	#state_total_graph=px.bar(country_total,x="Name of country",y="count")
	#st.plotly_chart(state_total_graph)
#if visualisation=='pie chart' :
	#state_total_graph=px.bar(country_total,x="Name of country",y="count")
	#st.plotly_chart(state_total_graph)	