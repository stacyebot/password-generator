# 🔐 Secure Password Generator

A flexible, command-line password generator with customizable security options and password strength analysis.

## 📋 Features

- **Multiple Generation Modes**
  - Single password generation
  - Bulk password generation
  - Custom password with advanced options

- **Customizable Options**
  - Adjustable password length (4-128 characters)
  - Toggle uppercase letters
  - Toggle numbers/digits
  - Toggle special characters

- **Password Strength Analysis**
  - Real-time strength scoring (0-100)
  - Descriptive strength labels (Very Weak, Weak, Moderate, Strong)
  - Considers length and character variety

- **User-Friendly Interface**
  - Interactive menu-driven interface
  - Input validation and error handling
  - Clear, formatted output

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/password-generator.git
cd password-generator

# No additional dependencies required (uses only standard library)
```

### Usage
```bash
python password_generator.py
```

Follow the on-screen menu to:
1. Generate a single password with default settings
2. Generate multiple passwords at once
3. Create custom passwords with specific requirements
4. Exit the program

## 📖 Example

```
==================================================
        SECURE PASSWORD GENERATOR
==================================================

1. Generate Single Password
2. Generate Multiple Passwords
3. Custom Password (Advanced)
4. Exit
--------------------------------------------------
Enter your choice (1-4): 1
Enter password length (default 12): 16

==================================================
Your Generated Password:
--------------------------------------------------
  aB3xK9mP2qRt5nY8
--------------------------------------------------
Strength: Strong (85/100)
==================================================
```

## 🧪 Testing

This project includes comprehensive unit tests using PyTest.

### Running Tests
```bash
# Install pytest if you haven't already
pip install pytest

# Run all tests
pytest test_password_generator.py -v

# Run with coverage report
pytest test_password_generator.py --cov=password_generator
```

### Test Coverage
The test suite includes:
- ✅ Basic functionality tests (password generation, length validation)
- ✅ Character type tests (uppercase, digits, special characters)
- ✅ Edge case tests (minimum length, very long passwords)
- ✅ Multiple password generation tests
- ✅ Password strength calculation tests
- ✅ Integration tests

## 🏗️ Code Structure

```
password-generator/
├── password_generator.py      # Main application with PasswordGenerator class
├── test_password_generator.py # Comprehensive test suite
└── README.md                   # This file
```

### Key Components

**PasswordGenerator Class**
- `generate_password()` - Generate a single password with options
- `generate_multiple()` - Generate multiple passwords at once
- `calculate_strength()` - Analyze password strength (0-100 score)
- `get_strength_label()` - Get descriptive strength label

## 🔒 Security Notes

- Passwords are generated using Python's `random` module
- For cryptographic purposes, consider using `secrets` module instead
- Generated passwords are displayed in terminal - handle with care
- No passwords are stored or logged by this application

## 💡 Use Cases

- Creating secure passwords for new accounts
- Generating temporary passwords for users
- Testing password strength requirements
- Educational tool for understanding password security

## 🛠️ Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses standard library only)
- **Modules Used**: `random`, `string`
- **Testing Framework**: PyTest
- **Code Style**: PEP 8 compliant

## 📝 Future Enhancements

Potential features for future versions:
- [ ] Password policy validation
- [ ] Save passwords to encrypted file
- [ ] GUI interface
- [ ] Password entropy calculation
- [ ] Generate pronounceable passwords
- [ ] Integration with password managers

## 👤 Author

**Stacy Ebot**
- LinkedIn: [staceyebot](https://linkedin.com/in/staceyebot-3a44342b4)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**⭐ If you find this project useful, please consider giving it a star!**
