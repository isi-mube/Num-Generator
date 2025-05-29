import streamlit as st
import random
import requests
from streamlit_lottie import st_lottie

# Streamlit app configuration
st.set_page_config(page_title="Comptador", page_icon="⏱️", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #1c1c1c;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(255, 0, 0, 0.3);
    }
    .title {
        color: #ff0000;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #ffffff;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .button {
        background-color: #ff0000;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #cc0000;
    }
    .stNumberInput input {
        background-color: #333;
        color: white;
        border: 1px solid #ff0000;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Fun Lottie animation (avocado cascade)
avocado_lottie = load_lottie_url("https://lottie.host/0bca77ae-49e7-4f58-8cf4-e21dc68f1827/hR5EvwnbfW.json")

# Title and subtitle
st.markdown('<div class="title">⏱️ Número aleatori</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Introdueix quin número hi haurà al cronòmetre +20 i +30 segons després. 👇</div>',
    unsafe_allow_html=True
)

# Generate a random number between 1 and 60
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 60)

random_number = st.session_state.random_number
st.write(f"El número aleatori generat és: **{random_number}**")

input_1 = st.number_input("Número al cronòmetre +20 segons:", min_value=random_number + 1, max_value=1000, step=1)
input_2 = st.number_input("Número al cronòmetre +30 segons:", min_value=random_number + 1, max_value=1000, step=1)

# Comprovar valors
if st.button("Comprova"):
    expected_20 = random_number + 20
    expected_30 = random_number + 30

    if input_1 == expected_20 and input_2 == expected_30:
        st.success("✅ Correcte! Has fet bé les sumes.")
        if avocado_lottie:
            st_lottie(avocado_lottie, speed=1, loop=False, height=300)
    else:
        st.error(f"❌ Incorrecte! Els valors correctes eren: +20 = {expected_20}, +30 = {expected_30}.")

    st.markdown("---")

# Button to generate a new random number
if st.button("🔁 Generar un nou número"):
    st.session_state.random_number = random.randint(1, 60)
    st.rerun()
