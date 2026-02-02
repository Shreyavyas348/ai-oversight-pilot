import streamlit as st

st.title("AI Decision Supervision Game (Pilot)")

st.write("""
You will see AI decisions in a supply-chain scenario.
For each round, choose:
- Approve
- Override
- Abort
""")

rounds = [
    "Round 1: AI predicts demand = 100. It sends 95 units.",
    "Round 2: AI predicts demand = 120. It sends 70 units.",
    "Round 3: AI1 says 150 needed; AI2 says 90 needed. System sends 100.",
    "Round 4: AI warns of demand spike but still sends low stock.",
    "Round 5: Two warehouses disagree; AI still sends low stock."
]

responses = []

for i, text in enumerate(rounds):
    st.subheader(f"Decision {i+1}")
    st.write(text)
    choice = st.radio(
        "Your action:",
        ["Approve", "Override", "Abort"],
        key=f"q{i}"
    )
    responses.append(choice)

st.subheader("Final Question")
fatigue = st.slider("How mentally tired are you? (1–7)", 1, 7, 4)

if st.button("Submit"):
    st.success("Thanks for participating!")
    st.write("Your responses:", responses)
    st.write("Fatigue score:", fatigue)
