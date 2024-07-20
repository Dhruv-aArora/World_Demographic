import streamlit as st
from streamlit_echarts import st_echarts
import data_preprocessing


def age_dependency_ratio(df,selected_country):
    # Filter data for selected region
    filtered_data = df[df["country"] == selected_country]

    options = {
        "title":{"text":"Age Dependency","subtext":"Age Dependency By Country","left":"center"},
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
        options=options,height="700px"
    )



with st.sidebar:
        selected_country = st.selectbox(
            "Select Country", data_preprocessing.processed_df["country"].unique()
        )






age_dependency_ratio(data_preprocessing.processed_df,selected_country)