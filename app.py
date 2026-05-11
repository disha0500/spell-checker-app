import streamlit as st
import textdistance

# Load dictionary
with open("words.txt", "r") as file:
    dictionary = file.read().splitlines()

# Page title
st.title("📝 Spell Checker")

st.write("Spell Checker using Minimum Edit Distance")

# Input box
user_word = st.text_input("Enter a word")

# Button
if st.button("Check Spelling"):

    user_word = user_word.lower().strip()

    # Correct word
    if user_word in dictionary:

        st.success("✅ Correct Spelling")

    else:

        suggestions = []

        # Find similar words
        for word in dictionary:

            if abs(len(word) - len(user_word)) <= 2:

                distance = textdistance.levenshtein(
                    user_word,
                    word
                )

                if distance <= 2:
                    suggestions.append((word, distance))

        suggestions.sort(key=lambda x: x[1])

        # Show suggestion
        if suggestions:

            best_word = suggestions[0][0]

            st.error(
                f"❌ Incorrect Spelling\n\nDid you mean: {best_word} ?"
            )

        else:

            st.warning("No suggestion found")

# Example table
st.subheader("Real World Examples")

st.table({
    "Wrong Word": [
        "speling",
        "langauge",
        "computr",
        "enviroment"
    ],
    "Correct Word": [
        "spelling",
        "language",
        "computer",
        "environment"
    ]
})