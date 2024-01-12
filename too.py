import streamlit as st

def main():
    # Streamlit app title
    st.title("Greetings App")

    # Input for the variable 'name'
    name = st.text_input("Enter your name:")

    # Display the greeting message
    if name:
        st.write(f"Hey {name}!")

if __name__ == "__main__":
    main()
