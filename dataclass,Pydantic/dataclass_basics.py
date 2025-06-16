# https://docs.python.org/3/library/dataclasses.html
# https://www.youtube.com/watch?v=CvQ7e6yUtnw

import random
import string 
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass(order=True, frozen=True) # Setting slots=True make the program faster by providing faster access to attributes
                                    # but results in problems if you use multiple inheritance
class Person:
    sort_index: int = field(init=False, repr=False) # init=False - Doesn't need to be initialized when creating a new object
                                                    # repr=False - When we print the object, this attribute will be not be printed
    character: str
    video_game: str
    age: int
    missions: list[str] | None = field(default_factory=list) # default_factory expects a Callable (function) - "list" assigns an empty list
                                                             # In order to assign a filled list, use (default_factory=lambda: ["help_villager"])
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        #self.sort_index = self.age                           # Works only if frozen=False for dataclass decorator (it is the default)
        object.__setattr__(self, "sort_index", self.age)   # As frozen=True so normal assignment is not possible


person1 = Person("V", "Cyberpunk 2077", 30)  # If kw_only=True in dataclass decorator, the initialization requires 
                                             # keyword arugments, so this line would have to be changed to 
                                             # Person(character="V", video_game="Cyberpunk 2077", age=30)
person2 = Person("Geralt", "Witcher", 200)
person3 = Person("Titus", "Space Marine", 300)

# person1.name = "Johnny Silverhand"         # Won't work as frozen=True so normal assignment is not possible

print(person1)
print(person2 > person1)