import streamlit as st

genre = st.radio(
    "What's your favorite lipstick brand?",
    [":rainbow[Dior]", "***Gucci***", "Hourglass :lipstick:"],
    captions = ["Lip Glow.", "Matte.", "Lip Balm."])

if genre == ':rainbow[Dior]':
    st.write('You selected Dior.')
else:
    st.write("You didn\'t select Dior.")
    
    
    
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'indigo'))
st.write('You selected wavelengths between', start_color, 'and', end_color)