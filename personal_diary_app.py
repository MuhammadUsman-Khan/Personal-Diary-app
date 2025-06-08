import streamlit as st 
import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",      
        password="usmankhan",  
        database="personal_diary"
    )

def register():
    st.subheader("📝 Register")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")

    if st.button("Register"):
        if username.strip() == "" or password.strip() == "":
            st.error("Username or password cannot be empty.")
            return
        
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            st.error("User already exists.")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            st.success("User registered! You can log in.")

        cursor.close()
        conn.close()


def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Enter your username")
    password = st.sidebar.text_input("Entry your password", type="password")
    
    if username and password:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            stored_password = result[0]
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
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO diary_entries (username, entry) VALUES (%s, %s)", (username, entry))
        conn.commit()
        st.success("Entry saved successfully!")
        cursor.close()
        conn.close()

def view_entries(username):
    st.subheader("📚 View Entries")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, entry, timespan FROM diary_entries WHERE username = %s ORDER BY timespan DESC", (username,))
    entries = cursor.fetchall()
    cursor.close()
    conn.close()

    if not entries:
        st.info("No entries found.")
        return

    entry_map = {f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}": (entry_id, entry) for entry_id, entry, timestamp in entries}
    selected = st.selectbox("Select an entry to view/delete:", list(entry_map.keys()))

    if selected:
        entry_id, content = entry_map[selected]
        st.text_area("Entry", content, height=200)

        if st.button(f"Delete entry from {selected}"):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM diary_entries WHERE id = %s", (entry_id,))
            conn.commit()
            st.success("Entry deleted successfully.")
            cursor.close()
            conn.close()
    

def change_password(username):
    st.subheader("🔑 Change Password")
    current = st.text_input("Current Password", type= "password")
    new = st.text_input("New Password", type= "password")
    confirm = st.text_input("Confirm Password", type= "password")

    if st.button("Change Password"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        stored = cursor.fetchone()[0]

        if current != stored:
            st.error("Current password is incorrect.")
        elif new != confirm:
            st.error("New passwords do not match.")
        elif new.strip() == "":
            st.error("New password cannot be empty.")
        else:
            cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new, username))
            conn.commit()
            st.success("Password updated successfully.")

        cursor.close()
        conn.close()

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