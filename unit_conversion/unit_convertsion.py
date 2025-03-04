import streamlit as st

st.title ("Welcome to Unit Converter")

conversion_type = st.sidebar.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Function Convert to Length

def convert_length (value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Feet":
        return value*3.2808
    elif from_unit == "Feet" and to_unit == "Meters":
         return value/3.2808
    elif from_unit == "Kilometers" and to_unit == "Miles":
         return value*0.621371
    elif from_unit == "Miles" and to_unit == "Kilometers":
         return value/0.621371
    else:
         return value
    
    # Function Convert Weight

def convert_weight (value, from_unit, to_unit):
     if from_unit == "Kilograms" and to_unit == "Pounds":
        return value*2.20462
     elif from_unit == "Pounds" and to_unit == "Kilograms":
          return value/2.20462
     elif from_unit == "Grams" and to_unit == "Ounce":
          return value*0.035274
     elif from_unit == "Ounce" and to_unit == "Grams":
          return value/0.035274
     else:
          return value
     
     # Function Convert Temperature
def convert_temperature (value, from_unit, to_unit):
     if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
     elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
     elif from_unit == "Celsius" and to_unit == "Fahrenheit":
          return (value * 9/5) + 32
     elif from_unit == "Fahrenheit" and to_unit == "Celsius":
          return (value-32) * 5/9
     else:
          return value
     
     # Main Conversion Logic
if conversion_type == "Length":
          st.header("Length Conversion")
          length_units = ["Meters" , "Feet" , "Kilometers" , "Miles"]
          from_unit = st.selectbox("From" , length_units)
          to_unit = st.selectbox("To" , length_units)
          value = st.number_input("Enter Value: " , value=0)
          result = convert_length (value, from_unit,to_unit)
          st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Weight":
          st.header("Weight Conversion")
          weight_units = ["Kilograms" , "Pounds" , "Ounce" , "Grams"]
          from_unit = st.selectbox("From" , weight_units)
          to_unit = st.selectbox("To" , weight_units)
          value = st.number_input("Enter Value: " , value=1.0)
          result = convert_weight (value, from_unit,to_unit)
          st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
          st.header("Temperature Conversion")
          temperature_units = ["Celsuis" , "Kelvin" , "Fahrenheit"]
          from_unit = st.selectbox("From" , temperature_units)
          to_unit = st.selectbox("To" , temperature_units)
          value = st.number_input("Enter Value: " , value=0.0)
          result = convert_temperature(value, from_unit,to_unit)
          st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")


