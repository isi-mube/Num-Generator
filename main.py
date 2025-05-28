import streamlit as st
import random

# Streamlit app configuration
st.set_page_config(page_title="Random Number Checker", page_icon="🔢", layout="centered")

# Title
st.title("Generador de Números Aleatoris")

# Generate random numbers
random_number = random.randint(0, 60)
st.write(f"El número aleatori generat és: **{random_number}**")

# User input
st.write("Introdueix els números +20 i +30:")
input_20 = st.number_input("Número +20:", min_value=0, max_value=80, step=1)
input_30 = st.number_input("Número +30:", min_value=0, max_value=80, step=1)

# Check if the sum is correct
if st.button("Comprova"):
    total = input_20 + input_30
    if total == random_number:
        st.success("✅ Correcte! La suma coincideix amb el número generat.")
    else:
        st.error(f"❌ Incorrecte! La suma és {total}, però el número generat és {random_number}.")