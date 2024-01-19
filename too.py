import streamlit as st
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
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
