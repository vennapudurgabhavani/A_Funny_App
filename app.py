import streamlit as st 

st.title("Welcome to Innomatics Data App :sunglasses:")
st.snow() 

btn_click = st.button("Hit me!") 

if btn_click == True: 
   st.subheader("You hit me :cry:")
   st.balloons()



