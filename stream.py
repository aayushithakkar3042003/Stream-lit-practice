import streamlit as st
st.title("hello ai")
st.write('yes')
st.header("hi")
st.text("hey")
chai = st.selectbox("yoour greetings",['good morning',"good afternoon","good night"])
ans = print(f" hello {chai}")
st.success("your chai has been order")