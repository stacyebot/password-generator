"""
Tests for the Secure Password Generator
Author: Stacy Ebot
"""

import pytest
import string
from password_generator import PasswordGenerator


class TestPasswordGenerator:
    """Test suite for PasswordGenerator class."""
    
    @pytest.fixture
    def generator(self):
        """Create a PasswordGenerator instance for testing."""
        return PasswordGenerator()
    
    # Basic Functionality Tests
    def test_generator_initialization(self, generator):
        """Test that generator initializes correctly."""
        assert generator is not None
        assert isinstance(generator, PasswordGenerator)
    
    def test_password_is_string(self, generator):
        """Test that generated password is a string."""
        password = generator.generate_password()
        assert isinstance(password, str)
    
    def test_password_default_length(self, generator):
        """Test default password length is 12."""
        password = generator.generate_password()
        assert len(password) == 12
    
    def test_password_custom_length(self, generator):
        """Test password with custom length."""
        for length in [8, 16, 20, 32]:
            password = generator.generate_password(length=length)
            assert len(password) == length
    
    def test_password_not_empty(self, generator):
        """Test that password is not empty."""
        password = generator.generate_password()
        assert password != ""
        assert len(password) > 0
    
    # Character Type Tests
    def test_password_contains_lowercase(self, generator):
        """Test that password contains lowercase letters."""
        password = generator.generate_password(length=50)  # Longer for better chance
        assert any(c.islower() for c in password)
    
    def test_password_contains_uppercase(self, generator):
        """Test that password contains uppercase when enabled."""
        password = generator.generate_password(length=50, use_uppercase=True)
        # With length 50, we should almost certainly get an uppercase
        assert any(c.isupper() for c in password)
    
    def test_password_no_uppercase_when_disabled(self, generator):
        """Test that password has no uppercase when disabled."""
        password = generator.generate_password(use_uppercase=False, use_digits=False, use_special=False)
        assert not any(c.isupper() for c in password)
        assert all(c.islower() for c in password)
    
    def test_password_contains_digits(self, generator):
        """Test that password contains digits when enabled."""
        password = generator.generate_password(length=50, use_digits=True)
        assert any(c.isdigit() for c in password)
    
    def test_password_no_digits_when_disabled(self, generator):
        """Test that password has no digits when disabled."""
        password = generator.generate_password(use_digits=False, use_uppercase=False, use_special=False)
        assert not any(c.isdigit() for c in password)
    
    def test_password_contains_special_chars(self, generator):
        """Test that password contains special characters when enabled."""
        password = generator.generate_password(length=50, use_special=True)
        assert any(c in string.punctuation for c in password)
    
    def test_password_no_special_when_disabled(self, generator):
        """Test that password has no special chars when disabled."""
        password = generator.generate_password(use_special=False)
        assert not any(c in string.punctuation for c in password)
    
    # Edge Cases and Validation Tests
    def test_minimum_length_four(self, generator):
        """Test that passwords can be generated with minimum length 4."""
        password = generator.generate_password(length=4)
        assert len(password) == 4
    
    def test_invalid_length_raises_error(self, generator):
        """Test that length < 4 raises ValueError."""
        with pytest.raises(ValueError, match="Password length must be at least 4"):
            generator.generate_password(length=3)
    
    def test_very_long_password(self, generator):
        """Test generation of very long passwords."""
        password = generator.generate_password(length=100)
        assert len(password) == 100
    
    def test_passwords_are_different(self, generator):
        """Test that multiple generations produce different passwords."""
        password1 = generator.generate_password(length=16)
        password2 = generator.generate_password(length=16)
        # With length 16, passwords should virtually never be identical
        assert password1 != password2
    
    # Multiple Password Generation Tests
    def test_generate_multiple_returns_list(self, generator):
        """Test that generate_multiple returns a list."""
        passwords = generator.generate_multiple(count=5)
        assert isinstance(passwords, list)
    
    def test_generate_multiple_correct_count(self, generator):
        """Test that generate_multiple returns correct number of passwords."""
        for count in [1, 5, 10]:
            passwords = generator.generate_multiple(count=count)
            assert len(passwords) == count
    
    def test_generate_multiple_all_unique(self, generator):
        """Test that multiple passwords are all unique."""
        passwords = generator.generate_multiple(count=10, length=16)
        # All passwords should be unique
        assert len(passwords) == len(set(passwords))
    
    def test_generate_multiple_with_options(self, generator):
        """Test generate_multiple with custom options."""
        passwords = generator.generate_multiple(
            count=5,
            length=20,
            use_uppercase=True,
            use_digits=True,
            use_special=True
        )
        assert len(passwords) == 5
        for password in passwords:
            assert len(password) == 20
    
    # Password Strength Tests
    def test_calculate_strength_returns_int(self, generator):
        """Test that strength calculation returns an integer."""
        score = generator.calculate_strength("testpassword123")
        assert isinstance(score, int)
    
    def test_calculate_strength_range(self, generator):
        """Test that strength score is between 0 and 100."""
        passwords = [
            "abc",              # Very weak
            "password",         # Weak
            "Password123",      # Moderate
            "P@ssw0rd!Strong",  # Strong
        ]
        for password in passwords:
            score = generator.calculate_strength(password)
            assert 0 <= score <= 100
    
    def test_weak_password_low_score(self, generator):
        """Test that weak passwords get low scores."""
        weak_password = "abc"
        score = generator.calculate_strength(weak_password)
        assert score < 40
    
    def test_strong_password_high_score(self, generator):
        """Test that strong passwords get high scores."""
        strong_password = "Str0ng!P@ssw0rd#2024"
        score = generator.calculate_strength(strong_password)
        assert score >= 80
    
    def test_get_strength_label_returns_string(self, generator):
        """Test that strength label returns a string."""
        label = generator.get_strength_label(75)
        assert isinstance(label, str)
    
    def test_strength_labels_correct(self, generator):
        """Test that strength labels match score ranges."""
        assert generator.get_strength_label(90) == "Strong"
        assert generator.get_strength_label(70) == "Moderate"
        assert generator.get_strength_label(50) == "Weak"
        assert generator.get_strength_label(30) == "Very Weak"
    
    # Integration Tests
    def test_full_custom_password_generation(self, generator):
        """Test complete custom password generation workflow."""
        password = generator.generate_password(
            length=16,
            use_uppercase=True,
            use_digits=True,
            use_special=True
        )
        
        # Verify all requirements
        assert len(password) == 16
        assert isinstance(password, str)
        
        # Calculate and verify strength
        score = generator.calculate_strength(password)
        assert score > 0
    
    def test_only_lowercase_password(self, generator):
        """Test generation of lowercase-only password."""
        password = generator.generate_password(
            length=10,
            use_uppercase=False,
            use_digits=False,
            use_special=False
        )
        
        assert len(password) == 10
        assert all(c.islower() for c in password)


# Run tests with: pytest test_password_generator.py -v
