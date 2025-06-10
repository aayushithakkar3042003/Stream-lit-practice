import streamlit as st
st.title("chai taste poll")
col1,col2 = st.columns(2)
with col1:
    st.header("masala chai")
    st.image("https://carameltintedlife.com/wp-content/uploads/2021/01/Masala-Chai-.jpg",width=200)
    vote1 = st.button("vote masala chai")

with col2:
    st.header("Adrak chai")
    st.image("https://www.indianhealthyrecipes.com/wp-content/uploads/2023/05/indian-masala-chai-tea.jpg",width=200)
    vote2 = st.button("vote adrak chai")
if vote1:
    st.success("thanks for voting masala chai")
elif vote2:
    st.success("thanks for adrak chai")
name = st.sidebar.text_input('enter your name')
st.sidebar.selectbox("choose your chai",["masala","kesar","adrak"])
st.write(f"welcome your chai{name}")
with st.expander("Show Chai Making INstructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
 """)
    
st.markdown('# Welcome to Chai App')
st.markdown('> Blockquote ')