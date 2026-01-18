# 📓 Personal Diary App

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FF5F1F?style=for-the-badge&logo=Firebase&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A simple and secure personal diary app built using **Streamlit** and **Firebase Firestore**. Users can register, log in, and manage their diary entries privately with a clean web interface.

## 🚀 Features

- **User Authentication** - Secure registration and login system
- **Create Entries** - Write and save diary entries with automatic timestamps
- **View Entries** - Browse through past diary entries organized by date
- **Delete Entries** - Remove unwanted entries
- **Password Management** - Change password functionality
- **Firebase Integration** - Cloud-based storage with Firestore
- **Streamlit UI** - Clean, intuitive web interface

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Framework**: Streamlit
- **Database**: Firebase Firestore (NoSQL)
- **Authentication**: Custom implementation with Firebase
- **Storage**: Cloud-based persistent storage

## 📁 Project Structure

```
Personal-Diary-app/
├── personal_diary_app.py    # Main Streamlit application
├── firebase_config.py        # Firebase configuration and initialization
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── personal-diary.json      # Local data file (gitignored)
└── .streamlit/
    └── secrets.toml         # Firebase secrets (gitignored)
```

## 📦 Installation

1. **Clone the repository**
```
git clone https://github.com/MuhammadUsman-Khan/Personal-Diary-app.git
cd Personal-Diary-app
```

2. **Install dependencies**
```
pip install -r requirements.txt
```

3. **Set up Firebase**
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Enable Firestore Database
   - Download your service account key JSON file
   - Create `.streamlit/secrets.toml` file with your Firebase credentials:

```
[firebase]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "your-private-key"
client_email = "your-client-email"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

4. **Run the application**
```
streamlit run personal_diary_app.py
```

## 💻 Usage

### Register
1. Select "Register" from the sidebar menu
2. Choose a unique username
3. Create a secure password
4. Click "Register" to create your account

### Login & Write
1. Enter your username and password in the sidebar
2. Once logged in, select "Write Entry" from the action menu
3. Type your diary entry in the text area
4. Click "Save Entry" to store it in the cloud

### View Entries
1. Select "View or Delete Entry" from the action menu
2. Browse entries from the dropdown (sorted by date)
3. Read your past entries
4. Optionally delete entries you no longer want

### Change Password
1. Select "Change Password" from the action menu
2. Enter your current password
3. Enter and confirm your new password
4. Click "Change Password" to update

## 🔒 Security Features

- **Password Storage**: Passwords stored in Firebase (consider adding hashing in production)
- **User Isolation**: Each user can only access their own entries
- **Cloud Security**: Firebase security rules protect data
- **Secrets Management**: Sensitive credentials stored in `.streamlit/secrets.toml` (gitignored)

## 📊 Firebase Collections

### Users Collection
```
users/
  └── {username}/
      └── password: string
```

### Entries Collection
```
entries/
  └── {entry_id}/
      ├── username: string
      ├── entry: string
      └── timestamp: datetime
```

## 🔮 Future Enhancements

- **Password Hashing** - Implement bcrypt or similar for secure password storage
- **Rich Text Editor** - Add formatting options for entries
- **Search Functionality** - Search entries by keywords
- **Export Feature** - Download entries as PDF or text files
- **Mood Tracking** - Add emotional tags to entries
- **Photo Attachments** - Upload images with diary entries
- **Entry Encryption** - End-to-end encryption for maximum privacy
- **Mobile App** - Native mobile version

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Developer

**Muhammad Usman Khan**

- GitHub: [@MuhammadUsman-Khan](https://github.com/MuhammadUsman-Khan)
- LinkedIn: [muhammad-usman-khan00](https://www.linkedin.com/in/muhammad-usman-khan00)
- Email: m.usman.khan.stu@gmail.com

---

<div align="center">

**Built with ❤️ using Streamlit and Firebase**

</div>
