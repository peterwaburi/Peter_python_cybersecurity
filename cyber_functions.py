from cryptography.fernet import Fernet

# genrate a key
key =""

key =Fernet.generate_key()
# print(key)
# original message 
print(key)


message ="I love cybersecurity"
print(message)

# create cypher oblecy with is used to encrypt the message 
cypher=Fernet(key)

# use the cypher to encrypt the message
encrypted_message =cypher.encrypt(message.encode())
print(encrypted_message)

# decrption
decrypted_message = cypher.decrypt(encrypted_message)
print(decrypted_message.decode())


# Hashing 
import hashlib
def hashpassword(password):
    # craete the hasher
    hasher =hashlib.sha256()

    # use hasher to hash the password 
    hasher.update(password.encode())

    # get the hashed password 
    hashed_password = hasher.hexdigest()

    return hashed_password

hashed_passowrd = hashpassword("admin1234")
print(f"The hashed password is :{hashed_passowrd}")


def verifyHash(input_password, hash_value):
    hashed_input_password =hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_input_password ==hash_value

print(verifyHash("Admin1234", hashed_passowrd))