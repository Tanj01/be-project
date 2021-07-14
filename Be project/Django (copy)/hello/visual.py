import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns
import plotly.graph_objects as go
#import plotly.io as pio
#pio.templates

global data

#set the style for seaborn
sns.set_style('darkgrid')

st.title(' Data Visualiztion Dashboard')


st.sidebar.subheader("visualisation settings")
uploaded_file = st.sidebar.file_uploader(label="upload your csv or Excel file.",type=['csv','xlsx'])

#global data
if uploaded_file is not None:
	print(uploaded_file)
	try:
		data=pd.read_csv(uploaded_file)
	except	Exception as e:
		print(e)
		data=pd.read_excel(uploaded_file)
try:
	st.write(data)
except Exception as e:
	print(e)
	st.write("file not uploaded")

#def load_data(nrows):
    #data = pd.read_csv("C:/Users/akash/Desktop/iris.csv", nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #return data

#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done! (using st.cache)")

#if st.checkbox('Show raw data'):
    #st.subheader('Raw data')
    #st.write(data)

 
global numeric_columns
try:
	numeric_columns=data.select_dtypes(['float64','float32','int32','int64','string']).columns
	print(numeric_columns)
except Exception as e:
	print(e)
	st.write(" Hey Select from side Bar to the left! .")

#selector
st.sidebar.title("selector")

#type of graph
visualisation=st.sidebar.selectbox('select a Page',('page1','page2','page3'))

#visualisation=st.sidebar.selectbox('select a chart type',('scatterplot','Line chart','Barchart','Area Chart','Box Plot','Histogram','jointplot','3d plot','Heatmap','Polar Chart','Contour map','violin plots','polar line','Parallel Category'))

# create scatterplot
if visualisation=='page1':
	
	try:
		st.title("Scatter plot")
		st.sidebar.markdown("**scatterplot Attributes** :")
		select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
		print(select_box1)
		select_box2=st.sidebar.selectbox(label='y axis',options=numeric_columns)
		#scatter=sns.relplot(x=select_box1,y=select_box2,data=data)
		plot=px.scatter(data_frame=data,x=select_box1,y=select_box2,trendline='ols',trendline_color_override='red', template="plotly_dark")
		st.plotly_chart(plot)

		if st.checkbox('Show Information'):

			st.subheader('OLS(ordinary least squares)')
			st.write("***The method of least squares is a standard approach in regression analysis to approximate the solution of overdetermined systems (sets of equations in which there are more equations than unknowns) by minimizing the sum of the squares of the residuals made in the results of every single equation. The most important application is in data fitting. The best fit in the least-squares sense minimizes the sum of squared residuals (a residual being: the difference between an observed value, and the fitted value provided by a model). When the problem has substantial uncertainties in the independent variable (the x variable), then simple regression and least-squares methods have problems; in such cases, the methodology required for fitting errors-in-variables models may be considered instead of that for least squares.***")

		st.title("Histogram")
		st.sidebar.markdown("**Histogram Attributes** :")
		select_box=st.sidebar.selectbox(label='feature',options=numeric_columns)
		ak=px.histogram(data,x=select_box,template="plotly_dark")
		st.plotly_chart(ak,width=1100,height=900)
	
		st.title("Area Chart")
		st.sidebar.markdown("**Area Chart  Attributes** :")
		select_box1=st.sidebar.selectbox(label="x_axis",options=numeric_columns)
		select_box2=st.sidebar.selectbox(label="Y_axis",options=numeric_columns)
		fig = px.area(data, x=select_box1, y=select_box2,
            hover_data=data,template="plotly_dark")
		st.plotly_chart(fig,width=1100,height=900)
	except Exception as e:
		print(e)


	#st.title("Line Chart")
	#st.line_chart(data)
	


#create a line chart 	
#elif visualisation=='Line chart':
	#st.title("Line Chart")
	#st.line_chart(data)

