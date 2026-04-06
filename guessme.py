import streamlit as st
import random
st.title("Guess me gamee")
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)
if "attemts" not in st.session_state:
    st.session_state.attempts = 0
max_attempts = 5
guess = st.number_input("Enter your guess(1-10)", min_value=1, max_value=10)
if st.button("Submit guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("guess higher! Try again.")
    elif guess > st.session_state.number:
        st.write("guess lower! Try again.")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.attempts} attempts!")
        st.balloons()
    if st.session_state.attempts >= max_attempts and guess != st.session_state.number:
        st.error(f"Game over! you have used all {max_attempts}attempts.the number was {st.session_state.number}.")
    st.write(f"Attempts remaining:{max_attempts - st.session_state.attempts}")
    if st.button("restart game"):
        st.session_state.number = random.randint(1, 10)
        st.session_state.attempts = 0