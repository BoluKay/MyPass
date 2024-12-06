# **MyPass - Password Manager**

## **Description**
MyPass is a secure password management application that allows users to:
- Register and log in securely.
- Store and manage sensitive data in a personal vault (CRUD operations).
- Generate strong, customizable passwords.
- Export vault data to a CSV file for backup.

---

## **Features**
1. **User Registration and Login**:
   - Secure user authentication with hashed passwords.
2. **Vault Management**:
   - Add, view, and delete sensitive data.
3. **Password Generator**:
   - Generate passwords with adjustable length and complexity (uppercase, numbers, special characters).
4. **Data Export**:
   - Export vault data as a CSV file for backup.
5. **Password Masking**:
   - View and toggle the visibility of stored passwords.

---

## **Installation**

### **Requirements**
- Python 3.x

### **Dependencies**
Install required Python libraries using `pip`:
```bash
pip install flask flask-bcrypt flask-wtf


Usage Instructions
Running the Application
Start the Flask app
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/

Key Routes
/register: Register a new user.
/login: Log in to your account.
/vault: View and manage your vault.
/vault/add: Add a new item to the vault.
/vault/delete/<item_id>: Delete an item from the vault.
/vault/export: Export vault data to a CSV file.
/password-generator: Generate a secure password.

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
└── README.md              # Documentation


Screenshots


- Registration Page:
  ![Registration Page]("C:\Users\bnkol\Downloads\MyPass\Images\Register_Page.png")

- Vault Page:
  ![Vault Page]("C:\Users\bnkol\Downloads\MyPass\Images\Vault_page.png")

- Password Generator:
  ![Password Generator]("C:\Users\bnkol\Downloads\MyPass\Images\Password_generator_page.png")

- Login Page:
  ![Login Page]("C:\Users\bnkol\Downloads\MyPass\Images\Register_Page.png")

-Add new vault item page:
![Add new vault item page]("C:\Users\bnkol\Downloads\MyPass\Images\Add_New_Vault_Item_page.png")





