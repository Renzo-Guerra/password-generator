from PasswordGenerator import PasswordGenerator

algo = (PasswordGenerator()
        .set_length("3")
        .generate_password())

print(algo)