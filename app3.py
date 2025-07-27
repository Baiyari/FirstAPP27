import np
import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Everyone This is Our First Application")
st.write("This is SCIT in Pune!!!")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
##Display the Dataframe
st.write("Here is the dataframe")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
