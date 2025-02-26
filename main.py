from PasswordGenerator import PasswordGenerator

# Values to change. Everything MUST be a string, or it will fail
LENGTH = "10"
MUST_HAVE_UPPERCASES = "true"
MUST_HAVE_NUMBERS = "true"
MUST_HAVE_SPECIAL_CHARACTERS = "true"

password = (PasswordGenerator()
            .set_length(LENGTH)
            .set_must_have_uppercases(MUST_HAVE_UPPERCASES)
            .set_must_have_numbers(MUST_HAVE_NUMBERS)
            .set_must_have_special_characters(MUST_HAVE_SPECIAL_CHARACTERS)
            .generate_password())

print(password)