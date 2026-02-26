import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

if not  st.session_state.get("logged_in", False):
    st.warning("Oops! access denied. Please login")
    st.switch_page("app.py")
    st.stop()

else:
    st.markdown("""
        <style>
        img {
            border-radius: 50%;
        }
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([1,6])

    with col2:
            st.markdown(
            "<h1 style='color:#0d6efd;'>AdelgaCode Empowered Dashboard </h1>", 
            unsafe_allow_html=True)
            
            
    with col1:
        st.image("pages/logo.jpg", width=80)

    st.subheader(f"Welcome to your dashboard  {st.session_state['user']}")
    # st.write("Use the button below to analyze your data and uncover meaningful insights.")

   

    col1, col2 = st.columns(2)

    # Data Visualization Section
    with col1:
        st.markdown(
            "<h4 style='color:skyblue;'>Visualize Data</h4>",
            unsafe_allow_html=True
        )
        st.write("Use powerful visualization tools to explore trends and patterns in your data.")
        
        if st.button("Visualize", use_container_width=True):
            st.switch_page("pages/charts.py")


    # Data Summary Section
    with col2:
        st.markdown(
            "<h4 style='color:skyblue;'>Quick Data Summary</h4>",
            unsafe_allow_html=True
        )
        st.write("Generate simple analytical insights and key statistics from your dataset.")
        
        if st.button("Analyze", use_container_width=True):
            st.switch_page("pages/summary.py")



button=st.sidebar.button("logout")
if button:
    st.session_state.clear()
    st.switch_page("app.py")


st.sidebar.image("pages/logo.jpg", width=120)




































# import streamlit as st

# if "logged_in" not in st.session_state:
#     st.warning("Opps! Access denied. Please login before!")
#     st.stop()

# st.title("dashborad")
# st.subheader("You are welcome to your dashboard", st.session_state["user"])
# st.write("Email", st.session_state["email"])
# st.write("age: " , st.session_state["age"])


# if st.button("logout"):
#     st.session_state.clear()
#     st.switch_page("app.py")
#     #