#create a bar chart
elif visualisation=='page3':
	col1,col2=st.beta_columns(2)

	
	try:
		

		st.sidebar.markdown("**contour Map Attributes** :")
		st.title("Contour Map")
		select_box1=st.sidebar.selectbox(label='x Axis',options=numeric_columns)
		select_box2=st.sidebar.selectbox(label='y Axis',options=numeric_columns)
		fig=px.density_contour(data,x=select_box1,y=select_box2,marginal_x="rug",marginal_y="histogram",  width=800, height=400,template="plotly_dark")
		st.plotly_chart(fig,width=1100,height=900)

		st.title("Bar graph")
		st.sidebar.markdown("**Bar Graph Attributes** :")
		select_box4=st.sidebar.selectbox(label='X_axis',options=numeric_columns)
		select_box5=st.sidebar.selectbox(label='Y_axis',options=numeric_columns)
		fig = go.Figure()
		fig.add_trace(go.Bar(
    	y=data[select_box5],
    	x=data[select_box4],
    	marker=dict(
 		color='rgba(58, 71, 80, 0.6)',	
        line=dict(color='rgba(246, 78, 139, 0.6)', width=6)
    	)
		))
		fig.update_layout(
		template="plotly_dark",	
    	xaxis_title=select_box4,
    	yaxis_title=select_box5,
    	legend_title="Legend Title",
    	font=dict(
        family="Courier New, monospace",
        size=18,
        color="white"
    		)
    	)

		st.plotly_chart(fig,width=1100,height=900)

		st.title("3D surface ")
		st.sidebar.markdown("**3d surface Attributes** :")
		select_box1=st.sidebar.selectbox(label="x_Axis",options=numeric_columns)
		select_box2=st.sidebar.selectbox(label="y_Axis",options=numeric_columns)
		select_box3=st.sidebar.selectbox(label="z_Axis",options=numeric_columns)
		fig= go.Figure(data=[go.Mesh3d(x=data[select_box1],y=data[select_box2],z=data[select_box3],
                   opacity=0.5,
                   color='rgba(244,22,100,0.6)'
                  )])
		fig.update_layout(template="plotly_dark",scene = dict(xaxis_title=select_box1,
    	yaxis_title=select_box2,
    	zaxis_title=select_box3))
	
		st.plotly_chart(fig,width=1100,height=900)

		#st.title("parallel categories")
		#st.sidebar.markdown("** Parallel categories Attributes** :")
		#select_box1=st.sidebar.selectbox(label="w.r.t",options=numeric_columns)
		#fig = px.parallel_categories(data, color=select_box1, color_continuous_scale=px.colors.sequential.Inferno)
		#st.plotly_chart(fig,width=1100,height=900)
	except Exception as e:
		print(e)	

	
  
	#fig = go.Figure()
	#fig.add_trace(go.Scatter(x=data[select_box1], y=data[select_box2], fill='tozeroy',mode='lines',
    #line_color='indigo')) # fill down to xaxis
	#fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 5, 1, 7], fill='tonexty')) # fill to trace0 y

#create a area chart


#create a histogram
elif visualisation=='page2':
	try:
		st.title("scatterplot 3 Dimensional")
		st.sidebar.markdown("**3D Scatter plot  Attributes** :")
		select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
		select_box2=st.sidebar.selectbox(label='y axis',options=numeric_columns)
		select_box3=st.sidebar.selectbox(label='z axis',options=numeric_columns)
		fig=px.scatter_3d(data, x=select_box1,y=select_box2,z=select_box3,color=select_box3)
		st.plotly_chart(fig,width=1100,height=900)
	
		st.title("voilin plot")
		st.sidebar.markdown("**Voilin Plot  Attributes** :")
		select_box1=st.sidebar.selectbox(label='x Axis',options=numeric_columns)
		select_box2=st.sidebar.selectbox(label='y Axis',options=numeric_columns)
		#select_box3=st.sidebar.selectbox(label='W.R.T',options=numeric_columns)
		fig = px.violin(data, y=select_box2, x=select_box1,color=select_box2, box=True, points="all", hover_data=data.columns)
		st.plotly_chart(fig,width=1100,height=900)

		st.title("Density Heatmap")
		st.sidebar.markdown("**density_heatmap  Attributes** :")
		select_box1=st.sidebar.selectbox(label='x_axis',options=numeric_columns)
		select_box2=st.sidebar.selectbox(label='y_axis',options=numeric_columns)
		fig=px.density_heatmap(data,x=select_box1,y=select_box2,marginal_x="rug",marginal_y="histogram",  width=800, height=400)
		st.plotly_chart(fig,width=1100,height=900)
	except Exception as e:
		print(e)

	#st.title("Histogram")
	#select_box=st.sidebar.selectbox(label='feature',options=numeric_columns)
	#histogram_slider=st.sidebar.slider(label="Number of Bins",min_value=5,max_value=100, value=30)
	#sns.displot(data[select_box], bins=histogram_slider)
	#st.pyplot()

#create a join plot
#elif visualisation=='jointplot':
	#?
	#fig=plt.hist(select_box3,bins=20 ,color ='green')
#elif visualisation == '3d plot':
	
	
#elif visualisation == 'Heatmap':
	#st.title("Density Heatmap")
	#select_box1=st.sidebar.selectbox(label='x axis',options=numeric_columns)
	#select_box2=st.sidebar.selectbox(label='y axis',options=numeric_columns)
	#fig=px.density_heatmap(data,x=select_box1,y=select_box2,marginal_x="rug",marginal_y="histogram",  width=800, height=400)
	#st.plotly_chart(fig,width=1100,height=900)
	

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


	


