import streamlit as st

def two_column_input(left_title, right_title):
    c1, c2 = st.columns([3,1])
    with c1:
        left = st.text_area(left_title, height=300)
    with c2:
        right = st.text_area(right_title, height=300)
    return left, right

def badge(text):
    st.markdown(f"**🔹 {text}**")
