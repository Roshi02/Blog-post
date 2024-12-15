import streamlit as st

import Blog
import blog_login

pages_dict = {
                "Blog": Blog,
                "Login": blog_login,
                
            }

st.sidebar.title("Navigation")

user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Blog":
    Blog.app() # The 'app()' function should not take any input if the selection option is "Home".
else:
      blog_login.app()
