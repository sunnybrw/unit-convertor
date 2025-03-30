import streamlit as st
st.title("Unit Convertor")
conversion_types = ["length","weight"]
conversion_choice = st.selectbox("Select the conversion type",conversion_types)
if conversion_choice == "length":
    length_units = ["meters","kilometers"]
    input_length = st.number_input("Enter the length", min_value=0.0, format="%.2f")
    from_units = st.selectbox("Select the unit to convert from",length_units)
    to_units = st.selectbox("Select the unit to convert to",length_units)
    length_conversion = {"meters":1.0,"kilometers":1000.0}
    if st.button("Convert"):
             result = input_length * length_conversion[from_units] / length_conversion[to_units]
             st.write(f"{input_length} {from_units} is equal to {result} {to_units}")
elif conversion_choice == "weight":
        weight_units = ["kilograms","grams"]
        input_weight = st.number_input("Enter the weight", min_value=0.0, format="%.2f")
        from_units = st.selectbox("Select the unit to convert from",weight_units)
        to_units = st.selectbox("Select the unit to convert to",weight_units) 
        weight_conversion = {"kilograms":1000,"grams":1}
        if st.button("Convert"):
            result = input_weight * weight_conversion[from_units] / weight_conversion[to_units]
            st.write(f"{input_weight} {from_units} is equal to {result} {to_units}")
