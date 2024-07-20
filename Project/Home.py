import streamlit as st
import pandas as pd
import data_preprocessing
 
st.title('World Demographic Data')
st.image('picture3.jpg')
 
def show_data_frame(df):
    st.write(df)    
 
def main():
    df=pd.read_csv("final_demographics_data.csv")
    
    
    if st.button("Show Data Frame"):
            # Display DataFrame
            show_data_frame(data_preprocessing.processed_df)    

    # Emtpy Values
    on = st.toggle("Check Missing Values")
    if on:
         st.dataframe(data_preprocessing.processed_df.isnull().sum(),use_container_width=True)

main()
