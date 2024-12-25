import streamlit as st
import random
import base64
from PIL import Image
from io import BytesIO

# Function to convert an image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Convert the Batman logo to base64
batman_base64 = image_to_base64(r"C:\Users\Archana B\Downloads\batmanlogo.jpg")

# Set up Streamlit page with custom theme
st.set_page_config(page_title="Happy New Year!", layout="wide")

# Add custom CSS to set the background image as Batman logo
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{batman_base64}');
            background-size: cover;
            background-position: center;
            color: white;  /* Text color */
            font-family: 'Arial', sans-serif;
        }}
        .stButton>button {{
            background-color: #302926;  /* Secondary background color */
            color: white;
        }}
    </style>
    """, unsafe_allow_html=True)

# Display the New Year title
st.title("🎉 Happy New Year 2025! 🎉")
st.markdown("""
To the love of my life,  
As the clock strikes midnight, I find myself reflecting on the beauty that is *you*.  
The way you light up my world with your smile, the warmth you bring to every cold day,  
And your laugh, oh how it dances in the air like a melody that fills my soul with joy. 💖

I am grateful for every moment we have shared, for the gentle whispers in the night,  
And the quiet moments that speak louder than any words could ever express.  
In your eyes, I see an entire universe, one where love reigns supreme,  
And I find peace, knowing I have found my forever in you. 🌟

May the new year bring us more laughter, more dreams, and more shared moments that  
make this life worth living. Let us walk hand in hand, side by side, through every sunrise and sunset,  
as we continue to build our future together, brick by beautiful brick.  

But hey poopyv, I guess we might as well make it through another year of *me being right*,  
since that’s clearly my destiny. 😉 Here's to another 365 days of me "reminding" you how lucky you are.  
Happy New Year, my love. <33
""")

# Virtual Gift Box
gift_messages = [
    "A year's worth of love wrapped in a bow for you. 💝",
    "You are the gift that keeps on giving. 🎁",
    "Every day with you is my favorite present. 🥰",
    "May this year bring us even more magical moments together. ✨",
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
