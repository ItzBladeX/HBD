import streamlit as st
import time



st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTY5MHd3ZnE5Y283ODQ5Nmd6MHBvemd5eTY0NzdsNTJicHAyenMwciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Mjcv3Dg6irEG6Bb9In/giphy.gif", width="stretch")
st.markdown(
    """
    <style>
    /* Import your desired font */
    @import url('https://googleapis.com');

    /* Target the base HTML and all Streamlit components */
    html, body, [class*="st-"] {
        font-family: 'Pacifico', cursive !important;
        font-size: 24px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

 
st.markdown(""" Happy Birthday! 🎂
            
I hope your day is filled with smiles, laughter, and everything you love. 
You make things brighter just by being you, and I'm really glad I get to know you. 
May this year bring you happiness, success, and maybe… a little more time with me too 😉✨
            
I just wanted you to know that you're special to me. 
I hope your birthday is gentle, happy, and filled with the kind of moments you enjoy most. 
You deserve to be cared for and appreciated, today and always. ✨
            
Enjoy your GIFT, darling. You deserve it all and more ❤️
            
-YOUR SECRET BFF 😊

""", width="stretch")

def animatation(x):
    if x == 1:
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTY5MHd3ZnE5Y283ODQ5Nmd6MHBvemd5eTY0NzdsNTJicHAyenMwciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Mjcv3Dg6irEG6Bb9In/giphy.gif", width="content")
    elif x == 2:
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm1jMHE5anFoeDFsdnd4YmZycnY5eG5uNGdpbjl1bWMwZWo1enEwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pk9FMe6GyhgBaP9QhW/giphy.gif")


suprise = st.button("Suprise", width="stretch", type="primary")

if "run_once" not in st.session_state:
    st.session_state.run_once = True
if st.session_state.run_once:
    st.balloons()
    st.session_state.run_once = False

    