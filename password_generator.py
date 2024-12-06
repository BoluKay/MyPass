import random
import string

class PasswordGenerator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 12
        self.use_uppercase = True
        self.use_numbers = True
        self.use_special_chars = True

    def set_length(self, length):
        self.length = length

    def include_uppercase(self, use_uppercase):
        self.use_uppercase = use_uppercase

    def include_numbers(self, use_numbers):
        self.use_numbers = use_numbers

    def include_special_chars(self, use_special_chars):
        self.use_special_chars = use_special_chars

    def generate(self):
        characters = string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_numbers:
            characters += string.digits
        if self.use_special_chars:
            characters += "!@#$%^&*()"

        return ''.join(random.choice(characters) for _ in range(self.length))
