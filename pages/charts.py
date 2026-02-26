import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

if not  st.session_state.get("logged_in", False):
    st.switch_page("test.py")
    st.stop()

st.markdown(
    "<h3 style='color:#1f77b4;;'>The table below displays data from your uploaded file. Select a chart from the sidebar to explore insights.</h3>",
    unsafe_allow_html=True
)

df=pd.read_csv("records.csv")
df.index=df.index+1
st.dataframe(df)

choice=st.sidebar.selectbox("Select", [None,"bar", "scatter", "line", "pie"])

df=pd.read_csv("records.csv")
if choice=="bar":
    fig,ax=plt.subplots(facecolor="lightgrey")
    plt.bar(df["names"], df["marks"])
    plt.xticks(rotation=90)
    plt.title("Bar Gragh Showing Insights on Student Score")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    ax.set_facecolor("black")
    plt.grid(True)
    st.pyplot(fig)

elif choice=="line":
    fig,ax=plt.subplots()
    plt.plot(df["names"], df["marks"], marker="o")
    plt.title("TRENDS ON STUDENTS PERFORMANCE")
    plt.xlabel('Student Names')
    plt.ylabel("Student Marks")
    plt.grid(True)
    plt.xticks(rotation=90)
    ax.set_facecolor("black")
    st.pyplot(fig)

elif choice=="scatter":
    st.subheader("Scatter Plot Illustratng A distribution")
    st.scatter_chart(df.set_index("names"))

elif choice=="pie":
    fig,ax=plt.subplots(facecolor="lightgrey")
    plt.pie(df["marks"],labels=df["names"], autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)


# logout logic
button=st.sidebar.button("logout")
if button:
    st.session_state.clear()
    st.switch_page("test.py")

