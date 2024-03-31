import pandas as pd
import numpy as np
import plotly.express as px
import calendar
from plotly.offline import init_notebook_mode, iplot
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="Hotel Bookings Dashboard",
    page_icon="🏠",
    layout="wide",
    )

df_original = pd.read_csv('hotel_bookings.csv')

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Hotel Bookings Dashboard</h1>', unsafe_allow_html=True)


animation = load_lottieurl('https://lottie.host/b4bd8aa2-6646-4536-a542-8a0d1612ded3/N6JHEWTMfD.json')

st_lottie(animation, speed=1, height=600, width=900, loop=True, quality="high")

st.markdown("""- #### The data is about hotel bookings and their associated details.
            \n- #### The data contains 119390 rows and 32 columns *(117601 rows and 26 columns after cleaning)*.
            \n- #### The data is from 2015 to 2017.\n - #### The data is available on [kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand). """, unsafe_allow_html=True)

st.divider()

if st.checkbox("Show Sample of Original Data"):
    st.dataframe(df_original.head())

st.divider()

if st.checkbox("Show Columns Discription (after cleaning)"):
    st.markdown(f"""<h3 style="text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;">Columns Discription</h3>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Reservation Id:</u>" + " *The id of the reservation*" + """ <span style="color:green">(Unique number)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Hotel:</u>" + " *The property where the booking was made*" + """ <span style="color:green">(City Hotel, Resort Hotel)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Is Canceled:</u>" + " *Whether the booking was canceled or not*" + """ <span style="color:green">(Canceled, Not Canceled)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Lead Time:</u>" + " *Count of days between the assignation date and the arrival date*" + """ <span style="color:green">(# of days)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Year:</u>" + " *The year of the booking*" + """ <span style="color:green">(2015, 2016, 2017)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Month:</u>" + " *The month of the booking*" + """ <span style="color:green">(1, 2, 3, ..., 12)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Quarter:</u>" + " *The quarter of the year the booking was made at*" + """ <span style="color:green">(Q1, Q2, Q3, Q4)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Day:</u>" + " *The day of the booking*" + """ <span style="color:green">(1, 2, 3, ..., 30)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Day Name:</u>" + " *The day of the week the booking was made at*" + """ <span style="color:green">(Monday, Tuesday, Wednesday, ..., Sunday)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Is Holiday:</u>" + " *Whether the booking was made on a holiday or not*" + """ <span style="color:green">(Holiday, Non-Holiday)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Adults:</u>" + " *The number of adults in the booking*" + """ <span style="color:green">(# of adults)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Children:</u>" + " *The number of children in the booking*" + """ <span style="color:green">(# of children)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Babies:</u>" + " *The number of babies in the booking*" + """ <span style="color:green">(# of babies)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Meal:</u>" + " *The meal plan of the booking*" + """ <span style="color:green">(No Meal, Bed and Breakfast, Half Board, Full Board)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Country:</u>" + " *The country of the people who made the booking*" + """ <span style="color:green">(175 country)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Reservation Channel:</u>" + " *From which channel the booking was made*" + """ <span style="color:green">(TA/TO, Direct, Corporate, GDS)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Is Repeated Guest:</u>" + " *Whether the booking was made by a repeated guest or not*" + """ <span style="color:green">(Repeated Guest, Not Repeated Guest)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Assigned Room Type:</u>" + " *The room type (assigned) to the booking*" + """ <span style="color:green">(A, B, C, D, E, F, G, H, I, K, L, P)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Reserved Room Type:</u>" + " *The room type (reserved) to the booking*" + """ <span style="color:green">(A, B, C, D, E, F, G, H, L, P)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Booking Changes:</u>" + " *The number of changes made to the booking*" + """ <span style="color:green">(# of changes)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Deposit Type:</u>" + " *Where the deposit was made or not*" + """ <span style="color:green">(No Deposit, With Deposit)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Customer Type:</u>" + " *The type of customer who made the booking*" + """ <span style="color:green">(Transient, Transient-Party, Contract)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Special Requests:</u>" + " *The number of special requests made during the reservation*" + """ <span style="color:green">(# of special requests)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Arrival Date:</u>" + " *The date of the arrival*" + """ <span style="color:green">(Date Format)</span>""", unsafe_allow_html=True)
    st.markdown(" - ##### <u>Duration:</u>" + " *The duration of the reservation*" + """ <span style="color:green">(# of days)</span>""", unsafe_allow_html=True)
















