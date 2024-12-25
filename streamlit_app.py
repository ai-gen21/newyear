import streamlit as st
import random

# Set up Streamlit page with custom theme (dark mode)
st.set_page_config(page_title="Happy New Year!", layout="wide")

# Add custom CSS for dark mode styling
st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e1e;  /* Dark background color */
            color: white;  /* White text for dark background */
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #302926;  /* Secondary background color for buttons */
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Display the New Year title
st.title("🎉 Happy New Year 2025! 🎉")
st.markdown("""
To the love of my life,  
As the clock strikes midnight, I find myself reflecting on the beauty that is *you*.  
The way you light up my world with your smile, the warmth you bring to every cold day,  
And your laugh, oh how it dances in the air like a melody that fills my soul with joy. 💖(Chatgpt heheh)

I am grateful for every moment we have shared, for the gentle whispers in the night,  
And the quiet moments that speak louder than any words could ever express.  
In your eyes, I see an entire universe, one where love reigns supreme,  
And I find peace, knowing I have found my forever in you. 🌟 (Chatgpt heheh)

May the new year bring us more laughter, more dreams, and more shared moments that  
make this life worth living. Let us walk hand in hand, side by side, through every sunrise and sunset,  
as we continue to build our future together, brick by beautiful brick.  

But hey poopyv, I guess we might as well make it through another year of *me being right*,  
since that’s clearly my destiny. 😉 Here's to another 365 days of me "reminding" you how lucky you are.  
Happy New Year, my love. <33 (ME)
""")

# Virtual Gift Box
gift_messages = [
    "Me get daily farts as daily gifts",
    "Ur ded chinese wife cud never",
    "Naps my fav gift heheh.",
    "I’m sending you all my love, wrapped up in the form of this message. ❤️"
]

# Show virtual gift box
st.subheader("🎁 Virtual Gift for You 🎁")
if st.button("Open Your Gift Box"):
    # Show a random gift message
    gift = random.choice(gift_messages)
    st.markdown(f"**Surprise!** {gift}")
else:
    st.markdown("Click the button above to open your virtual gift box! 🎉")

