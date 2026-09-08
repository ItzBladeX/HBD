import streamlit as st



if "run_once" not in st.session_state:
    st.session_state.run_once = True
if st.session_state.run_once:
    st.balloons()
    st.session_state.run_once = False

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

st.title("🎂Happy Birthday Heru!🎉", text_alignment="center")
st.markdown(""" 

I hope your day is filled with smiles, laughter, and everything you love. 
You make things brighter just by being you, and I'm really glad I got to know you. 
May this year bring you happiness, success, health and maybe… a LOT OF TIME TO SLEEP (Please Sleep For Gods Sake 😭) 😁
            
I just wanted you to know that you're as special as they come.
And for some reason, you never fail to impress me — you are kind, open minded, and a truly genuine person 💫

I hope you succeed in whatever u want and may the world be kind to you. and may you always find joy in the little things.

            
I hope your birthday is gentle, happy, and filled with the kind of moments you enjoy most. 
You deserve all the gentle and beautiful moments, today and always. ✨🌷
            
Enjoy your Birthday! You deserve it all and more ❤️
Hope you have a wonderful day and an amazing year ahead! 🎉🎈
            
-- Your Random Friend 😊  
@BladeX

""", width="stretch")

def animatation(x):
    if x == 1:
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTY5MHd3ZnE5Y283ODQ5Nmd6MHBvemd5eTY0NzdsNTJicHAyenMwciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Mjcv3Dg6irEG6Bb9In/giphy.gif", width="content")
    elif x == 2:
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm1jMHE5anFoeDFsdnd4YmZycnY5eG5uNGdpbjl1bWMwZWo1enEwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pk9FMe6GyhgBaP9QhW/giphy.gif")

balloons = st.button("CLICK FOR MORE BALLOONS", on_click=st.balloons, type="primary", width="stretch")


st.success("This isnt much but its all i could manage in the time i had 😅 ENJOOOOOYYY HERU 😁 (and check ur telebirr acc)")

# if balloons:
#     st.balloons()


# st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXAwaWZvMG12YW1rbTZmZm9iOWJsbzExazF5OHBoZWh6M2w5cTBjZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bErElGdAHUmoE/giphy.gif", width="stretch")

# suprise = st.button("CLICK IF U LOVE ME 😉", width="stretch", type="primary")
# if suprise:
#     st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3Noenp3ZzhkeG5jOWZleWd3YjZhcmU0OXZ4Y3NkM3cwdXAxcXE3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dpSrm4cwUmCeQ/giphy.gif", width="stretch")
    


    