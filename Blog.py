import streamlit as st
def app():	
	st.title("Embracing the Season and Finding Joy in the Little Things")

	st.subheader("The Magic of Twinkling Lights")

	st.write("There’s something about holiday lights that makes everything feel magical. Whether you’re taking a walk around your neighborhood or hanging them up in your own living room, those bright, tiny sparks of light remind us that even in the darkest months, there is always something to illuminate our path.") 

	st.subheader("The Comfort of a Good Book and a Warm Drink")

	st.write("One of the best ways to unwind after a long day is to curl up with a good book, a fuzzy blanket, and your favorite drink. There’s a certain comfort in sipping on a hot cocoa or chai latte as you lose yourself in a story, letting your imagination travel to other worlds or simply finding solace in the familiar.")

	st.subheader("Quality Time with Loved Ones")

	st.write("During winter, quality time with loved ones becomes even more special as the season encourages cozy, shared moments. Whether it’s gathering by the fire, sipping hot cocoa, playing games, or taking a snowy walk, these activities create lasting memories and deepen bonds. The shorter days and colder nights remind us that true joy lies in simple pleasures and the warmth found in each other’s company.")

	st.sidebar.slider("Rate the blog",1, 5)
	st.sidebar.selectbox("Would you recommend it to a friend?", ("Yes", "No"))
	if st.sidebar.button("Sumbit"):
		st.sidebar.success("Thank you for submitting or sharing your response!")
	st.text_input("Feedback:")
	if st.button("Enter Feedback"):
		st.success("Thanks for entering your feedback!")

