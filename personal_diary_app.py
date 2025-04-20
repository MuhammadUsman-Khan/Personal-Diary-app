import streamlit as st 
import os 
from datetime import datetime

def register():
    st.subheader("📝 Register")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")

    if st.button("Register"):
        if username.strip() == "" or password.strip() == "":
            st.error("Username or password cannot be empty.")
            return
        
        user_file = f"users/{username}.txt"
        if os.path.exists(user_file):
            st.error("User already exists.")
        else:
            os.makedirs("users", exist_ok=True)
            with open(user_file, "w") as f:
                f.write(password)
            os.makedirs(f"entries/{username}", exist_ok=True)
            st.success("User registered! You can log in.")

def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Enter your username")
    password = st.sidebar.text_input("Entry your password", type="password")
    
    user_file = f"users/{username}.txt"
    if username and password:
        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                stored_password = f.read().strip()
            if stored_password == password:
                return True, username
            else:
                st.sidebar.error("Incorrect password!")
        else:
            st.sidebar.error("User does not exist!")
    return False, None

def add_entry(username):
    st.subheader("📝 New Diary Entry")
    entry = st.text_area("What's on your mind today?", height=200)

    if st.button("Save Entry"):
        now = datetime.now()
        timespan = now.strftime("%Y-%m-%d_%H-%M-%S")
        folder = f"entries/{username}"
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/{timespan}.txt", "w") as f:
            f.write(entry)
        st.success(f"Entry saved at {timespan}")

def view_entries(username):
    st.subheader("📚 View Entries")
    folder = f"entries/{username}"
    if not os.path.exists(folder):
        st.info("No entries found.")
        return
    
    files = sorted(os.listdir(folder), reverse=True)
    if not files:
        st.info("No entries yet!")
        return
    
    selected = st.selectbox("Select an entry to view and delete:", files)
    if selected:
        with open(f"{folder}/{selected}", "r") as f:
            content = f.read()
        st.text_area("Entry", content, height=200)

        if st.button(f"Delete {selected}"):
            os.remove(f"{folder}/{selected}")
            st.success(f"Deleted {selected} successfully.")
    
def change_password(username):
    st.subheader("🔑 Change Password")
    current = st.text_input("Current Password", type= "password")
    new = st.text_input("New Password", type= "password")
    confirm = st.text_input("Confirm Password", type= "password")

    user_file = f"users/{username}.txt"
    if st.button("Change Password"):
        with open(user_file, "r") as f:
            stored = f.read().strip()

        if current != stored:
            st.error("Current password is incorrect.")
        elif new != confirm:
            st.error("New passwords do not match.")
        elif new.strip() == "":
            st.error("New password cannot be empty.")
        else:
            with open(user_file, "w") as f:
                f.write(new)
            st.success("Password updated successfully.")

def main():
    st.set_page_config("Personal Diary App", layout="centered")
    st.title("📖 Personal Diary (File-Based Users)")

    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
    if menu == "Register":
        register()

    else:
        logged_in, username = login()
        if logged_in:
            st.sidebar.success(f"Logged in as {username}")
            action = st.sidebar.radio("Choose action", ["Write Entry", "View or Delete Entry", "Change Password"])

            if action == "Write Entry":
                add_entry(username)
            elif action == "View or Delete Entry":
                view_entries(username)
            elif action == "Change Password":
                change_password(username)
        
        else:
            st.warning("Please log in to continue.")
    
    st.markdown("""<hr style="margin-top: 20px;">
    <center><p style='font-size:20px;'>🤖 Made by <strong>Muhammad Usman Khan</strong></p></center>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
