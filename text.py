caesar_cipher = ["Substitution Cipher", 1, 
"""The Caesar cipher is a substitution cipher that shifts the letters of the plaintext by a certain number of places. For example, with a shift of 3, A would be encrypted as D, B as E, and so on. Here is how the Caesar cipher works:

1. Decide on a shift value, this will be your encryption key.
2. For each letter in your plaintext, shift it over by the encryption key. So, if your key is 3, an 'A' becomes 'D', a 'B' becomes 'E', and so on. For letters at the end of the alphabet, loop back to the start. So, a 'Z' with a key of 1 becomes 'A'.
3. This gives you your ciphertext. To decrypt, just do the same process in reverse.""",
"""The Caesar cipher, one of the earliest known encryption techniques, dates back to Julius Caesar around 58 B.C., as recorded in his war commentaries. A basic substitution cipher, it replaces each letter in the plaintext by a letter a fixed number of positions down the alphabet. Despite its simplicity, it was effective in its time due to widespread illiteracy. Today, the Caesar cipher is far from secure and is typically used for educational purposes."""]

atbash_cipher = ["Substitution Cipher", 1, 
"""The Atbash cipher is a monoalphabetic substitution cipher where each letter of the plaintext is replaced by the letter in the same position from the end of the alphabet (A becomes Z, B becomes Y, C becomes X, etc.).

Here is how the Atbash cipher works:

1. Take each letter in your plaintext.
2. Replace it with the letter in the same position from the end of the alphabet. For example, 'A' becomes 'Z', 'B' becomes 'Y', and so on.
3. The result is your ciphertext. To decrypt, simply repeat the process.""",
"""The Atbash cipher is a simple substitution cipher that was used in the Hebrew language and can be traced back to the Bible. This monoalphabetic cipher works by replacing each letter in the plaintext with its mirror image in the alphabet—A becomes Z, B turns into Y, and so forth. Much like the Caesar cipher, Atbash has a security rating of 1 out of 5 due to its simplicity and predictability. Today, it's primarily employed in puzzle-solving and cryptographic education."""]

rot13_cipher = ["Substitution Cipher", 1, 
"""Here is how the ROT13 cipher works:

1. For each letter in your plaintext, replace it with the letter 13 places ahead in the alphabet. So, 'A' becomes 'N', 'B' becomes 'O', and so on. For letters at the end of the alphabet, loop back to the start. So, 'Z' becomes 'M'.
2. The result is your ciphertext. To decrypt, just apply the ROT13 operation again.""",
"""The ROT13 ("rotate by 13 places") is a special case of the Caesar cipher. It shifts each letter in the plaintext 13 places down the alphabet, effectively scrambling readable text. With a fixed shift of 13, ROT13 is its own inverse—applying it twice restores the original text. Its simplicity, predictability, and self-inversing property make it insecure but useful in situations like hiding movie spoilers in an online forum."""]

affine_cipher = ["Substitution Cipher", 2, 
"""The Affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.

Here is how the Affine cipher works:

1. First, assign each letter a numerical equivalent. For example, 'A' becomes 0, 'B' becomes 1, and so on.
2. Decide on two keys, say 'a' and 'b'. The key 'a' must be chosen such that 'a' and the size of the alphabet are coprime.
3. For each letter in your plaintext, convert it to a number, say 'x'. Then compute the value of '(ax + b) mod 26'. Replace your original letter with the letter represented by this result.
4. The result is your ciphertext. To decrypt, the receiver does the reverse process, using the modular multiplicative inverse of 'a'.""",
"""The Affine cipher is a type of monoalphabetic substitution cipher, where each letter in the plaintext is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. Its name originates from the affine function used in the encryption process, making it slightly more secure than basic substitution ciphers, although it remains vulnerable to frequency analysis attacks. It's commonly used for instructional purposes in teaching basic cryptography."""]

simple_columnar_transposition_cipher = ["Transposition Cipher", 2, 
"""The Simple Columnar Transposition Cipher is a method of encryption where the plaintext is written down in rows of a fixed length, and then read out again column by column, and the columns are chosen in some scrambled order.

Here is how the Simple Columnar Transposition Cipher works:

1. Decide on a number of columns, this will be your key.
2. Write your plaintext into rows with a number of characters that match your key.
3. Write out the ciphertext by reading down the columns, from left to right.
4. The result is your ciphertext. To decrypt, write the ciphertext into columns, then read off the plaintext in rows.""",
"""The Simple Columnar Transposition Cipher is a type of transposition cipher that arranges plaintext in rows and reads off the ciphertext in columns, one by one, in an ordered manner. This cipher saw use during World War I and II as a means of obscuring messages, providing a step-up in security over simple substitution ciphers."""]

