import csv  # to allow owkring on / with csv files.


def main():  # main subroutine to make it all work.

    while True:  # while loop to ensure correct shift int and number

        print("Welcome to the decryption station")  # welcome message

        try:  # try the following
            shift = int(input("Enter the 'shift' you want to apply"))  # takes in input and cast it to int
            if (shift > 0 and shift < 27):  # as long as its between 1 and 26 for a shift
                break  # break the loop to progress
            else:  # otherwise error message and loop
                print("Not a valid shift")

        except ValueError:  # if not a valid number entered
            print("invalid shift number")

    messages = []  # empty list for encoded messages

    with open('message.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            messages.append(row[0])

    decrypt = []
    for rows in messages:

        decrypted_text = ""

        # Normalize the shift to stay within 0-25
        shift = shift % 26

        char_idx = 0

        while char_idx < len(rows):
            char = rows[char_idx]
            if char.isalpha():
                # Determine if the character is uppercase or lowercase
                start = ord('A') if char.isupper() else ord('a')

                # 1. Convert char to 0-25 scale: (ord(char) - start)
                # 2. Subtract the shift
                # 3. Use modulo 25 to wrap around
                # 4. Convert back to ASCII: + start
                new_char = chr((ord(char) - start - shift) % 26 + start)
                decrypted_text += new_char
            else:
                # Keep spaces, numbers, and punctuation as they are
                decrypted_text += char

            char_idx += 1
        decrypt.append(decrypted_text)
        print(f"Original: {rows}")
        print(f"Decrypted: {decrypted_text}")

        # Exporting to CSV
    with open('decrypted_file.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write Data
        for l in decrypt:
            writer.writerow([l])


if __name__ == "__main__":
    main()