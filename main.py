import streamlit as st
import random
from giphy_client import DefaultApi, ApiException

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
    .header {
        color: #ffffff;
        font-size: 24px;
        font-weight: bold;
        text-
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

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Generate random numbers
    random_number = random.randint(50, 60)
    st.write(f"El número aleatori generat és: **{random_number}**")

    # User input
    input_20 = st.number_input("Número +20:", min_value=20, max_value=60, step=1)
    input_30 = st.number_input("Número +30:", min_value=30, max_value=60, step=1)

    # Check if the sum is correct
    if st.button("Comprova", key="check_button"):
        total = input_20 + input_30
        if total == random_number:
            st.success("✅ Correcte! La suma coincideix amb el número generat.")
        else:
            st.error(f"❌ Incorrecte! La suma és {total}, però el número generat és {random_number}.")

    st.markdown('</div>', unsafe_allow_html=True)
    import streamlit.components.v1 as components

    # Streamlit animation using Lottie
    def load_lottie_animation(url):
        components.html(
            f"""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.4/lottie.min.js"></script>
            <div id="lottie-animation" style="width: 300px; height: 300px; margin: auto;"></div>
            <script>
                var animation = bodymovin.loadAnimation({{
                    container: document.getElementById('lottie-animation'),
                    renderer: 'svg',
                    loop: true,
                    autoplay: true,
                    path: '{url}'
                }});
            </script>
            """,
            height=300,
        )

    # Load and display a Lottie animation
    st.markdown('<div class="header">Animació:</div>', unsafe_allow_html=True)
    load_lottie_animation("https://assets9.lottiefiles.com/packages/lf20_5k1zqk.json")

    # Random Giphy generator
    def get_random_giphy(api_key, tag="funny"):
        api_instance = DefaultApi()
        try:
            response = api_instance.gifs_random_get(api_key, tag=tag)
            return response.data.image_url
        except ApiException as e:
            st.error("Error fetching Giphy: {}".format(e))
            return None

    # Display a random Giphy
    st.markdown('<div class="header">Giphy Aleatori:</div>', unsafe_allow_html=True)
    giphy_api_key = "YOUR_GIPHY_API_KEY"  # Replace with your Giphy API key
    giphy_url = get_random_giphy(giphy_api_key)
    if giphy_url:
        st.image(giphy_url, caption="Giphy generat aleatoriament")