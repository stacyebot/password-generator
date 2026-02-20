"""
Secure Password Generator
A flexible command-line tool for generating secure passwords with customizable options.
Author: Stacy Ebot
"""

import random
import string


class PasswordGenerator:
    """Password generator with customizable security options."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation
    
    def generate_password(self, length=12, use_uppercase=True, use_digits=True, use_special=False):
        """
        Generate a random password with specified criteria.
        
        Args:
            length (int): Password length (minimum 4, default 12)
            use_uppercase (bool): Include uppercase letters (default True)
            use_digits (bool): Include numbers (default True)
            use_special (bool): Include special characters (default False)
        
        Returns:
            str: Generated password
        
        Raises:
            ValueError: If length is less than 4
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character pool based on options
        characters = self.lowercase  # Always include lowercase
        
        if use_uppercase:
            characters += self.uppercase
        if use_digits:
            characters += self.digits
        if use_special:
            characters += self.special
        
        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        return password
    
    def generate_multiple(self, count=5, **kwargs):
        """
        Generate multiple passwords at once.
        
        Args:
            count (int): Number of passwords to generate
            **kwargs: Password generation options (passed to generate_password)
        
        Returns:
            list: List of generated passwords
        """
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def calculate_strength(self, password):
        """
        Calculate password strength score (0-100).
        
        Args:
            password (str): Password to evaluate
        
        Returns:
            int: Strength score from 0 to 100
        """
        score = 0
        
        # Length scoring
        if len(password) >= 12:
            score += 25
        elif len(password) >= 8:
            score += 15
        else:
            score += 5
        
        # Character variety scoring
        if any(c.islower() for c in password):
            score += 15
        if any(c.isupper() for c in password):
            score += 20
        if any(c.isdigit() for c in password):
            score += 20
        if any(c in string.punctuation for c in password):
            score += 20
        
        return min(score, 100)
    
    def get_strength_label(self, score):
        """
        Get descriptive label for password strength.
        
        Args:
            score (int): Strength score
        
        Returns:
            str: Strength description
        """
        if score >= 80:
            return "Strong"
        elif score >= 60:
            return "Moderate"
        elif score >= 40:
            return "Weak"
        else:
            return "Very Weak"


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("        SECURE PASSWORD GENERATOR")
    print("="*50)
    print("\n1. Generate Single Password")
    print("2. Generate Multiple Passwords")
    print("3. Custom Password (Advanced)")
    print("4. Exit")
    print("-"*50)


def get_int_input(prompt, min_val=1, max_val=None):
    """Get validated integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            if max_val and value > max_val:
                print(f"Please enter a number <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_yes_no(prompt):
    """Get yes/no input from user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")


def main():
    """Main program loop."""
    generator = PasswordGenerator()
    
    print("\nWelcome to the Secure Password Generator!")
    print("Create strong, random passwords for your accounts.\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Generate single password with defaults
            length = get_int_input("Enter password length (default 12): ", min_val=4, max_val=128)
            password = generator.generate_password(length=length)
            
            print("\n" + "="*50)
            print("Your Generated Password:")
            print("-"*50)
            print(f"  {password}")
            print("-"*50)
            
            # Show strength
            score = generator.calculate_strength(password)
            strength = generator.get_strength_label(score)
            print(f"Strength: {strength} ({score}/100)")
            print("="*50)
        
        elif choice == '2':
            # Generate multiple passwords
            count = get_int_input("How many passwords? ", min_val=1, max_val=20)
            length = get_int_input("Password length (default 12): ", min_val=4, max_val=128)
            
            passwords = generator.generate_multiple(count=count, length=length)
            
            print("\n" + "="*50)
            print("Your Generated Passwords:")
            print("-"*50)
            for i, pwd in enumerate(passwords, 1):
                score = generator.calculate_strength(pwd)
                print(f"{i}. {pwd} ({score}/100)")
            print("="*50)
        
        elif choice == '3':
            # Custom password with all options
            print("\nCustom Password Generation")
            print("-"*50)
            length = get_int_input("Password length: ", min_val=4, max_val=128)
            use_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
            use_digits = get_yes_no("Include numbers? (y/n): ")
            use_special = get_yes_no("Include special characters? (y/n): ")
            
            password = generator.generate_password(
                length=length,
                use_uppercase=use_uppercase,
                use_digits=use_digits,
                use_special=use_special
            )
            
            print("\n" + "="*50)
            print("Your Custom Password:")
            print("-"*50)
            print(f"  {password}")
            print("-"*50)
            
            score = generator.calculate_strength(password)
            strength = generator.get_strength_label(score)
            print(f"Strength: {strength} ({score}/100)")
            print("="*50)
        
        elif choice == '4':
            print("\nThank you for using Secure Password Generator!")
            print("Stay safe online! 🔒\n")
            break
        
        else:
            print("\nInvalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
