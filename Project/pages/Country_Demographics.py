import streamlit as rt
import pandas as ad
import data_preprocessing


def visualisation(df):
   rt.subheader("Automated teller machines (ATMs) (per 100,000 adults)")
   rt.bar_chart(data=df,x='country',y="Automated teller machines (ATMs) (per 100,000 adults)")

def visualisation1(df):
   
   rt.bar_chart(data=df,x='country',y=['Fixed broadband subscriptions','Fixed telephone subscriptions'])

def visualisation2(df):
   rt.bar_chart(data=df,x='country',y='Women Business and the Law Index Score (scale 1-100)')

def visualisation3(df):
   rt.bar_chart(data=df,x='country',y='Labor force, total')

def visualisation4(df):
   rt.line_chart(data=df,x='country',y='Final consumption expenditure (constant 2010 US$)')
def main():
   visualisation(data_preprocessing.processed_df)
   visualisation1(data_preprocessing.processed_df)
   visualisation2(data_preprocessing.processed_df)
   visualisation3(data_preprocessing.processed_df)
   visualisation4(data_preprocessing.processed_df)
main()
    

 