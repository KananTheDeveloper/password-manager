# Password Manager

A simple Password Manager application built with Python and Tkinter that allows users to generate strong passwords and securely save them.

## Features
- **Password Generator**: Generates strong, random passwords with letters, numbers, and symbols.
- **Save Passwords**: Stores website credentials securely in a local text file (`data.txt`).
- **Auto-Copy to Clipboard**: Automatically copies generated passwords for easy pasting.
- **Update Existing Credentials**: Allows updating stored passwords if the website and email already exist.
- **User-Friendly Interface**: Built using Tkinter for an intuitive graphical user interface (GUI).

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). You also need to install `pyperclip`:
```sh
pip install pyperclip
```

## Usage
1. Run the script:
   ```sh
   python PASSWORD_MANAGER.py
   ```
2. Enter the website, email/username, and password.
3. Click "Generate Password" to create a strong password.
4. Click "Add" to save the credentials.

## File Structure
```
password-manager/
├── PASSWORD_MANAGER.py  # Main application script
├── data.txt             # Stores saved passwords (created after first use)
├── logo.png             # Application logo
└── README.md            # Project documentation
```

## How It Works
- The application generates passwords randomly using letters, numbers, and symbols.
- The generated password is copied to the clipboard for convenience.
- Saved passwords are stored in `data.txt` in the format:
  ```
  website.com | user@example.com | P@ssw0rd123
  ```
- If a website and email already exist, the program prompts to update the password.

## Screenshot
![App Interface](logo.png)

## Future Improvements
- Encrypt stored passwords for better security.
- Implement a search feature to find saved credentials easily.
- Add a database instead of using a text file.

## License
This project is open-source and available under the **MIT License**.

