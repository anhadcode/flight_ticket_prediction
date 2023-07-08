import streamlit as st
import pickle 
import pandas as pd
from PIL import Image
st.set_page_config(page_title="EasyFlight.com")
df= pd.read_excel("Data_Train.xlsx")
st.title("EasyFlights.com")
col= st.columns(3)


with col[1]:
    st.image('flight.jpg')

col= st.columns(3)
#Choose an airline

with col[0]:
    Airline= st.selectbox("Choose an Airline", ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
        'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
        'Vistara Premium economy', 'Jet Airways Business',
        'Multiple carriers Premium economy', 'Trujet'])

#Select source
with col[1]:
    Source= st.selectbox("From",['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])

#Select your Destination
with col[2]:
    Destination= st.selectbox("Destination",['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])

#Total stops
col= st.columns([2,2,2])
with col[0]:
    stops= st.number_input("Number of stops")

with col[1]:
    Date= st.date_input("When")


pipe= pickle.load(open('Flight.pkl','rb'))
result=pipe.predict(pd.DataFrame({"Airline":[Airline],"Source":[Source],"Destination":[Destination],
                           "Total_Stops":[stops],"Month":[Date.month],"Day":[Date.day]}))


col= st.columns([2.5,2,2])

with col[1]:
    if st.button("Estimate Price and Duration"):
        st.write(f"### Price: ₹{'{:,.0f}'.format(int(result[0][0]))}")
        st.write(f"### Duration: {str(int(result[0][1]//1))} Hrs {'{:,.0f}'.format(60*((abs(result[0][1])- result[0][1]//1)))} min")

###########################
#Experimentation
airline_list= ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
        'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
        'Vistara Premium economy', 'Jet Airways Business',
        'Multiple carriers Premium economy', 'Trujet']

#lowest price to high
"""## Also Check"""
if st.button("Cheapest flights"):
    l=[]
    #making a list of prices of all airlines
    for i in airline_list:
        result= pipe.predict(pd.DataFrame({"Airline":[i],"Source":[Source],"Destination":[Destination],
                            "Total_Stops":[stops],"Month":[Date.month],"Day":[Date.day]}))
        l.append([i,result[0][0], result[0][1]])
        #l.append([result])
    #sorted the price 
    l= sorted(l, key=lambda x: x[1])[:5]
    col=st.columns([0.4,4,1])
    for i in l:
        with col[0]:
            img= Image.open(f"{i[0]}.png")
            #img= img.reduce(1)
            st.image(img)
            #st.divider()
        with col[1]:
            st.write(f"##### {(i[0])} price: ₹ {i[1]//1} Duration:{int(i[2]//1)}hrs {int(60*(i[2]-i[2]//1))} min Book it") 
            st.markdown(f'[Click here to Book](https://www.makemytrip.com/flights/)')

        #st.divider()
        
####################
#Less duration flights


if st.button("Less Duration Flights"):
    l=[]
    #making a list of prices of all airlines
    for i in airline_list:
        result= pipe.predict(pd.DataFrame({"Airline":[i],"Source":[Source],"Destination":[Destination],
                            "Total_Stops":[stops],"Month":[Date.month],"Day":[Date.day]}))
        l.append([i,result[0][0], result[0][1]])
        #l.append([result])
    #sorted the price 
    l= sorted(l, key=lambda x: x[2])
    col=st.columns([0.4,4,1])
    for i in l:
        with col[0]:
            img= Image.open(f"{i[0]}.png")
            #img= img.reduce(1)
            st.image(img)
            #st.divider()
        with col[1]:
            st.write(f"##### {(i[0])} price: ₹ {i[1]//1} Duration:{int(i[2]//1)}hrs {int(60*(i[2]-i[2]//1))} min Book it") 
            st.markdown(f'[Click here to Book](https://www.makemytrip.com/flights/)')
            #st.divider()
        
#################
#Expensive ones

if st.button("Premium flights"):
    l=[]
    #making a list of prices of all airlines
    for i in airline_list:
        result= pipe.predict(pd.DataFrame({"Airline":[i],"Source":[Source],"Destination":[Destination],
                            "Total_Stops":[stops],"Month":[Date.month],"Day":[Date.day]}))
        l.append([i,result[0][0], result[0][1]])
        #l.append([result])
    #sorted the price 
    l= sorted(l, key=lambda x: x[1])[::-1]
    col=st.columns([0.4,4,1])
    for i in l:
        with col[0]:
            img= Image.open(f"{i[0]}.png")
            #img= img.reduce(1)
            st.image(img)
            #st.divider()
        with col[1]:
            st.write(f"##### {(i[0])} price: ₹ {i[1]//1} Duration:{int(i[2]//1)}hrs {int(60*(i[2]-i[2]//1))} min Book it") 
            st.markdown(f'[Click here to Book](https://www.makemytrip.com/flights/)')

    

