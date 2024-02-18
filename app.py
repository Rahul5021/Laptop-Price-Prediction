import streamlit as st
import pickle
import numpy as np
# importing pickles
pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")


# brand
company = st.selectbox("Brand", df["Company"].unique())

# operating system
os = st.selectbox("Operating System", df["Operating System"].unique())

# ram size
ram = st.selectbox("RAM Size (in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# type of laptop
type = st.selectbox("Type", df["Type"].unique())

#warranty
warranty = st.selectbox("Warranty", [1,2])

#screen size 
size = st.number_input("Screen Size (Inch)")

#Touchscreen
touch = st.selectbox("Touchscreen", ["YES","NO"])

#hdd
hdd = st.selectbox("HDD (in GB)", [0,128,256,512,1024,2048])

#ssd
ssd = st.selectbox("SSD (in GB)",[0.0,128.0,256.0,512.0,1024.0,2048.0])

#generation
gen = st.number_input("Processor Generation (like 10,11)")

#processor name
proc = st.selectbox("Processor Name",df["Processor Type"].unique())

if st.button("Predict"):
    
    #query
    query = np.array([company, os, ram, type, warranty, size, touch, hdd, ssd, gen, proc])

    query = query.reshape(1,11)
    st.title("Predicted Price= Rs." + str(int(np.exp(pipe.predict(query)[0]))))