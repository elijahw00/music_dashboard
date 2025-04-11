import os
import streamlit as st
from textblob import TextBlob
from spotify_util import get_songs_by_mood, get_current_user

st.title("Music Mood DashBoard")
st.write("Tell ur how you're feeling, and we''ll suggest some songs!")
#try getting user info
try:
    user = get_current_user()
    st.success(f"Logged in as {user['display_name']}")
except:
    st.warning("Please login to Spotify using the button below")
    login_url = auth_manager.get_authorize_url()
    st.markdown(f"[Login to Spotify]({login_user})")


#function to analyze the mood of user based on text input
def analyze_mood(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity #polarity from -1 to 1
    if polarity > 0.3:
        return 'happy'
    elif polarity < -0.3:
        return 'angry'
    else:
        return 'neutral'
    
# Create a text input for the user to describe their mood
text_input = st.text_area("How are you feeling today?")

# Create a button to get music suggestions
if st.button("Get Music Suggestions"):
    if text_input:
        mood = analyze_mood(text_input)
        st.write(f"So, you're feeling {mood}. Let's find some music for you!")
        try:

            # Get songs based on the analyzed mood
            songs = get_songs_by_mood(mood)
            st.subheader("Here are some song suggestions since you're feeling " + mood + ":")
            # Display the songs
            for song in songs:
                st.write(f"{song['name']} by {song['artist']}")
                st.image(song['image'], width=100)
                st.markdown(f"[Listen here]({song['url']})")
            else:
                st.warning("Please tell us how you're feeling!")
        except Exception as e:
            st.error("Something went wrong while fetching songs.")
            st.exception(e)
else:
    st.warning("Please tell us how you're feeling!")