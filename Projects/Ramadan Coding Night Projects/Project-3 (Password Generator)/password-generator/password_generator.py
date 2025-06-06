import streamlit as st # Import streamlit for creating the web-based UI
import random # Import random for generating random choices
import string # Import string to use predefined character sets

# Function to generate a random password
def generate_password (length, use_digits, use_special) :
    character = string.ascii_letters # Includes uppercase and lowercacse letters

    if use_digits :
        character += string.digits # Adds numbers (0-9) if selected

    if use_special :
        character += string.punctuation # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return ''.join(random.choice(character) for _ in range (length))

# Streamlit UI setup
st.title("Password Generator") # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select Password Length" ,min_value = 6, max_value = 32, value = 12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include Digits") # Checkbox for numbers (0-9)

use_special = st.checkbox("Include Special Characters") # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button ("Generate Password"):
    password = generate_password(length, use_digits, use_special) # Call the password generation function
    st.write(f"Generated Password : {password}") # Display the generated password

st.write("---------------------------------------")
st.write("Build with ❤ by [Muhammad Sharoz](https://github.com/024ahmad)")