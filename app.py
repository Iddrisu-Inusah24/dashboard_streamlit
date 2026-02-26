import streamlit as st
st.sidebar.write("__"*10)
import pandas as pd
import os
import bcrypt


if "user" not in st.session_state:
    st.session_state["user"] = None

if not os.path.exists("users.csv"):
    df=pd.DataFrame(columns=["username","email", "password"])
    df.to_csv("users.csv",index=False)


st.markdown(
            "<h2 style='color:#0d6efd;'>User Authentication Page </h2>", 
            unsafe_allow_html=True)



username=st.text_input("name")
email=st.text_input("email")
password=st.text_input("password", type="password")


col1,col2= st.columns(2)

with col1:
    # registration hash_password logic
    def hash_password(password):
        # convert to bytes
        password_bytes = password.encode('utf-8')
        
        # generate salt + hash
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        
        return hashed.decode('utf-8')  # store as string


    st.markdown(
            "<h4 style='color:skyblue;'>Click here if new</h4>",
            unsafe_allow_html=True
        )
    if st.button("register", use_container_width=True):
        hashed_pw = hash_password(password)
        df=pd.read_csv("users.csv")

        # Check if username already exists
        existing_user = df[df["email"] == email]

        if not existing_user.empty:
            st.error("Username already exists. Please choose another.")
        
        else:
            hashed_pw = hash_password(password)

            new_user = {
                "username": username,
                "email":email,
                "password": hashed_pw
            }

            df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
            df.to_csv("users.csv", index=False)
            st.success("Registration successful")

with col2:
    st.markdown(
            "<h4 style='color:skyblue;'>Click here if already user</h4>",
            unsafe_allow_html=True
        )
    
    if st.button("Login", use_container_width=True):
        # login hash-password logic
        def verify_password(stored_password, provided_password):
            stored_password_bytes = stored_password.encode('utf-8')
            provided_password_bytes = provided_password.encode('utf-8')
            
            return bcrypt.checkpw(provided_password_bytes, stored_password_bytes)
        df=pd.read_csv("users.csv")
        user = df[df["username"] == username]

        # Check if user exists
        if user.empty:
            st.error("User does not exist")
        
        else:
            #  Extract stored hash
            stored_password = user.iloc[0]["password"]

            #  Verify password securely
            if verify_password(stored_password, password):
                st.success("Login successful")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.switch_page("pages/dashboard.py")


            else:
                st.error("Incorrect password")
        
st.sidebar.image("pages/logo.jpg", width=120)
        























































# import streamlit as st
# secrete_name="iddi"
# secret_password="iddi24"
# with st.form("user login system"):
#     name=st.text_input("name")
#     email=st.text_input("email")
#     password=st.text_input("password", type="password")
#     age=st.number_input("age", step=1)
#     buttton=st.form_submit_button("submit")

# if buttton:
#     if not name or not email or not password:
#         st.warning("Fields cannot be empty")
#     if name==secrete_name and password==secret_password:
#         st.session_state["user"]=name
#         st.session_state["email"]=email
#         st.session_state["age"]=age
#         st.session_state["logged_in"]=True
#         st.success(f"You are welcom back {st.session_state["user"]}")
#         st.switch_page("pages/dashboard.py")
#     else:
#         st.error("incorrect username or password")

