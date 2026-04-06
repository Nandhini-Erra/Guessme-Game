import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
st.title('Student performance Dashboard')
data={
        "Name":['A','B','C','D','E'],
        "Math":[25,30,35,None],
        'Science':[30,35,40,45,None,],
        "English":[85,88,None,90,55]
}
df=pd.DataFrame(data)
# handle missing values
st.header('Raw Data')
st.write(df)
st.header('Data after handling missing values')

#Filling missing values with mean
df.fillna(df.mean(numeric_only=True),inplace=True)
st.subheader('data after filling missing values with mean')
st.write(df)
df['Total']=df['Math']+df['Science']+df['English']
df['Average']=df['Total']/3
st.subheader('Data with Total and Average scores')
st.write(df)
topper=df.loc[df['Average'].idxmax()]
st.success(f'Topper: {topper["Name"]} with average score of {topper["Average"]}')
st.subheader("Total marks score board")
fig=plt.figure(figsize=(10,6))
plt.bar(df['Name'],df['Total'],color='skyblue')
plt.xlabel('Students')
plt.ylabel('Total Marks')
plt.title('Total Marks of Students')    
st.pyplot(fig)