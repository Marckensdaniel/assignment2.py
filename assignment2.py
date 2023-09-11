
from datetime import datetime
import socket

class Assignment2:
    def __init__(self, year: int):
        self.year = year

    def tellAge(self, currentYear: int) -> None:
        age = currentYear - self.year
        print(f"Your age is {age}")

    def listAnniversaries(self):
        current_year = 2023
        anniversary_years = [i for i in range(10, currentYear - self.year + 1, 10)

        return anniversary_years
    
    def modifyYear(self, n: int):
        year_str = str(self.year)
        first_two_characters = year_str[:2] * n
        text_year = str(self.year * n)
        odd_positioned_characters = ''.join(text_year[i] for i in range(len(text_year)) if i % 2 == 0)

        return first_two_characters + odd_positioned_characters
    
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        
        first_character = string[0]
        if not first_character.islower():
            return False

        digit_count = sum(1 for char in string if char.isdigit())
        if digit_count != 1:
            return False

        return True
    
    @staticmethod
    def connectTcp(host: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            
            return True
        except (socket.error, socket.timeout):
            return False
