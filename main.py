import streamlit as st
import random

if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'guesses_left' not in st.session_state:
    st.session_state.guesses_left = 7
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'message' not in st.session_state:
    st.session_state.message = ""

st.title("Guess the Number Game")
st.write(f"You have {st.session_state.guesses_left} guesses left.")

guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if not st.session_state.game_over:
        if guess == st.session_state.random_number:
            st.session_state.message = "🎉 You guessed the correct number!"
            st.session_state.game_over = True
        elif guess < st.session_state.random_number:
            st.session_state.message = "Too low!"
            st.session_state.guesses_left -= 1
        elif guess > st.session_state.random_number:
            st.session_state.message = "Too high!"
            st.session_state.guesses_left -= 1
                        
        if st.session_state.guesses_left == 0 and not st.session_state.game_over:
            st.session_state.message = f"Sorry, you ran out of guesses. The number was {st.session_state.random_number}"
            st.session_state.game_over = True

st.write(st.session_state.message)

if st.button("New Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.guesses_left = 7
    st.session_state.game_over = False
    st.session_state.message = ""
    st.rerun()