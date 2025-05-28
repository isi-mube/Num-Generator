import streamlit as st
import random
import requests
from streamlit_lottie import st_lottie

# Streamlit app configuration
st.set_page_config(page_title="Random Number Checker", page_icon="🔢", layout="centered")

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

# Title
st.markdown('<div class="title">Generador de Números Aleatoris</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Introdueix els números +20 i +30 per comprovar la suma!</div>', unsafe_allow_html=True)

# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Fun Lottie animation (avocado cascade)
avocado_lottie = load_lottie_url("https://lottie.host/0bca77ae-49e7-4f58-8cf4-e21dc68f1827/hR5EvwnbfW.json")

# Fun facts or memes
fun_facts = [
    "🥑 Avocados are berries!",
    "🐢 Turtles can breathe through their butts.",
    "😺 Cats have fewer toes on their back paws.",
    "🧠 A day on Venus is longer than a year.",
    "🎮 The first video game was made in 1958!",
]

giphy_embeds = [
    "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "https://media.giphy.com/media/xT9IgpZzk3Z4Z1hXao/giphy.gif",
    "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
    "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"
]

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Generate random numbers
    if "random_number" not in st.session_state:
        st.session_state.random_number = random.randint(50, 60)

    random_number = st.session_state.random_number
    st.write(f"El número aleatori generat és: **{random_number}**")

    # User input
    input_20 = st.number_input("Número +20:", min_value=20, max_value=1000, step=1)
    input_30 = st.number_input("Número +30:", min_value=30, max_value=1000, step=1)

    # Check if the sum is correct
    if st.button("Comprova", key="check_button"):
        total = input_20 + input_30
        if total == random_number:
            st.success("✅ Correcte! La suma coincideix amb el número generat.")
            if avocado_lottie:
                st_lottie(avocado_lottie, speed=1, loop=False, height=300)
        else:
            st.error(f"❌ Incorrecte! La suma és {total}, però el número generat és {random_number}.")

        # Show random fun fact or meme (always)
        st.markdown("---")
        st.subheader("🎉 Random Fact:")
        st.info(random.choice(fun_facts))
        st.image(random.choice(giphy_embeds))

    st.markdown('</div>', unsafe_allow_html=True)

# Button to generate a new random number
if st.button("🔁 Nou número aleatori"):
    st.session_state.random_number = random.randint(50, 60)
    st.rerun()