keyword_columnar_cipher = ["Transposition Cipher", 3, 
"""The Keyword Columnar Transposition cipher is a variant of the simple columnar transposition cipher where the columns are ordered not by their original number, but by a keyword.

Here is how the Keyword Columnar Transposition Cipher works:

1. Decide on a keyword, this will be your key. The keyword should not contain any repeated characters.
2. Write your plaintext into rows, using the number of characters in the keyword as the row length.
3. Arrange the columns in the order of the alphabetical order of the letters in the keyword.
4. Write out the ciphertext by reading down the columns, in their rearranged order.
5. The result is your ciphertext. To decrypt, the receiver must rearrange the columns according to the keyword, and then read off the plaintext in rows.""",
"""The Keyword Columnar Transposition Cipher is a variant of the simple columnar transposition cipher. The primary difference lies in the ordering of columns, which is determined by a keyword. The characters of the keyword, when sorted alphabetically, determine the order in which the columns are read off. This method provides additional security by making the encryption key more complex, although it remains vulnerable to certain statistical attacks."""]

vigenere_cipher = ["Polyalphabetic Substitution Cipher", 3, 
"""The Vigenère Cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

Here is how the Vigenere Cipher works:

1. Decide on a keyword. This will be your key.
2. For each letter in your plaintext, shift it by the position in the alphabet of the corresponding letter in the keyword. For example, if the first letter in your keyword is 'B', shift the first letter of your plaintext by 1 place. If the second letter in your keyword is 'D', shift the second letter of your plaintext by 3 places, and so on. When you reach the end of the keyword, loop back to the start.
3. The result is your ciphertext. To decrypt, the receiver must know the keyword, and shift each letter in the ciphertext back by the position in the alphabet of the corresponding letter in the keyword.""",
"""The Vigenère cipher, developed in the 16th century by Blaise de Vigenère, is a polyalphabetic substitution cipher that uses a series of Caesar ciphers based on the letters of a keyword. This technique provides better security than monoalphabetic ciphers, as the same plaintext letter can be encrypted differently based on its position in the text. However, it is susceptible to frequency analysis attacks if the keyword is known or guessed correctly."""]

caesar_function = """
def caesar(job, message, offset=0):
    translated = ''
    if job in ['e', 'd']:
        offset = -offset if job == 'd' else offset
        for i in message:
            if i.isalpha():
                new_char = alphabet[(alphabet.index(i.lower())+offset) % 26] 
                translated += new_char if i.islower() else new_char.upper()
            else:
                translated += i
    else:
        translated = []
        for brute_i in range(1,26):
            translated.append(f"Shift by {brute_i}: {caesar('d', message, brute_i)}")
        return translated
"""

rot13_function = """
def rot13(message):
    return caesar('d', message, 13)
"""

atbash_function = """
def atbash(message):
    translated = ''
    for i in message:
        if i.isalpha():
            new_char = alphabet[25-alphabet.index(i.lower())]
            translated += new_char if i.islower() else new_char.upper()
        else:
            translated += i
    return translated
"""

affine_function = """
def affine(job, message, a, b):
    translated = ''
    if job == 'e':
        for i in message:
            if i.isalpha():
                new_char = alphabet[((alphabet.index(i.lower())*a) + b) % 26]
                translated += new_char if i.islower() else new_char.upper()
            else:
                translated += i
    elif job == 'd':
        x = 1
        while x % a != 0:
            x += 26
        x //= a
        for i in message:
            if i.isalpha():
                new_char = alphabet[((alphabet.index(i.lower()) - b)*x) % 26]
                translated += new_char if i.islower() else new_char.upper()
            else:
                translated += i
        
    else:
        translated = ['Format: (a,b): decrypted message']
        for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
            for j in range(1,27):
                translated.append(f"({i},{j}): {affine('d', message, i,j)}")
    return translated
"""

