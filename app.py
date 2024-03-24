import streamlit as st

header = st.header("Submission Form")

st.write("Enter a desired gloss and check the box for all true statements.")

gloss = st.text_input("Enter the proposed gloss here.", value="gloss")
auto = st.checkbox(f"{gloss.upper()} thinks on its own.")
mobile = st.checkbox(f"{gloss.upper()} can move through space without outside intervention.")
corp = st.checkbox(f"{gloss.upper()} has a concrete, physical body/form.")
count = st.checkbox(f"{gloss.upper()} is a discretely countable.")
cog = st.checkbox(f"{gloss.upper()} is a mental, psychedelic or otherwise cognitive phenomenon.")

per = st.checkbox(f"{gloss.upper()} is primarily perceived without sight.")

submit = st.button("Submit")

if submit:
    data = {"gloss": gloss.lower(),
            "autonomous": int(auto),
            "mobile": int(mobile),
            "corporeal": int(corp),
            "countable": int(count),
            "cognitive": int(cog),
            "visible": int(not per),
            "other_perception": int(per)}

    st.write(data)
