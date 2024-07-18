import streamlit as st
import pandas as pd
import base64
import pickle
import datetime
from sklearn.preprocessing import MinMaxScaler

st.set_page_config( page_title='Flight Fare Prediction' , page_icon='✈️')



st.markdown(
    """
    <style>
    .stButton button {
        width: 200px;
        height: 50px;
        font-size: 20px;
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Load the model
model = pickle.load(open("flight_model.sav", 'rb'))

# App header
st.header('Flight Price Prediction' )


# Current date
curr_date = datetime.date.today()
selected_date = st.date_input("Enter Date", value=curr_date)

# Select airline
airline = st.selectbox(
    "Select Airline:",
    [
        'Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
        'Jet Airways Business', 'Multiple carriers', 'Multiple carriers Premium economy',
        'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy'
    ]
)
dep_time = st.time_input('Enter Departure Time')

Arrival = st.time_input('Enter Arrival Time')

# Calculate hours and minutes
dep_hour = dep_time.hour
dep_min = dep_time.minute
Arrival_hour = Arrival.hour
Arrival_minute = Arrival.minute

# Extract day and month from the selected date
day = selected_date.day
month = selected_date.month

# Calculate duration
Duration_hour = abs(dep_hour - Arrival_hour)
Duration_minute = abs(dep_min - Arrival_minute)

# One-hot encode the airline
airline_map = {
    'Jet Airways': 'Jet_Airways', 'IndiGo': 'IndiGo', 'Air India': 'Air_India',
    'Multiple carriers': 'Multiple_carriers', 'SpiceJet': 'SpiceJet', 'Vistara': 'Vistara',
    'GoAir': 'GoAir', 'Multiple carriers Premium economy': 'Multiple_carriers_Premium_economy',
    'Jet Airways Business': 'Jet_Airways_Business', 'Vistara Premium economy': 'Vistara_Premium_economy',
    'Trujet': 'Trujet', 'Air Asia': 'Air_Asia'
}

airline_cols = ['Air_Asia', 'Air_India', 'GoAir', 'IndiGo', 'Jet_Airways', 'Jet_Airways_Business',
                'Multiple_carriers', 'Multiple_carriers_Premium_economy', 'SpiceJet', 'Vistara',
                'Vistara_Premium_economy', 'Trujet']

airline_encoded = {col: 0 for col in airline_cols}
if airline in airline_map:
    if airline == None:
        st.error('please enter airline')
    else:
        airline_encoded[airline_map[airline]] = 1

# Select source
source = st.selectbox('Select Source', ['Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai'])

source_map = {
    'Delhi': 's_Delhi', 'Kolkata': 's_Kolkata', 'Mumbai': 's_Mumbai',
    'Chennai': 's_Chennai', 'Banglore': 's_Banglore'
}

source_cols = ['s_Banglore', 's_Chennai', 's_Delhi', 's_Kolkata', 's_Mumbai']
source_encoded = {col: 0 for col in source_cols}
if source in source_map:
    source_encoded[source_map[source]] = 1

# Select destination
destination = st.selectbox('Select Destination:', [ 'Cochin','Banglore', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'])

destination_map = {
    'Cochin': 'Cochin', 'Delhi': 'Delhi', 'New Delhi': 'New_Delhi',
    'Hyderabad': 'Hyderabad', 'Kolkata': 'Kolkata', 'Banglore': 'Banglore'
}

destination_cols = [ 'Cochin', 'Delhi', 'Hyderabad','Banglore', 'Kolkata', 'New_Delhi']
destination_encoded = {col: 0 for col in destination_cols}
if destination in destination_map:
    destination_encoded[destination_map[destination]] = 1

# Select total stops
Total_Stops = st.selectbox('Total Stops', [0, 1, 2, 3, 4])

# Collect all input data
test_data = [[
    airline_encoded['Air_Asia'], airline_encoded['Air_India'], airline_encoded['GoAir'], airline_encoded['IndiGo'],
    airline_encoded['Jet_Airways'], airline_encoded['Jet_Airways_Business'], airline_encoded['Multiple_carriers'],
    airline_encoded['Multiple_carriers_Premium_economy'], airline_encoded['SpiceJet'], airline_encoded['Vistara'],
    airline_encoded['Vistara_Premium_economy'], airline_encoded['Trujet'],
    source_encoded['s_Banglore'], source_encoded['s_Chennai'], source_encoded['s_Delhi'],
    source_encoded['s_Kolkata'], source_encoded['s_Mumbai'],
    destination_encoded['Banglore'], destination_encoded['Cochin'], destination_encoded['Delhi'],
    destination_encoded['Hyderabad'], destination_encoded['Kolkata'], destination_encoded['New_Delhi'],
    Total_Stops, day, month, dep_hour, dep_min, Arrival_hour, Arrival_minute, Duration_hour, Duration_minute
]]


scaler = MinMaxScaler()
test_data = scaler.fit_transform(test_data)

# Create submit button

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button('Predict'):
    prediction = model.predict(test_data)
    st.success(f'Predicted Flight Fare : {prediction[0]}')
st.markdown("</div>", unsafe_allow_html=True)