vigenere_function = """
def vigenere(job, message, keyword):
    translated, keyword = '', keyword.lower()
    counter, op = 0, (1 if job == 'e' else -1)
    for i in message:
        if i.isalpha():
            keyword_val, message_val = alphabet.index(keyword[counter % len(keyword)]), alphabet.index(i.lower())
            shift = (message_val + (op*keyword_val)) % 26
            translated += alphabet[shift] if i.islower() else alphabet[shift].upper()
            counter += 1
        else:
            translated += i
    return translated
"""

simple_columnar_function = """
def simple_col(job, message, char):
    def ceil(x):
        return (int(x+1))

    translated = []
    letters, not_alpha = [], {}
    for ind,i in enumerate(message):
        if i.isalpha():
            letters.append(i)
        else:
            not_alpha[ind] = i

    r = ceil(len(letters)/char)
    block_count = (r*char) % len(letters)
    table = [['' for j in range(char)] for i in range(r)]
    displacement_count, cell_count = 0,0
    for i in range(1,block_count+1):
        table[r-1][-i] = None

    if job == 'e':
        # Traverse table in row major order
        for i in range(r):
            for j in range(char):
                if table[i][j] != None:
                    table[i][j] = letters[cell_count - displacement_count]    
                else:
                    table[i][j] = None
                    displacement_count += 1
                cell_count += 1
        for j in range(char):
            for i in range(r):
                if table[i][j] != None:
                    translated.append(table[i][j])

    if job == 'd':
        # Traverse table in column major order
        for j in range(char):
            for i in range(r):
                if table[i][j] != None:
                    table[i][j] = letters[cell_count - displacement_count]
                else:
                    table[i][j] = None
                    displacement_count += 1
                cell_count += 1
        for i in range(r):
            for j in range(char):
                if table[i][j] != None:
                    translated.append(table[i][j])
    
    for ind, i in not_alpha.items():
        translated.insert(ind, i)
    return ''.join(translated)
"""

keyword_columnar_function = """
def keyword_col(job, message, keyword):
    def ceil(x):
        return (int(x+1))

    sort_descending = False

    translated = []
    letters, not_alpha = [], {}
    for ind,i in enumerate(message):
        if i.isalpha():
            letters.append(i)
        else:
            not_alpha[ind] = i

    char = len(keyword)
    r = ceil(len(letters)/char)

    block_count = (r*char) % len(letters)
    table = [['' for j in range(char)] for i in range(r)]
    for i in range(1,block_count+1):
        table[r-1][-i] = None

    keyword_dict = {}
    order = []
    repeat_count = 0
    displacement_count, cell_count = 0, 0
    
    for i in range(char):
        keyword_dict[i] = keyword[i]
    for i in sorted(keyword, reverse=sort_descending):
        for j in keyword_dict:
            if keyword_dict[j] == i:
                order.append(j)
                break

    if job == 'e':
        # Traverse table in row major order
        for i in range(r):
            for j in range(char):
                if table[i][j] != None:
                    table[i][j] = letters[cell_count - displacement_count]    
                else:
                    table[i][j] = None
                    displacement_count += 1
                cell_count += 1
        for j in order:
            for i in range(r):
                if table[i][j] != None:
                    translated.append(table[i][j])

    if job == 'd':
        # Traverse table in column major order
        for j in order:
            for i in range(r):
                if table[i][j] != None:
                    table[i][j] = letters[cell_count - displacement_count]
                else:
                    table[i][j] = None
                    displacement_count += 1
                cell_count += 1
        for i in range(r):
            for j in range(char):
                if table[i][j] != None:
                    translated.append(table[i][j])
    
    for ind, i in not_alpha.items():
        translated.insert(ind, i)
    return ''.join(translated)
"""

###

railway_cipher = ["Transposition Cipher", 2, 
"""The Rail Fence Cipher is a type of transposition cipher that gets its name from the way in which it's encoded. In the rail fence cipher, the plaintext is written downwards and diagonally on successive 'rails' of an imaginary fence, then moving up when we reach the bottom rail. When we reach the top rail, the message is written downwards again until the whole plaintext is exhausted. 

Here's how the Rail Fence Cipher works:

1. Decide on the number of rails, this will be your key.
2. Write your plaintext down and diagonally on successive rails of an imaginary fence.
3. Start moving up when you reach the bottom rail.
4. Write the ciphertext by reading the message in the order it appears on each rail, from top to bottom.
5. The result is your ciphertext. To decrypt, you would reverse the process."""]

