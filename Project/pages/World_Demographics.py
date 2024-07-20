import streamlit as rt
import pandas as ad
import data_preprocessing
from streamlit_echarts import st_echarts
 


def visualisation(df):
    rt.subheader("Adults (ages 15+) and children (ages 0-14) newly infected with HIV")
    rt.bar_chart(data=df,x='country',y='Adults (ages 15+) and children (ages 0-14) newly infected with HIV')

def visualisation1(df):
    rt.subheader("Adults (ages 15-49) newly infected with HIV")
    rt.bar_chart(data=df,x='country',y='Adults (ages 15-49) newly infected with HIV')


def visualisation2(df):
    rt.subheader('"Population, male","Population, female')
    rt.line_chart(data=df,x='country',y= ["Population, male","Population, female"])

def visualisation3(df):
    rt.subheader("Employment to population ratio, 15+, male (%) (national estimate)","Employment to population ratio, 15+, female (%) (national estimate)")
    rt.bar_chart(data=df,x='country',y=["Employment to population ratio, 15+, male (%) (national estimate)","Employment to population ratio, 15+, female (%) (national estimate)"])

def visualisation4(df):
    rt.subheader('GDP per capita (constant 2010 US$)','GNI per capita (constant 2010 US$)')
    rt.bar_chart(data=df,x='country',y=['GDP per capita (constant 2010 US$)','GNI per capita (constant 2010 US$)'])
 
def visualisation5(df):
    rt.subheader('Age dependency ratio (% of working-age population)')
    rt.bar_chart(data=df,x='country',y='Age dependency ratio (% of working-age population)')


def visualisation6(df):
    rt.subheader('Arms Import and Export')
    rt.bar_chart(data=df,x='country',y=['Arms imports (SIPRI trend indicator values)','Arms exports (SIPRI trend indicator values)'])

def visualisation7(df):
    rt.subheader("Total reserves (includes gold, current US$)")
    rt.bar_chart(data=df,x='country',y="Total reserves (includes gold, current US$)")

def visualisation8(df):
    rt.subheader('GDP per capita (constant 2010 US$)')
    rt.bar_chart(data=df,x='Region',y='GDP per capita (constant 2010 US$)')

def visualisation9(df):
    rt.subheader('Individuals using the Internet (% of population)')
    rt.bar_chart(data=df,x='country',y='Individuals using the Internet (% of population)')
def main():
    visualisation(data_preprocessing.processed_df)
    visualisation1(data_preprocessing.processed_df)
    visualisation2(data_preprocessing.processed_df)
    visualisation3(data_preprocessing.processed_df)
    visualisation4(data_preprocessing.processed_df)
    visualisation5(data_preprocessing.processed_df)
    visualisation6(data_preprocessing.processed_df)
    visualisation7(data_preprocessing.processed_df)
    visualisation8(data_preprocessing.processed_df)
    visualisation9(data_preprocessing.processed_df)
main()


def age_dependency_ratio(df,selected_country):
    # Filter data for selected region
    filtered_data = df[df["country"] == selected_country]

    options = {
        "title":{"text":"Age Dependency","subtext":"Age Dependency","left":"center"},
        "tooltip":{"trigger":"item"},
        "legend":{"orient":"vertical","left":"bottom"},
        "series":[
            {
                "name": "Age Dependency",
                "type":"pie",
                "radius":"50%",
                "data":[
                    {"value":filtered_data["Age dependency ratio, young (% of working-age population)"].values[0],"name":"{a} Young".format(a=selected_country)},
                    {"value":filtered_data["Age dependency ratio, old (% of working-age population)"].values[0],"name":"{b} Old".format(b=selected_country)},
                    {"value":filtered_data["Age dependency ratio (% of working-age population)"].values[0],"name":"{c} Ratio".format(c=selected_country)}
                ],
                "emphasis":{
                    "itemStyle":{
                        "shadowBlur":50,
                        "shadowOffsetX":1,
                        "shadowColor":"rgba(0,0,0,0.5)",
                    }
                }
            }
        ]
    }
    st_echarts(
        options=options,height="200px"
    )



with rt.sidebar:
        selected_country = rt.selectbox(
            "Select Country", data_preprocessing.processed_df["country"].unique()
        )






age_dependency_ratio(data_preprocessing.processed_df,selected_country)