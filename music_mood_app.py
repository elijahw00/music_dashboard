import streamlit as st
from textblob import TextBlob
from spotify_util import get_songs_by_mood

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

# Set up the Streamlit app
st.title("Music Mood Dashboard")
st.write("Tell us how you're feeling, and we'll suggest some songs!")
# Create a text input for the user to describe their mood
text_input = st.text_area("How are you feeling today?")

# Create a button to get music suggestions
if st.button("Get Music Suggestions"):
    if text_input:
        mood = analyze_mood(text_input)
        st.write(f"So, you're feeling {mood}. Let's find some music for you!")
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