# https://analyticsindiamag.com/building-a-covid-19-dashboard-using-streamlit/
# https://realpython.com/pandas-groupby/

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

def Stats(df,name,age,sex):

    st.write("Record your BP and Sp02")
    file = 'Data/survival-stats.csv'
    df['Age'] = df['Age'].astype(int)
    df['BP'] = df['BP'].astype(int)
    df['SpO2'] = df['SpO2'].astype(int)
    #df['Date'] = pd.to_datetime(df['Date'])

    with st.form("morning_form"):
        today = date.today()
        order_date = st.date_input('Today', today)
        sl_time = st.radio("",("Morning","Afternoon"))
        BP_rate = st.number_input("BP", value=0)
        SP02_rate = st.number_input("Sp02", value=0)
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(sl_time)
            st.write(name)
            st.write(f"BP: {BP_rate}")
            st.write(SP02_rate)
            st.image('img/BP_Standard.png')

            df = df.append({
                'Date' : today,
                'Mor-Aft' : sl_time,
                'Name' : name,
                'Age' : age,
                'Sex' : sex,
                'BP' : BP_rate,
                'SpO2' : SP02_rate
            }, ignore_index=True)

            #df['Date'] = df['Date'].astype(str)
            st.write(df[['Name','BP','SpO2']])
            df.to_csv(file, index=False)

    #df.to_csv(file, index=['Date'])


def Report(df):
    st.write("Report")
    person = st.radio("",('Tuong','Thu','Danh'))

    if person == 'Tuong':
        st.subheader("Survival Stats of Tuong")
        df_chart = df.groupby('Name')
        tuong_chart = df_chart.get_group("Tuong")
        st.line_chart(tuong_chart[['BP','SpO2']])
        st.area_chart(tuong_chart[['BP','SpO2']])
        st.write(tuong_chart)

    elif person == 'Thu':
        st.subheader("Survival Stats of Thu")
        df_chart = df.groupby('Name')
        thu_chart = df_chart.get_group("Thu")
        st.line_chart(thu_chart[['BP','SpO2']])
        st.area_chart(thu_chart[['BP','SpO2']])
        st.write(thu_chart)

    else:
        st.subheader("Survival Stats of Danh")
        df_chart = df.groupby('Name')
        danh_chart = df_chart.get_group("Danh")
        st.line_chart(danh_chart[['BP','SpO2']])
        st.area_chart(danh_chart[['BP','SpO2']])
        st.write(danh_chart)


def main():
    st.title("SURVIVAL STATS")

    fileUpload = st.file_uploader("Upload file", type=['csv','xlsx','pickle'])

    file = "Data/survival-stats.csv"
    df = pd.read_csv(file)
                     #index_col=['Date'])

    name = st.sidebar.radio('Name', ['Tuong', 'Thu','Danh','Report'], 0)
    if name == 'Tuong':
        age = 42
        sex = 'Male'
        Stats(df,name,age,sex)
    elif name == 'Thu':
        age = 44
        sex = 'Female'
        Stats(df,name,age,sex)
    elif name == 'Danh':
        age = 10
        sex = 'Male'
        Stats(df,name,age,sex)
    else:
        Report(df)

main()
