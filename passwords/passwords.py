import hashlib
import binascii
import time
from collections import defaultdict

'''
#Part 1

# Function to hash a word using SHA-256
def hash_word(password):
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string

words = [line.strip().lower() for line in open('words.txt')]


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





'''
#Part 2

def hash_word(password):
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string

words = [line.strip().lower() for line in open('words.txt')]

def import_passwords(filename):
    passwords_dict = {}
    for line in open(filename):
        username, password_hash = line.strip().split(':')
        if password_hash not in passwords_dict:
            passwords_dict[password_hash] = []
        passwords_dict[password_hash].append(username)
    return passwords_dict

# Create an empty dictionary to store username-password combinations
cracked_passwords = {}
f = open('cracked2.txt', 'w')

# Include an empty string in the list of words
words.append("")

passwords_dict = hash_word("passwords2.txt")
hash_count = 0
password_cracked = 0
# Iterate through the hashed words and username-hash pairs
for word1 in words:
    print(word1)
    for word2 in words:
        password = word1 + word2
        hashed_password = hash_word(password)
        hash_count += 1
        if hashed_password in passwords_dict:
            usernames = passwords_dict[hashed_password]
            print('Found')
            password_cracked += 1
            for username in usernames:
                cracked_passwords[username] = password
                print(username, password)
                print('hashes computed: ', hash_count)
                print('cracked: ', cracked_passwords)
                res = f"{username}:{password}\n"
                f.write(res)

f.close()
'''




#Part 3

# Function to hash a word using SHA-256
def hash_word(password):
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string

words = [line.strip().lower() for line in open('words.txt')]

def import_salted_passwords(filename):
    salted_passwords_dict = defaultdict(str)
    salt_list = []
    for line in open(filename):
        username = line.split(":")[0]
        salt = line.split("$")[2]
        rest_of_line = line.split("$")[3]
        salted_hash = rest_of_line.split(":")[0]
        salted_passwords_dict[salted_hash] = [username, salt]
        salt_list.append(salt)
    return salted_passwords_dict, salt_list

password_cracked = 0
hash_count = 0
passwords_dict, salt_list = import_salted_passwords("passwords3.txt")
num_passwords = len(salt_list)

f = open('cracked3.txt', 'w')

for word1 in words:
    for salt in salt_list:
        password = hash_word(salt+word1)
        hash_count += 1
        if passwords_dict.get(password) != None:
            password_cracked += 1
            username = passwords_dict[password][0]
            print(username, word1)
            print('hashes computed: ', hash_count)
            print('cracked: ', password_cracked)
            res = f"{username}:{word1}\n"
            f.write(res)
f.close()
