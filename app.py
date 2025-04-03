# 1st Assignment
# Growth Mindset Challenge: Web App with Streamlit
import streamlit as st
import streamlit as st

st.title("Welcome")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.title("Growth Mindset Challenge")
st.write("This is a simple and interactive web app to help you develop a growth mindset.")
st.header("What is a Growth Mindset?")
st.write("A growth mindset is the belief that abilities and intelligence can be developed through dedication and hard work. It is the foundation for all great accomplishments.")
st.subheader("Why is it important?")
st.write("Having a growth mindset can lead to greater achievement and success. It encourages resilience, perseverance, and a love for learning.")
st.markdown("streamlit is really cool")

st.markdown('''
    :red[streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.write("This is some text")
st.slider("This is a slider",0,100,50)
st.checkbox("This is a checkbox")
st.radio("This is a radio button", ["Option 1", "Option 2", "Option 3"])
st.selectbox("This is a select box", ["Option 1", "Option 2", "Option 3"])


if st.button("Click me!"):
    st.write("Button clicked!")

st.text_input("enter your name","Type here...")
st.text_area("enter your message","Type here...")
st.date_input("enter your date")
if st.button("submitted"):
    st.write("submitted!")





