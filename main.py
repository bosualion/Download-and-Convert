import streamlit as st
with st.sidebar:
    username = st.text_input("Username: ")
    password = st.text_input("Password: ")
if username == "Le Tan Loi" and password == "051323":
    st.title("Download and Convert")
    l,m,r = st.columns(3)
    m.image('Img.png',width=400)
    left, right = st.columns(2)
    if left.button("Download",use_container_width=True):
        st.write("[YouTube](https://y2mate.bet)")
        st.write("[Facebook](https://taivideo.vn)")
    if right.button("Convert",use_container_width=True):
        st.write("https://cloudconvert.com/")
