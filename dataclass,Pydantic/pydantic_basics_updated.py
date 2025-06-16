# https://docs.pydantic.dev/latest/concepts/validators/
# https://www.youtube.com/watch?v=Vj-iU-8_xLs (Github : https://github.com/ArjanCodes/2021-pydantic/blob/main/example.py)
# This file is an updated version of the code in the video as some functions have been deprecated

# pydantic module offers data validation which is not available in built-in dataclasses

from pydantic import BaseModel, field_validator, model_validator
import json
from typing import Optional


class ISBNMissingError(Exception):
    """ Custom error that is raised whether neither isbn_10 or isbn_13 are provided"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message        
        super().__init__(message)


class ISBN10FormatError(Exception):
    """ Custom error when the isbn_10 value is not valid"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message        
        super().__init__(message)


class Author(BaseModel):
    name: str
    verified: bool


class Book(BaseModel):
    title: str
    author:str
    publisher: str
    price: float
    isbn_10: Optional[str] = None
    isbn_13: Optional[str] = None
    subtitle: Optional[str] = None
    author2: Optional[Author] = None

    @model_validator(mode='before') # validate the entire data model
    @classmethod
    def check_isbn10_or_isbn13(cls, data): # 'data' has all the attributes of the class
        """
        Make sure either isbn_10 or isbn_13 is provided
        """
        if 'isbn_10' not in data and 'isbn_13' not in data:
            raise ISBNMissingError(data['title'], "Book should have an ISBN10 or ISBN13")
        
        return data


    @field_validator("isbn_10") # validate a particular attribute
    @classmethod
    def validate_isbn_10(cls, value: str) -> str: # 'value' is assigned the attribute that is given in 'field_validator' decorator
        """
        Validator to check if 'isbn_10' has a valid value
        """

        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value, "ISBN10 should be 10 digits")
        
        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        
        weighted_sum = sum((10 - i) * char_to_int(x) for i,x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(value, "ISBN10 digit sum should be divisible by 11")
        
        return value  
    
    
def main() -> None:

    try:
        with open("book_data.json") as file:
            data = json.load(file)
            books: list[Book] = [Book(**item) for item in data]
            print(books[0].model_dump(exclude={'subtitle'}))

    except FileNotFoundError as err:
        raise



if __name__ == "__main__":
    main()