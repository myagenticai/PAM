import streamlit as st

# App Title
st.set_page_config(page_title="Meet PAM – Personality Assessment Mentor", layout="centered")
st.title("🌟 Meet PAM – Your Personality Assessment Mentor")
st.subheader("Helping Special Minds Shine 🌈")

# Agent Description
st.markdown("""
**PAM (Personality Assessment Mentor)** is here to help parents and children better understand themselves using a fun and friendly personality quiz.

At **Special Minds Unlocked**, we believe every child is uniquely gifted. PAM helps reveal those strengths using four simplified DISC personality styles:

- 🔴 **Forceful** *(Dominance)* – Bold and driven
- 🟡 **Friendly** *(Influence)* – Energetic and social
- 🟢 **Flowing** *(Steadiness)* – Calm and steady
- 🔵 **Factual** *(Conscientiousness)* – Thoughtful and precise

Answer these simple questions to discover your primary personality type.
""")

# Questions
st.markdown("### 🧠 Let’s Find Your Personality!")
questions = [
    ("When I want something...", ["I go get it", "I talk to people", "I wait my turn", "I plan it carefully"]),
    ("I feel best when...", ["I win", "I’m with friends", "I’m calm and comfy", "I do it right"]),
    ("When something's hard...", ["I push through", "I ask for help", "I keep trying", "I figure out the details"]),
    ("People say I’m...", ["A leader", "Fun", "Chill", "Smart"]),
    ("I like to...", ["Compete", "Talk and laugh", "Keep peace", "Solve puzzles"]),
    ("My room usually looks...", ["Busy", "Colorful", "Cozy", "Organized"]),
    ("If there’s a problem...", ["I fix it fast", "I get everyone together", "I stay calm", "I think through it"]),
    ("I like when things are...", ["Fast and exciting", "Social and upbeat", "Gentle and relaxed", "Clear and fair"]),
    ("When I’m upset...", ["I speak out", "I look for a hug", "I go quiet", "I shut down to think"]),
    ("I like group work if...", ["I’m in charge", "It’s fun", "We all get along", "Everyone follows rules"]),
    ("My energy is...", ["High and focused", "Big and friendly", "Steady and soft", "Quiet and thoughtful"]),
    ("When learning something new...", ["I want to master it", "I want it to be fun", "I take my time", "I want all the steps"]),
    ("I care about...", ["Winning", "Everyone having fun", "Everyone feeling good", "Everyone being fair"]),
    ("I enjoy...", ["Challenges", "Parties", "Peace", "Details"]),
    ("I’m most like...", ["A coach", "A performer", "A peacemaker", "A scientist"]),
]

# Track scores
types = ["Forceful", "Friendly", "Flowing", "Factual"]
scores = {t: 0 for t in types}

# Display questions
for i, (q, options) in enumerate(questions):
    st.markdown(f"**{i+1}. {q}**")
    answer = st.radio("", options, key=i)
    index = options.index(answer)
    scores[types[index]] += 1

# Results
if st.button("🔍 Show My Personality!"):
    primary = max(scores, key=scores.get)
    secondary = sorted(scores, key=scores.get, reverse=True)[1]

    st.markdown(f"### 🎉 Your Primary Personality: **{primary}**")
    st.markdown(f"### 🌟 Your Support Style: **{secondary}**")

    personality_data = {
        "Forceful": {
            "Strengths": "Driven, Determined, Brave",
            "Weaknesses": "Bossy, Impatient",
            "Connect": "Let them lead a project, keep it quick and to the point."
        },
        "Friendly": {
            "Strengths": "Social, Creative, Enthusiastic",
            "Weaknesses": "Distracted, Forgetful",
            "Connect": "Laugh, talk, smile, and let them express themselves."
        },
        "Flowing": {
            "Strengths": "Peaceful, Patient, Caring",
            "Weaknesses": "Too quiet, avoids change",
            "Connect": "Be calm, gentle, ask how they feel."
        },
        "Factual": {
            "Strengths": "Thoughtful, Precise, Honest",
            "Weaknesses": "Overthinks, Too serious",
            "Connect": "Give details, explain why, follow the rules."
        },
    }

    for style in [primary, secondary]:
        st.markdown(f"#### {style}")
        st.markdown(f"**Strengths:** {personality_data[style]['Strengths']}")
        st.markdown(f"**Weaknesses:** {personality_data[style]['Weaknesses']}")
        st.markdown(f"**Ways to Connect:** {personality_data[style]['Connect']}")

# Footer
st.markdown("---")
st.caption("🧩 Powered by PAM – Created for Special Minds Unlocked")

