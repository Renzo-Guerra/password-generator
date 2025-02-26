from random import randint

class PasswordGenerator:
  __MIN_LENGTH_ALLOWED = 6
  __DEFAULT_LENGTH = 8

  """
    Initiates the Object, by default the password will has:
    * __min_length: 8
    * __must_have_special_characters: False
    * __must_have_numbers: False
    * __must_have_uppercase: False
  """
  def __init__(self):
    self.__length = self.__DEFAULT_LENGTH
    self.__must_have_special_characters = False
    self.__must_have_numbers = False
    self.__must_have_uppercase = False
  
  def set_length(self, min_length):
    if min_length.isdigit() == False:
      print("Minimum length must be a positive number!")
    elif int(min_length) < self.__MIN_LENGTH_ALLOWED:
      print(f"Minimum length must be at least {self.__MIN_LENGTH_ALLOWED}!")
    else:  
      self.__length = int(min_length)
    return self
  
  def set_must_have_special_characters(self, must_have_special_characters):
    must_have_special_characters = must_have_special_characters.strip().lower()

    if must_have_special_characters not in ("true", "false"):
      print("To specify whether it must has special characters you need to type 'true' or 'false'.")
    else:
      self.__must_have_special_characters = must_have_special_characters == "true"
    
    return self
  
  def set_must_have_numbers(self, must_have_numbers):
    must_have_numbers = must_have_numbers.strip().lower()

    if must_have_numbers not in ("true", "false"):
      print("To specify whether it must has numbers you need to type 'true' or 'false'.")
    else:
      self.__must_have_numbers = must_have_numbers == "true"

    return self

  def set_must_have_uppercase(self, must_have_uppercase):
    must_have_uppercase = must_have_uppercase.strip().lower()

    if must_have_uppercase not in ("true", "false"):
      print("To specify whether it must has uppercases you need to type 'true' or 'false'.")
    else:
      self.__must_have_uppercase = must_have_uppercase == "true"

    return self

  def __get_random_lowercase(self):
    return chr(randint(97, 122))
  
  def __get_random_uppercase(self):
    return self.__get_random_lowercase().upper()
  
  def __get_random_digit(self):
    return chr(randint(48, 57))

  def __get_random_special_character(self):
    pool = []
    pool.extend(range(33, 48))
    pool.extend(range(58, 65))
    pool.extend(range(91, 97))
    pool.extend(range(123, 127))

    return chr(pool[randint(0, len(pool)-1)]) 

  def generate_password(self):
    # Initialize the password with empty characters
    password = [''] * self.__length
    index_pool_remaining = list(range(len(password)))
    
    divided_by = 1
    
    if(self.__must_have_numbers):
      divided_by += 1
    if(self.__must_have_special_characters):
      divided_by += 1
    if(self.__must_have_uppercase):
      divided_by += 1

    amount_per_group = int(self.__length / divided_by)

    if self.__must_have_numbers:
      for _ in range(amount_per_group):
        index = randint(0, len(index_pool_remaining)-1)
        password[index_pool_remaining[index]] = self.__get_random_digit()
        index_pool_remaining.pop(index)

    if self.__must_have_uppercase:
      for _ in range(amount_per_group):
        index = randint(0, len(index_pool_remaining)-1)
        password[index_pool_remaining[index]] = self.__get_random_uppercase()
        index_pool_remaining.pop(index)
    
    if self.__must_have_special_characters:
      for _ in range(amount_per_group):
        index = randint(0, len(index_pool_remaining)-1)
        password[index_pool_remaining[index]] = self.__get_random_special_character()
        index_pool_remaining.pop(index)

    for _ in range(len(index_pool_remaining)):
      _index = len(index_pool_remaining)-1
      password[index_pool_remaining[_index]] = self.__get_random_lowercase()
      index_pool_remaining.pop()

    return "".join(password)