# **MyPass - Password Manager**

## **Description**
MyPass is a secure password management application designed to simplify and enhance password management for users. It allows users to:
- Register and log in securely.
- Store and manage sensitive data in a personal vault (CRUD operations).
- Generate strong, customizable passwords.
- Export vault data to a CSV file for backup.

---

## **Features**
1. **User Registration and Login**:
   - Secure user authentication with hashed passwords using Flask-Bcrypt.
2. **Vault Management**:
   - Add, view, and delete sensitive data entries.
3. **Password Generator**:
   - Generate strong passwords with customizable length and complexity (uppercase, numbers, special characters).
4. **Data Export**:
   - Export vault data as a CSV file for easy backup.
5. **Password Masking**:
   - Toggle visibility for stored passwords in the vault.

---

## **Installation**

### **Requirements**
- Python 3.x

### **Dependencies**
Install required Python libraries using `pip`:
```bash
pip install flask flask-bcrypt flask-wtf

## **Usage Instructions**
Running the Application
Start the Flask app:

```bash
python app.py

Open your browser and navigate to: http://127.0.0.1:5000/


Key Routes
Route	              Description
/register	         Register a new user.
/login	                 Log in to your account.
/vault	                 View and manage your vault.
/vault/add	         Add a new item to the vault.
/vault/delete/<item_id>	 Delete an item from the vault.
/vault/export	         Export vault data to a CSV file.
/password-generator	 Generate a secure password.

Project Structure
MyPass/
├── app.py                 # Main application file
├── database.py            # Script to initialize database
├── password_generator.py  # Password generator logic
├── mypass.db              # SQLite database file
├── templates/             # HTML templates
│   ├── register.html
│   ├── login.html
│   ├── vault.html
│   ├── add_vault.html
│   ├── password_generator.html
├── Images/                # Screenshot images for documentation
│   ├── Register_Page.png
│   ├── Login_Page.png
│   ├── Vault_Page.png
│   ├── Password_Generator_Page.png
│   ├── Add_New_Vault_Item_Page.png
└── README.md              # Documentation
Acknowledgments
Flask Documentation: https://flask.palletsprojects.com/
SQLite Documentation: https://www.sqlite.org/
Bootstrap: https://getbootstrap.com/

