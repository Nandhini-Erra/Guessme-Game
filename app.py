import streamlit as st 
st.title("Hi Mrecw")
st.write("welcome Mrecw")
st.header("This is header")
st.text("This is Text")
st.success("This is success msg")

st.title("this is my first app")
name=st.text_input("enter your name")
age=st.number_input("Enter your age",min_value=1,max_value=100)
st.write("Age",age)
branch=st.selectbox("select any ine option",["cse","ece","eee","cs","IT"])
st.write(branch)
skills=st.multiselect("select multiple options",["python","c","java","c++",".net","java script"])
st.write(skills)
gender=st.radio("gender",["Male","Female","Other"])
st.write(gender)
marks=st.slider("Marks",0,100)
st.write(marks)
file=st.file_uploader("upload resume",type=['pdf'])
date=st.date_input("select date")
st.write(date)
color=st.color_picker("picker the color u like")
st.write("the color ive picked is",color)
camera=st.camera_input("take a picture")
if camera:
    st.image(camera)
else:
    st.write("no image captured")
import time
with st.spinner("processing"):
    time.sleep(2)
st.success("Done")
dark_mode=st.toggle("enable dark mode")
if dark_mode:
    st.write("dark mode is on")
else:
    st.write("dark mode is diabled")
