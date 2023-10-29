import hashlib
import binascii
import time

# Function to hash a word using SHA-256
def hash_word(password):
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string

words = [line.strip().lower() for line in open('words.txt')]

'''
#Part 1

# Hash all the words and store them in a dictionary
hashed_words = {}
for word in words:
    hashed_words[word] = hash_word(word)



hash_list = [line.split(':') for line in open('passwords1.txt')]
hashmap = {}
for item in hash_list:
    username = item[0]
    hash_value = item[1]
    hashmap[username] = hash_value

# Create an empty dictionary to store username-password combinations
cracked_passwords = {}

# Iterate through the hashed words and username-hash pairs
for username, hash_value in hashmap.items():
    for word, password in hashed_words.items():
        if password == hash_value:
            print("found")
            cracked_passwords[username] = word

# Write the cracked username-password combinations to a file
with open('cracked1.txt', 'w') as output_file:
    for username, password in cracked_passwords.items():
        output_file.write(f"{username}:{password}\n")
'''

#Part 2

# Hash all the words and store them in a dictionary
hashed_words = {}
for word1 in words:
    for word2 in words:
        word = word1 + word2
        hashed_words[word] = hash_word(word)


hash_list = [line.split(':') for line in open('passwords2.txt')]
hashmap = {}
for item in hash_list:
    username = item[0]
    hash_value = item[1]
    hashmap[username] = hash_value
    
# Create an empty dictionary to store username-password combinations
cracked_passwords = {}

# Iterate through the hashed words and username-hash pairs
for username, hash_value in hashmap.items():
    for word, password in hashed_words.items():
        if password == hash_value:
            print('Found')
            cracked_passwords[username] = word

# Write the cracked username-password combinations to a file
with open('cracked2.txt', 'w') as output_file:
    for username, password in cracked_passwords.items():
        output_file.write(f"{username}:{password}\n")

