import streamlit as st
with st.sidebar:
    st.title("Video Downloader")
    if st.button("YouTube"):
        st.write("https://y2mate.bet/")
    if st.button("Facebook"):
        st.write("https://taivideo.vn/")
st.title("Download and Convert")
st.image('Img.png',width=400)
if st.button("Convert"):
    st.write("https://cloudconvert.com/")
