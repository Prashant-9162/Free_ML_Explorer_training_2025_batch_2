import streamlit  as st
import joblib


model = joblib.load("mymarksmodel")



st.title("Welcome to LW App")

st.write("hello this is vimal")

# hrs = st.text_input("Enter ur hrs : ")

hrs = st.slider("Enter ur hrs : " , 0, 10, 4)

if int(hrs) <= 10:
	finalmarks= model.predict( [[ int(hrs) ]] )
	st.write("Your Final Marks Will be : " , finalmarks)
else:
	st.write("not supported")


