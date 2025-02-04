import streamlit as st
import pandas as pd
import numpy as np

st.write("## Welcome to my first Streamlit Project")
st.write("Hello! I am excited to have you here!")
x = st.text_input("What is your name?")

st.write("Nice to meet you" , x, ". I'm excited to explore countries freedom scores with you.")
st.write("Ready to get started? Click the button below.")
is_clicked = st.button("Click me :)")

data = pd.read_csv("freedom_world_data.csv")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)