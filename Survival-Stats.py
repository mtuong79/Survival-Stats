# https://analyticsindiamag.com/building-a-covid-19-dashboard-using-streamlit/
# https://realpython.com/pandas-groupby/
# https://scholar.uwindsor.ca/cgi/viewcontent.cgi?article=8997&context=etd

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

def Stats(df,name,age,sex):

    st.write("Record your Hear-Rate and Sp02")
    file = 'Data/survival-stats.csv'
    df['Age'] = df['Age'].astype(int)
    df['BP'] = df['BP'].astype(int)
    df['SpO2'] = df['SpO2'].astype(int)
    #df['Date'] = pd.to_datetime(df['Date'])

    with st.form("morning_form"):
        today = date.today()
        order_date = st.date_input('Today', today)
        sl_time = st.radio("",("Morning","Afternoon"))
        SP02_rate = st.number_input("Sp02", value=0)
        BP_rate = st.number_input("BP", value=0)
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(sl_time)
            st.write(name)
            st.write(SP02_rate)
            st.write(BP_rate)
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
    person = st.radio("",('Tuong','Thu','Danh','Heart Rate'))

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

    elif person == 'Danh':
        st.subheader("Survival Stats of Danh")
        df_chart = df.groupby('Name')
        danh_chart = df_chart.get_group("Danh")
        st.line_chart(danh_chart[['BP','SpO2']])
        st.area_chart(danh_chart[['BP','SpO2']])
        st.write(danh_chart)
    else:
        st.subheader("Approximate maximum heart rate")
        age = st.number_input("Your Age", value=0)
        max_HR = 220 - age
        st.write(f"The maximum heart rate of you is **{max_HR}** beats per minute")
        st.subheader("Standard of Heart Rate")
        st.image('img/BP_Standard.png')
        st.subheader("What is a normal heart rate?")
        st.markdown("A normal heart rate, when you're not being active, is between 60 – 100 beats per minute. "
                    " is called your resting heart rate. If you've been active, you'll need to wait at least five minutes before taking your pulse.")
        st.markdown("When you're active, your heart beats faster to get more oxygen to your working muscles. The harder your body is working, the faster your heart will beat. "
                    "For example, your heart rate when you're sprinting will be much faster than your heart rate when you're walking. "
                    "If you're exercising hard it's normal for your heart rate to get up to 160 beats per minute or more.")
        st.markdown("There are other things that can make your heart beat faster, like caffeine, nicotine, recreational drugs and some kinds of medications. "
                    "Your heart will also beat faster when you feel strong emotions, like anxiety or fear.")
        st.markdown("Athletes or people who are very fit may have resting heart beats of less than 60 bpm.")
        st.subheader("Exercise and heart rate")
        st.markdown("Like any other muscle, your heart needs exercise to keep it fit and healthy. "
                    "Regular exercise can help reduce your risk of heart disease and other health conditions, such as diabetes.")
        st.markdown("To keep your heart healthy, you should aim to do 150 minutes of low to moderate intensity exercise a week.")

def main():
    st.title("VITAL SIGN")

    st.image("img/jumper.jpg")

    file = "Data/survival-stats.csv"
    # df = get_df(file)
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
