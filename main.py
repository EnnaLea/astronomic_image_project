import streamlit as st
import requests

st.set_page_config(layout="wide")

api_key = "g0UR7Qf5FUdC2hybpWAHf0JxAHJ0BDYXhHoW3WLP"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# response from nasa api
response = requests.get(url)

# status response control
if response.status_code == 200:
    data = response.json()
    image = data.get("url")
    title = data.get("title")
    explanation = data.get("explanation")

    st.header(title)
    st.image(image)
    st.write(explanation)
else:
    st.error(f"Errore nella richiesta: {response.status_code}")







