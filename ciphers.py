alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(job, message, offset):
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
            translated.append(f"Shift by {brute_i}: {caesar('e', message, brute_i)}")
    return translated

def rot13(message):
    return caesar('d', message, 13)

def atbash(message):
    translated = ''
    for i in message:
        if i.isalpha():
            new_char = alphabet[25-alphabet.index(i.lower())]
            translated += new_char if i.islower() else new_char.upper()
        else:
            translated += i
    return translated

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
                translated.append(f"({i},{j}): {affine('e', message, i,j)}")
    return translated

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

# def keyword_col(job, message, keyword):
#     def ceil(x):
#         return (int(x+1))

#     sort_descending = False

#     translated = []
#     letters, not_alpha = [], {}
#     for ind,i in enumerate(message):
#         if i.isalpha():
#             letters.append(i)
#         else:
#             not_alpha[ind] = i

#     my_keyword = [letter for letter in keyword if letter in alphabet]
#     char = len(my_keyword)
#     r = ceil(len(letters)/char)

#     block_count = (r*char) % len(letters)
#     table = [['' for j in range(char)] for i in range(r)]
#     for i in range(1,block_count+1):
#         table[r-1][-i] = None

#     keyword_dict = {}
#     order = []
#     repeat_count = 0
#     displacement_count, cell_count = 0, 0
    
#     for i in range(char):
#         keyword_dict[i] = my_keyword[i]
#     for i in sorted(my_keyword, reverse=sort_descending):
#         for j in keyword_dict:
#             if keyword_dict[j] == i:
#                 order.append(j)
#                 break

#     if job == 'e':
#         # Traverse table in row major order
#         for i in range(r):
#             for j in range(char):
#                 if table[i][j] != None:
#                     table[i][j] = letters[cell_count - displacement_count]    
#                 else:
#                     table[i][j] = None
#                     displacement_count += 1
#                 cell_count += 1
#         for j in order:
#             for i in range(r):
#                 if table[i][j] != None:
#                     translated.append(table[i][j])

#     if job == 'd':
#         # Traverse table in column major order
#         for j in order:
#             for i in range(r):
#                 if table[i][j] != None:
#                     table[i][j] = letters[cell_count - displacement_count]
#                 else:
#                     table[i][j] = None
#                     displacement_count += 1
#                 cell_count += 1
#         for i in range(r):
#             for j in range(char):
#                 if table[i][j] != None:
#                     translated.append(table[i][j])
    
#     for ind, i in not_alpha.items():
#         translated.insert(ind, i)
#     return ''.join(translated)