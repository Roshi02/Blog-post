import streamlit as st
def app():
	st.title("Roshni's Daily Blog")
	st.subheader("Login page")
	st.text_input("Username:")
	p=st.text_input("Password:")
	pas ="Roshni02"

	if st.button("Submit"):
		if p==pas:
		 st.success("You are successfully logged in!")
		if p !=pas:
		 st.info("Check your password again")


