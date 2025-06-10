import streamlit as st
st.title("ai maker app")
if st.button("Make chai"):
    st.success("ai is active")
m = st.checkbox("More functions")
if m:
    st.write("its done")
art_type = st.radio("pick your function",["automation",'data analyst'])
st.write(f"selected function{art_type}")
language = st.selectbox("choose function",['function1',"function2"])
aii = st.slider("firstlevel",0,5,3)
st.number_input("How many cups",min_value=1,max_value=10,step = 1)
st.write(f"Selected sugar level")
name = st.text_input("enter your name")
if name:
    st.write(f"welcome,{name} your chai is on the way")
dob = st.date_input("select your date of birth")
st.write(f"your dob {dob}")
