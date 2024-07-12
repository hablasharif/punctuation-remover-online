import streamlit as st
import string

# Define allowed characters
allowed_characters = 'abcdefghijklmnopqrstuvwxyz'

# Function to remove punctuation
def remove_punctuation(text):
    cleaned_text = ''.join(char for char in text if char.lower() in allowed_characters)
    return cleaned_text

# Streamlit app
def main():
    st.title('Punctuation Remover')

    # Input text area
    input_text = st.text_area('Enter your text:', height=200)

    if st.button('Remove Punctuation'):
        cleaned_text = remove_punctuation(input_text)
        st.markdown('### Cleaned Text:')
        st.text(cleaned_text)

if __name__ == "__main__":
    main()
