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

# Cancelation Rate
st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">The Cancelation Rate</h1>', unsafe_allow_html=True)
fig = px.pie(df.is_canceled.value_counts().reset_index(), values='count', names='is_canceled', 
             color='count', color_discrete_sequence=px.colors.sequential.RdBu,
             template='simple_white', hole=0.4)
fig.add_annotation(text="Canceled", x=0.5, y=0.5, showarrow=False)
fig.update_layout(showlegend=False)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Number of Reservations by Year, Month & Holiday(Not Canceled)
st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Number of Reservations by Year, Month & Holiday</h1>' + '<span style="text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;">(Not Canceled Reservations)</span>', unsafe_allow_html=True)
fig = px.line(df_not_canceled.month.value_counts().reset_index().sort_values(by='month'), x="month", y="count",
             title="Number of Bookings by Month",
             labels={'month':'Month', 'count':'# of Bookings'}, markers=True,
             template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)


fig = px.line(df_not_canceled.year.value_counts().reset_index().sort_values(by='year'), x="year", y="count",
             title="Number of Bookings by Year",
             labels={'year':'Year', 'count':'# of Bookings'}, markers=True,
             template='plotly_dark')
fig.update_layout(width=540, height=400)

col1.plotly_chart(fig)

fig = px.pie(df_not_canceled.is_holiday.value_counts().reset_index(), values='count', names='is_holiday',
             template='simple_white', color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_layout(showlegend=False)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)

col2.plotly_chart(fig)

st.divider()

# Top 15 Countries
st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Top 15 Countries</h1>' + '<span style="text-align: center; color: #ad79b5; font-size: 25px; font-weight: bold;">(Not Canceled Reservations)</span>', unsafe_allow_html=True)
fig = px.bar(df_not_canceled.country.value_counts().reset_index().head(15), y="country", x="count",
             color="country",
             labels={'country':'Country', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='#ad79b5', marker_line_width=1.5)

st.plotly_chart(fig, use_container_width=True)
st.divider()
st.divider()
st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 80px; font-weight: bold;">Filter The Data</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)


data_selection = col1.selectbox("Select The Type of Data", ["All", "Canceled", "Not Canceled"], help='Canceled or Not Canceled or Both')

if data_selection == 'Canceled':
    df = df_canceled
elif data_selection == 'Not Canceled':
    df = df_not_canceled
else:
    df = df_all

year_selection = col2.selectbox("Select The Year", sorted(df['year'].unique().tolist()) + ['All'], index=3)

if year_selection == 'All':
    pass

else:
    df = df[df['year'] == year_selection]

month_selection = col3.multiselect("Select The Month", df['month'].unique(), default=df['month'].unique())

df = df[df['month'].isin(month_selection)]


col1, col2 = st.columns(2)

fig = px.bar(df.meal.value_counts().reset_index(), x="meal", y="count",
             title="Number of Bookings by Meal", color="meal", text_auto=True,
             labels={'meal':'Meal', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

col1.plotly_chart(fig, use_container_width=True)


fig = px.histogram(df, x="number_of_guests",
                   title="Number of Guests Distribution",
                   labels={'number_of_guests':'Number of Guests'},
                   template='simple_white')

col2.plotly_chart(fig, use_container_width=True)


fig = px.pie(df.reservation_channel.value_counts().reset_index(), values='count', names='reservation_channel',
            title="Number of Bookings by Reservation Channel",
            color_discrete_sequence=px.colors.sequential.RdBu,
            template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)

col2.plotly_chart(fig, use_container_width=True)

fig = px.histogram(df, x="booking_changes",
                   title="Number of Booking Changes Distribution",
                   labels={'booking_changes':'Number of Booking Changes'},
                   template='simple_white')

col1.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)

fig = px.bar(df.deposit_type.value_counts().reset_index(), x="deposit_type", y="count",
             title="Number of Bookings by Deposit Types", color="deposit_type", text_auto=True,
             labels={'deposit_type':'Deposit Types', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

col1.plotly_chart(fig, use_container_width=True)

fig = px.histogram(df, x='special_requests', marginal="box",
                   title="Number of Special Requests Distribution",
                   labels={'special_requests':'Number of Special Requests'},
                   template='simple_white')
fig.update_traces(marker_color='red')

col2.plotly_chart(fig, use_container_width=True)

fig = px.bar(df.customer_type.value_counts().reset_index(), x="customer_type", y="count",
             title="Number of Bookings by Customer Types", color="customer_type", text_auto=True,
             labels={'customer_type':'Customer Types', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

col3.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

fig = px.bar(df.assigned_room_type.value_counts().reset_index(), x="assigned_room_type", y="count",
             title="Number of Bookings by (Assigned) Room Types", color="assigned_room_type", text_auto=True,
             labels={'assigned_room_type':'Room Types', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

col1.plotly_chart(fig, use_container_width=True)


fig = px.bar(df.reserved_room_type.value_counts().reset_index(), x="reserved_room_type", y="count",
             title="Number of Bookings by (Reserved) Room Types", color="reserved_room_type", text_auto=True,
             labels={'reserved_room_type':'Room Types', 'count':'# of Bookings'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)

col2.plotly_chart(fig, use_container_width=True)

fig = px.pie(df.is_repeated_guest.value_counts().reset_index(), values='count', names='is_repeated_guest',
             color='is_repeated_guest', title="Number of Bookings of Repeated Guests & Not Repeated Guests",
             template='simple_white', hole=0.6)
fig.add_annotation(text="Repeated Guests", x=0.5, y=0.5, showarrow=False)
fig.update_layout(showlegend=False)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)

st.plotly_chart(fig, use_container_width=True)

