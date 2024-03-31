import pandas as pd
import numpy as np
import plotly.express as px
import calendar
from plotly.offline import init_notebook_mode, iplot
import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(
    page_title="First Dashboard",
    page_icon="🏠",
    layout="wide",
    )

df_all = pd.read_csv('hotel_bookings_EDA.csv')

df_canceled = df_all[df_all['is_canceled'] == 'Canceled']

df_not_canceled = df_all[df_all['is_canceled'] == 'Not Canceled']

df = df_all

#ad79b5
# st.markdown('<h1 style="color: red; font-size: 30px; font-weight: bold;">All The Coming Insights About The Non-Canceled Reservations</h1>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Cancelation Rate by Hotel</h1>', unsafe_allow_html=True)

fig = px.sunburst(df.groupby(['hotel', 'is_canceled'])['reservation_id'].count().reset_index(),
                  path=['hotel', 'is_canceled'], values='reservation_id',
                  color='reservation_id', color_continuous_scale='Blues')
fig.update_layout(showlegend=False, coloraxis_showscale=False)
fig.update_traces(marker_line_color='black', marker_line_width=1, textinfo='label+percent parent')

st.plotly_chart(fig, use_container_width=True)


st.markdown("""<h1 style= "color: #ffffff; font-size: 25px; font-weight: bold;">Although (City Hotel) has bigger number of reservations than (Resort Hotel), it has higher number of canceled reservations</h1>""", unsafe_allow_html=True)

st.divider()
st.divider()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 52px; font-weight: bold;">Lead Time Distribution by Reservation Status</h1>', unsafe_allow_html=True)

fig = px.histogram(df[df.lead_time < 400], x='lead_time', color='is_canceled', barmode='overlay',
                   labels={'is_canceled':'Reservation Status', 'lead_time':'Lead Time'},
                   template='simple_white')

st.plotly_chart(fig, use_container_width=True)


st.markdown("""<h1 style= "color: #ffffff; font-size: 25px; font-weight: bold;">We can see clearly when the Lead Time is low, the Non-Canceled Reservations is high and while the Lead Time is getting higher, the Orange color is getting obvious.\nThat means, The longer the lead time, the higher the cancellation rate</h1>""", unsafe_allow_html=True)

st.divider()
st.divider()


st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Cancelation Rate in Top 15 Countries</h1>', unsafe_allow_html=True)

top15_countries = df.groupby('country')['reservation_id'].count().reset_index().sort_values(by='reservation_id', ascending=False).head(15)


fig = px.bar(df[df.country.isin(top15_countries.country.tolist())].groupby(['country', 'is_canceled'])['reservation_id'].count().reset_index(),
             y="country", x="reservation_id", color="is_canceled",
             barmode="group",
             labels={'country':'Country', 'reservation_id':'# of Bookings', 'is_canceled':'Status'},
             template='simple_white')
# fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)
fig.update_layout(height=600)


st.plotly_chart(fig, use_container_width=True)



st.markdown("""<h1 style= "color: #ffffff; font-size: 25px; font-weight: bold;">All the countries have Non-Canceled Reservations more than Canceled Reservations EXCEPT China & Portugal. China has almost equal number of canceled and non-canceled reservations\nPortugal has the canceled reservation more than non-canceled with a big difference</h1>""", unsafe_allow_html=True)

st.divider()
st.divider()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 52px; font-weight: bold;">Cancelation Rate by Reservation Channel</h1>', unsafe_allow_html=True)

fig = px.sunburst(df.groupby(['reservation_channel', 'is_canceled'])['reservation_id'].count().reset_index(),
                  path=['reservation_channel', 'is_canceled'], values='reservation_id',
                  color='reservation_channel')
fig.update_traces(marker_line_color='black', marker_line_width=1, textinfo='label+percent parent')

st.plotly_chart(fig, use_container_width=True)


st.markdown("""<h1 style= "color: #ffffff; font-size: 25px; font-weight: bold;">although,(Ta/To) has the highest number of reservations, it has high cancelation rate. Unlike (Direct) or (Corporate) has lower number of reservation but has low cancelation rate</h1>""", unsafe_allow_html=True)

st.divider()
st.divider()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 40px; font-weight: bold;">Meal Type Distribution in Top 5 Countries with Non-Canceled Reservation</h1>', unsafe_allow_html=True)


top5_countries_not_canceled = df_not_canceled.country.value_counts().reset_index().head(5).country.to_list()

fig = px.bar(df_not_canceled[df_not_canceled.country.isin(top5_countries_not_canceled)].groupby(['country', 'meal'])['reservation_id'].count().reset_index(),
             x='country', y='reservation_id', color='meal',
             barmode='group',
             labels={'country':'Country', 'reservation_id':'# of Bookings', 'meal':'Meal Type'},
             template='simple_white')
# fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

st.plotly_chart(fig, use_container_width=True)


st.markdown("""<h1 style= "color: #ffffff; font-size: 25px; font-weight: bold;">The meal type distribution is mostly same in all the countries EXCEPT France. France has (No Meal) little bit more than (Half Board)</h1>""", unsafe_allow_html=True)

st.divider()
st.divider()




col1, col2, col3 = st.columns(3)


con1 = col1.container(border=True)
con1.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 20px; font-weight: bold;">Average Number of Guests by Reservation Channel</h1>', unsafe_allow_html=True)
con1.dataframe(df.groupby('reservation_channel')['number_of_guests'].mean().round().reset_index().rename(columns={'reservation_channel':'Reservation Channel', 'number_of_guests':'# of Guests'}))

con2 = col2.container(border=True)
con2.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 20px; font-weight: bold;">Average Number of Guests by Country (Not Canceled Reservations)</h1>', unsafe_allow_html=True)
con2.dataframe(df_not_canceled.groupby('country')['number_of_guests'].mean().round().reset_index().sort_values(by='number_of_guests', ascending=False).rename(columns={'country':'Country', 'number_of_guests':'# of Guests'}))

con3 = col3.container(border=True)
con3.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 20px; font-weight: bold;">Countries With Menimum Number of Reservations (Not Canceled Reservations)</h1>', unsafe_allow_html=True)
con3.dataframe(df_not_canceled.country.value_counts().reset_index()[df_not_canceled.country.value_counts().reset_index()['count'] == 1].rename(columns={'country':'Country', 'count':'# of Reservations'}))