playfair_cipher = ["Substitution Cipher", 3, 
"""The Playfair Cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. It employs a 5x5 matrix of letters, generated using a keyword. The rules of the cipher can handle pairs of letters in the plaintext differently, making it slightly more complex and harder to break than single-letter substitution ciphers.

Here's how the Playfair Cipher works:

1. Decide on a keyword (ignoring duplicate letters) and generate the 5x5 matrix. Fill the leftover spaces with the rest of the letters of the alphabet in order.
2. For each pair of letters in the plaintext, locate the letters in the matrix and apply the following rules:
   - If the letters appear on the same row of the matrix, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row).
   - If the letters appear on the same column of the matrix, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).
   - If the letters are not on the same row or column, replace them with the letters in the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.
3. The result is your ciphertext. To decrypt, you would reverse the process."""]

baconian_cipher = ["Substitution Cipher", 2, 
"""The Baconian Cipher is a method of steganography (hiding a secret message within an ordinary message) created by Francis Bacon. In this system, each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'.

Here's how the Baconian Cipher works:

1. Each letter of the plaintext is replaced by a 5-character code composed of 'A's and 'B's. For example, 'A' might be 'AAAAA', 'B' might be 'AAAAB', and so on.
2. These codes can then be hidden in a piece of writing by using two different typefaces, or by subtly changing the appearance of the text.
3. The result is your ciphertext. To decrypt, the receiver must know the code, and replace each group of five 'A's and 'B's with the corresponding letter."""]

polybius_square_cipher = ["Substitution Cipher", 2.5, 
"""The Polybius Square is a cipher that is a simple substitution cipher, and uses a square grid. The traditional square involves a grid of 5x5, and the letters i and j are merged into a single cell.

Here's how the Polybius Square Cipher works:

1. Generate a 5x5 grid and fill it with the letters of the alphabet, combining 'I' and 'J' into one cell.
2. For each letter in your plaintext, replace it with the two-digit number representing its row and column in the grid. For example, 'A' might be '11', 'B' might be '12', and so on.
3. The result is your ciphertext. To decrypt, the receiver must know the grid, and replace each pair of digits with the corresponding letter."""]

autokey_cipher = ["Polyalphabetic Substitution Cipher", 3.5, 
"""The Autokey Cipher is a cipher that is a type of polyalphabetic substitution cipher. It uses a keyword to determine the shift for the first few characters, but then it uses the plaintext itself to determine the shift for each subsequent character.

Here's how the Autokey Cipher works:

1. Decide on a keyword. This will be your key.
2. For the first few characters in your plaintext, shift them by the position in the alphabet of the corresponding letter in the keyword. For example, if the first letter in your keyword is 'B', shift the first letter of your plaintext by 1 place. If the second letter in your keyword is 'D', shift the second letter of your plaintext by 3 places, and so on.
3. For each subsequent character in your plaintext, shift it by the position in the alphabet of the corresponding letter in the plaintext. So if the fourth letter of your plaintext is 'E', shift the fourth letter by 4 places.
4. The result is your ciphertext. To decrypt, the receiver must know the keyword, and shift each letter in the ciphertext back by the position in the alphabet of the corresponding letter in the keyword or the plaintext, as appropriate."""]

adfgvx_cipher = ["Substitution and Transposition Cipher", 4, 
"""The ADFGVX cipher is a combination of a substitution and a transposition cipher and was used by the German Army during World War I. It uses a 6x6 grid of characters to substitute plaintext characters, and then a columnar transposition to rearrange the characters.

Here's how the ADFGVX Cipher works:

1. Create a 6x6 grid and fill it with the letters of the alphabet and the digits 0-9 in a mixed order based on a keyword.
2. Replace each letter of the plaintext with the two-letter combination in the grid corresponding to the row and column of the letter.
3. Perform a columnar transposition based on another keyword. This involves writing the letters out in rows of a fixed length, and then reordering the columns by sorting the keyword alphabetically.
4. The result is your ciphertext. To decrypt, the receiver must know the two keywords, reverse the columnar transposition, and replace each two-letter combination with the corresponding letter in the grid."""]