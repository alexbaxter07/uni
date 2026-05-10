import csv

# open message.csv
with open("message.csv", newline="") as f:

    reader = csv.reader(f)

    encrypted_message = ""

    for row in reader:

        for item in row:
            encrypted_message = encrypted_message + item

print("")
print("Encrypted Message:")
print(encrypted_message)
print("")

# get shift value
while True:

    try:
        shift = int(input("Please enter the shift value: "))

        break

    except ValueError:
        print("Please enter a number.")

decrypted_message = ""

index = 0

# decrypt using while loop
while index < len(encrypted_message):

    character = encrypted_message[index]

    # uppercase letters
    if character.isupper():

        new_character = chr((ord(character) - 65 - shift) % 26 + 65)

        decrypted_message = decrypted_message + new_character

    # lowercase letters
    elif character.islower():

        new_character = chr((ord(character) - 97 - shift) % 26 + 97)

        decrypted_message = decrypted_message + new_character

    # spaces and special characters
    else:

        decrypted_message = decrypted_message + character

    index = index + 1

print("")
print("Decrypted Message:")
print(decrypted_message)

# save decrypted file
with open("decrypted_file.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([decrypted_message])

print("")
print("Decrypted message saved to decrypted_file.csv")