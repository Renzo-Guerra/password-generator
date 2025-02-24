class PasswordGenerator:
  """
    Initiates the Object, by default the password will has:
    * __min_length: 8
    * __max_length: 14
    * __must_have_special_characters: False
    * __must_have_numbers: False
    * __must_have_uppercase: False
  """
  def __init__(self):
    self.__min_length = 8
    self.__max_length = 14
    self.__must_have_special_characters = False
    self.__must_have_numbers = False
    self.__must_have_uppercase = False
  
  def set_min_length(self, min_length):
    if min_length.isdigit() == False:
      print("Minimum length must be a positive number!")
    else:
      self.__min_length = min_length
    
    return self
  
  def set_max_length(self, max_length):
    if max_length.isdigit() == False:
      print("Maximum length must be a positive number!")
    else:
      self.__max_length = max_length
    
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

  def generate_password(self):
    return f"min_length: {self.__min_length}, max_length: {self.__max_length}, must_have_special_characters: {self.__must_have_special_characters}, must_have_numbers: {self.__must_have_numbers}, must_have_uppercase: {self.__must_have_uppercase}." 