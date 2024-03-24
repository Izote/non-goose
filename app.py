import streamlit as st
from st_supabase_connection import SupabaseConnection


@st.cache_resource(ttl=30)
def load_table():
    col_order = ["gloss", "autonomous", "mobile", "corporeal", "countable",
                 "subtle", "cognitive", "visible", "other_perception",
                 "transforms"]
    row_data = client.table("properties").select("*").execute().data

    return st.dataframe(row_data, column_order=col_order)


client = st.connection("conlang", type=SupabaseConnection)

display_header = st.header("Existing Properties")
st.write("This section displays properties currently stored in the database.")
df = load_table()

form_header = st.header("Submit a New Property")
st.write("Enter a desired gloss and check the box for all true statements.")
gloss = st.text_input("Enter the proposed gloss here.", value="gloss")

g = gloss.upper()
text = [f"{g} thinks on its own.",
        f"{g} can move through space of its own accord.",
        f"{g} has a concrete, physical body/form.",
        f"{g} can be counted as one of several discrete entities.",
        f"{g} can be described as delicate, light, small, soft, subtle, etc.",
        f"{g} exists only as a cognitive phenomenon.",
        f"{g} is primarily perceived without sight.",
        f"{g} can transform, radically changing its state."]

auto = st.checkbox(text[0])
mobile = st.checkbox(text[1])
corp = st.checkbox(text[2])
count = st.checkbox(text[3])
sub = st.checkbox(text[4])
cog = st.checkbox(text[5])
per = st.checkbox(text[6])
tran = st.checkbox(text[7])

password = st.text_input("Enter password for database write-access.",
                         type="password")

submit = st.button("Submit")

if submit:
    if password == st.secrets["PASSWORD"]:
        new = {"gloss": gloss.lower(),
               "autonomous": int(auto),
               "mobile": int(mobile),
               "corporeal": int(corp),
               "countable": int(count),
               "subtle": int(sub),
               "cognitive": int(cog),
               "visible": int(not per),
               "other_perception": int(per),
               "transforms": int(tran)}

        if gloss.lower() != "gloss":
            try:
                client.table("properties").insert(new, count="None").execute()
                st.write(f"Properties for `{gloss}` added to database!")
            except Exception as e:
                st.write(e)
    elif password == "" or password is None:
        st.write("Please enter the password!")
    else:
        st.write("Incorrect password!")
