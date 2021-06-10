from random import randrange, choice
import string


VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


class RandomData:
    @classmethod
    def generate_word(cls, length: int) -> str:
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += choice(CONSONANTS)
            else:
                word += choice(VOWELS)
        return word

    @classmethod
    def generate_password(cls) -> str:
        number = str(randrange(1000, 9999))
        letters = cls.generate_word(randrange(8, 9))
        password = f"{letters}{number}"
        return password

    @classmethod
    def generate_mail(cls, mail_name: str) -> str:
        number = str(randrange(1000, 9999))
        name = cls.generate_word(randrange(3, 9))
        email = f"{name}-{number}{mail_name}"
        return email
