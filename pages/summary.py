import streamlit as st
import pandas as pd


if not  st.session_state.get("logged_in", False):
    st.warning("Oops! access denied. Please login")
    st.switch_page("test.py")
    st.stop()


else:
    st.markdown(
    "<h3 style='color:#1f77b4;;'>The table below displays data from your uploaded file. Select a matric from the sidebar to explore insights.</h3>",
    unsafe_allow_html=True
    )


    df=pd.read_csv("records.csv")
    df.index=df.index+1
    st.dataframe(df)

    # ---- Sidebar Controls ----
    st.sidebar.header("Insights Panel")

    age_option = st.sidebar.selectbox(
        "Age Insight",
        [None, "Average Age", "Max Age", "Min Age"]
            )

    marks_option = st.sidebar.selectbox(
        "Marks Insight",
        [None, "Average Mark", "Highest", "Lowest", "Summation", "Standard Deviation"]
             )
    

    # appear in card format
    col1, col2 = st.columns([3,2])

    with col1:
        st.markdown(
            "<h5 style='color:skyblue;'>See age insights here</h5>",
            unsafe_allow_html=True
        )


    with col2:
         st.markdown(
            "<h5 style='color:skyblue;'>See marks insights here</h5>",
            unsafe_allow_html=True
        )

    #  age logic
    if age_option == "Average Age":
        with col1:
            st.metric("Average Age", round(df["ages"].mean(), 2))

    elif age_option == "Max Age":
        with col1:
            st.metric("Maximum Age", df["ages"].max())

    elif age_option == "Min Age":
        with col1:
            st.metric("Minimum Age", df["ages"].min())


    # marks logic
    if marks_option == "Average Mark":
       
        with col2:
            st.metric("Average Mark", round(df["marks"].mean(), 2))

    elif marks_option == "Highest":
        with col2:
            st.metric("Highest Mark", df["marks"].max())

    elif marks_option == "Lowest":
        with col2:
            st.metric("Lowest Mark", df["marks"].min())

    elif marks_option == "Summation":
        with col2:
            st.metric("Total Marks", df["marks"].sum())

    elif marks_option == "Standard Deviation":
        with col2:
            st.metric("Marks Std Dev", round(df["marks"].std(), 2))


# logout logic
button=st.sidebar.button("logout")
if button:
    st.session_state.clear()
    st.switch_page("test.py")

    