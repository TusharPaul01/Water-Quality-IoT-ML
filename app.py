import pandas as pd
import streamlit as st
import pickle
import sklearn
import plotly.express as px
import numpy as np

st.title('Water Quality Prediction')

st.write('Give your data below')

with open('trained_model.pkl', 'rb') as f:
  model = pickle.load(f)

uploaded_file = st.text_input('The URL link','https://thingspeak.com/channels/2029314/feed.csv')
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df.describe())
  df.drop(df.columns[[0, 1, 5, 6, 7, 8, 9]], axis=1, inplace=True)
  df.head()
  df.drop(df.columns[[2]], axis=1, inplace=True)
  df.rename(columns={'field1': 'Turbidity', 'field2': 'ph', 'field3': 'tds'}, inplace=True)
  # df = df[['ph', 'tds', 'Turbidity']]
  predictions = model.predict_proba(df)
  predictions = np.where(predictions[:, 1] >= 0.5, 1, 0)
  potability = pd.DataFrame(predictions, columns=['Potability'])
  fig = px.scatter(df, x="ph", y="Turbidity", template="plotly_dark")
  st.write(fig)
  st.write("WEB APP SCREEN")
  st.write("Prediction of potability using ")
  st.write("the values of TDS and Turbidity")
  st.write(potability)
  st.write("Output")
  if (potability.iloc[1].max() == 1):
    st.write("Fit for drinking")
  else:
    st.write("Unfit for drinking")
