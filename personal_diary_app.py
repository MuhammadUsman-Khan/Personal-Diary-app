import streamlit as st
from datetime import datetime
from firebase_config import db

def register():
    st.subheader("📝 Register")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")

    if st.button("Register"):
        if not username or not password:
            st.error("Username or password cannot be empty")
            return

        user_ref = db.collection("users").document(username)
        if user_ref.get().exists:
            st.error("User already exists")
        else:
            user_ref.set({"password": password})
            st.success("User registered successfully!")

def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if username and password:
        user_ref = db.collection("users").document(username)
        doc = user_ref.get()

        if doc.exists:
            stored_password = doc.to_dict()["password"]
            if stored_password == password:
                return True, username
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("User does not exist")

    return False, None

def add_entry(username):
    st.subheader("📝 New Diary Entry")
    entry = st.text_area("What's on your mind today?", height=200)

    if st.button("Save Entry"):
        if entry.strip() == "":
            st.error("Entry cannot be empty")
            return

        db.collection("entries").add({
            "username": username,
            "entry": entry,
            "timestamp": datetime.now()
        })
        st.success("Entry saved successfully!")

def view_entries(username):
    st.subheader("📚 View Entries")

    docs = db.collection("entries") \
        .where("username", "==", username) \
        .order_by("timestamp", direction="DESCENDING") \
        .stream()

    entries = [(doc.id, doc.to_dict()) for doc in docs]

    if not entries:
        st.info("No entries found.")
        return

    entry_map = {
        e[1]["timestamp"].strftime("%Y-%m-%d %H:%M:%S"): e
        for e in entries
    }

    selected = st.selectbox("Select an entry", entry_map.keys())

    if selected:
        doc_id, data = entry_map[selected]
        st.text_area("Entry", data["entry"], height=200)

        if st.button("Delete Entry"):
            db.collection("entries").document(doc_id).delete()
            st.success("Entry deleted successfully.")

def change_password(username):
    st.subheader("🔑 Change Password")
    current = st.text_input("Current Password", type="password")
    new = st.text_input("New Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Change Password"):
        user_ref = db.collection("users").document(username)
        stored = user_ref.get().to_dict()["password"]

        if current != stored:
            st.error("Current password is incorrect")
        elif new != confirm:
            st.error("Passwords do not match")
        elif not new:
            st.error("Password cannot be empty")
        else:
            user_ref.update({"password": new})
            st.success("Password updated successfully")

def main():
    st.set_page_config("Personal Diary App", layout="centered")
    st.title("📖 Personal Diary")

    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

    if menu == "Register":
        register()
    else:
        logged_in, username = login()

        if logged_in:
            st.sidebar.success(f"Logged in as {username}")
            action = st.sidebar.radio(
                "Choose action",
                ["Write Entry", "View or Delete Entry", "Change Password"]
            )

            if action == "Write Entry":
                add_entry(username)
            elif action == "View or Delete Entry":
                view_entries(username)
            else:
                change_password(username)
        else:
            st.warning("Please log in to continue")

    st.markdown("""<hr>
    <center><p style='font-size:18px;'>🤖 Made by <strong>Muhammad Usman Khan</strong></p></center>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
