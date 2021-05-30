#python code to encrypt and decrypt
from tkinter import *

root = Tk()
root.title("Modified Playfair Cipher")
entry = Entry(root,width=40)

def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
                      for sub in [lst1, lst2]]

def odd_numbers():
    start, end = 1,60
    number=[]
    # iterating each number in list
    for num in range(start, end + 1):

        # checking condition
        if num % 2 != 0:
            number.append(num)
    return number

def even_number():
    start, end = 1,40
    number = []
    # iterating each number in list
    for num in range(start, end + 1):# checking condition
        if num % 2 == 0:
            number.append(num)
    return number

def fibonacci():
    nterms =20
    count=0
    n1=0
    n2=100
    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

def generate_number(formula):
    numbers=[]
    formula_list=['even','odd','fibonacci']
    if formula=='even':
        numbers=even_number()
    elif formula=='odd':
        numbers=odd_numbers()
    elif formula=='fibonacci':
        numbers=fibonacci()
    return numbers


def Encryption(plaintext,key,flag,formula):
    ciphertext = []
    if flag == 0:
        n = 5
        numbers = generate_number(formula)
        final = [numbers[i * n:(i + 1) * n] for i in range((len(numbers) + n - 1) // n)]
        Alphabets = [0 for i in range(26)]
        Matrix = [[0 for i in range(5)] for i in range(5)]
        r, c = 0, 0
        # KEYWORD is stored into matrix
        for i in key:
            if Alphabets[ord(i) - 97] == 0:
                Alphabets[ord(i) - 97] = 1
                Matrix[r][c] = i
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        for i in range(26):
            if Alphabets[i] == 0:
                Alphabets[i] = 1
                if i == 9:
                    continue
                Matrix[r][c] = chr(i + 97)
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        Matrix_f = countList(Matrix, final)
        Matrix_f.append(Matrix[4][:])
        plaintext = plaintext.lower().replace(" ", "").replace('j', 'i')
        if len(plaintext) % 2 != 0:
            plaintext += "x"
        i = 0
        while i < len(plaintext):

            r1, c1, r2, c2 = -1, -1, -1, -1
            for row in range(9):
                for col in range(5):
                    if Matrix_f[row][col] == plaintext[i]:
                        r1, c1 = row, col
                    elif Matrix_f[row][col] == plaintext[i + 1]:
                        r2, c2 = row, col
            if r1 == r2:
                c1 = (c1 + 1) % 5
                c2 = (c2 + 1) % 5
            elif c1 == c2:
                r1 = (r1 + 1) % 9
                r2 = (r2 + 1) % 9
            else:
                temp = c1
                c1 = c2
                c2 = temp
            ciphertext.append(Matrix_f[r1][c1])
            ciphertext.append(Matrix_f[r2][c2])
            i = i + 2

    elif flag== 1:
        n = 4
        numbers = generate_number(formula)
        final = [numbers[i * n:(i + 1) * n] for i in range((len(numbers) + n - 1) // n)]
        Alphabets = [0 for i in range(26)]
        Matrix = [[0 for i in range(5)] for i in range(5)]
        r, c = 0, 0

        for i in key:
            if Alphabets[ord(i) - 97] == 0:
                Alphabets[ord(i) - 97] = 1
                Matrix[r][c] = i

                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        for i in range(26):
            if Alphabets[i] == 0:
                Alphabets[i] = 1
                if i == 9:
                    continue
                Matrix[r][c] = chr(i + 97)
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        Matrix_f = []
        for i, j in zip(Matrix, final):
            temp1 = i
            temp2 = j
            final_temp = countList(temp1, temp2)
            final_temp.append(temp1[4])
            Matrix_f.append(final_temp)
        plaintext = plaintext.lower().replace(" ", "").replace('j', 'i')
        if len(plaintext) % 2 != 0:
            plaintext += "x"
        ciphertext = []
        i = 0
        # algorithm for playfair cipher
        while i < len(plaintext):

            r1, c1, r2, c2 = -1, -1, -1, -1
            for row in range(5):

                for col in range(9):
                    if Matrix_f[row][col] == plaintext[i]:
                        r1, c1 = row, col

                    elif Matrix_f[row][col] == plaintext[i + 1]:
                        r2, c2 = row, col

            if r1 == r2:

                c1 = (c1 + 1) % 9
                c2 = (c2 + 1) % 9
            elif c1 == c2:
                r1 = (r1 + 1) % 5
                r2 = (r2 + 1) % 5
            else:
                temp = c1
                c1 = c2
                c2 = temp
            ciphertext.append(Matrix_f[r1][c1])
            ciphertext.append(Matrix_f[r2][c2])
            i = i + 2
    return ciphertext

def Decryption(ciphertext,key,flag,formula):
    plaintext = []
    if flag==0:
        n = 5
        numbers = generate_number(formula)
        final = [numbers[i * n:(i + 1) * n] for i in range((len(numbers) + n - 1) // n)]
        Alphabets = [0 for i in range(26)]
        Matrix = [[0 for i in range(5)] for i in range(5)]
        r, c = 0, 0
        # KEYWORD is stored into matrix
        for i in key:
            if Alphabets[ord(i) - 97] == 0:
                Alphabets[ord(i) - 97] = 1
                Matrix[r][c] = i
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        for i in range(26):  # itcsitgsblwspeiqdp
            if Alphabets[i] == 0:
                Alphabets[i] = 1
                if i == 9:
                    continue
                Matrix[r][c] = chr(i + 97)
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        Matrix_f = countList(Matrix, final)
        Matrix_f.append(Matrix[4][:])
        i = 0
        while i < len(ciphertext):
            r1, c1, r2, c2 = -1, -1, -1, -1
            for row in range(9):
                for col in range(5):
                    if Matrix_f[row][col] == ciphertext[i]:
                        r1, c1 = row, col
                    elif Matrix_f[row][col] == ciphertext[i + 1]:
                        r2, c2 = row, col
            if r1 == r2:
                c1 = (c1 - 1) % 5
                c2 = (c2 - 1) % 5
            elif c1 == c2:
                r1 = (r1 - 1) % 9

                r2 = (r2 - 1) % 9

            else:
                temp = c1
                c1 = c2
                c2 = temp

            plaintext.append(Matrix_f[r1][c1])
            plaintext.append(Matrix_f[r2][c2])
            i = i + 2
    elif flag==1:
        n = 4
        numbers = generate_number(formula)
        final = [numbers[i * n:(i + 1) * n] for i in range((len(numbers) + n - 1) // n)]
        Alphabets = [0 for i in range(26)]
        Matrix = [[0 for i in range(5)] for i in range(5)]
        r, c = 0, 0
        # KEYWORD is stored into matrix
        for i in key:
            if Alphabets[ord(i) - 97] == 0:
                Alphabets[ord(i) - 97] = 1
                Matrix[r][c] = i
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        for i in range(26):  # itcsitgsblwspeiqdp
            if Alphabets[i] == 0:
                Alphabets[i] = 1
                if i == 9:
                    continue
                Matrix[r][c] = chr(i + 97)
                if c == 4:
                    r = r + 1
                    c = 0
                else:
                    c = c + 1
        Matrix_f = []
        for i, j in zip(Matrix, final):
            temp1 = i
            temp2 = j
            final_temp = countList(temp1, temp2)
            final_temp.append(temp1[4])
            Matrix_f.append(final_temp)
        print(Matrix_f)
        i = 0
        while i < len(ciphertext):
            r1, c1, r2, c2 = -1, -1, -1, -1
            for row in range(5):
                for col in range(9):
                    if Matrix_f[row][col] == ciphertext[i]:
                        r1, c1 = row, col
                    elif Matrix_f[row][col] == ciphertext[i + 1]:
                        r2, c2 = row, col
            if r1 == r2:
                c1 = (c1 - 1) % 9
                c2 = (c2 - 1) % 9
            elif c1 == c2:
                r1 = (r1 - 1) % 5

                r2 = (r2 - 1) % 5

            else:
                temp = c1
                c1 = c2
                c2 = temp

            plaintext.append(Matrix_f[r1][c1])
            plaintext.append(Matrix_f[r2][c2])
            i = i + 2
    return plaintext
	
def outputter(ciphertext):
    entry.insert(END, ciphertext)

def encrypt():
    entry.delete(0, END)
    plaintext = variable.get()
    key = variable2.get()
    flag = variable4.get()
    flag = int(flag)
    formula= variable5.get()
    ciphertext = Encryption(plaintext, key,flag,formula)
    outputter(ciphertext)

def decrypt():
    entry.delete(0, END)
    ciphertext = variable3.get()
    key = variable2.get()
    flag = variable4.get()
    flag=int(flag)
    formula = variable5.get()
    ciphertext = list(ciphertext.split(" "))
    count = -1
    for i in ciphertext:
        count = count + 1
        if i.isnumeric():
            ciphertext[count] = int(i)
    plaintext = Decryption(ciphertext, key,flag,formula)
    outputter(plaintext)


label = Label(root, text="Encryption algorithm : Modified Playfair Cipher")
label.pack()

variable = StringVar()
variable2 = StringVar()
variable3 = StringVar()
variable4 = StringVar()
variable5 = StringVar()
plaintext = Entry(root, textvariable=variable,width=40)
key = Entry(root, textvariable=variable2,width=40)
ciphertext = Entry(root, textvariable=variable3,width=40)
flag = Entry(root, textvariable=variable4,width=40)
formula = Entry(root, textvariable=variable5,width=40)

label1 = Label(root, text="Enter Plaintext: ")
label1.pack()

plaintext.pack(expand="200")

label2 = Label(root, text="Key (text): ")
label2.pack()
key.pack(expand=50)

 
label3 = Label(root, text="Enter Ciphertext: ")
label3.pack()
ciphertext.pack(expand="200")

label5= Label(root, text="Enter flag value (0 or 1): ")
label5.pack()
flag.pack(expand="200")

label6= Label(root, text="Enter formula: ")
label6.pack()
formula.pack(expand="200")

label4 = Label(root, text="Output: ")
label4.pack()
entry.pack(expand=200)

encryptbutton = Button(text="Encrypt", command=encrypt)
decryptbutton = Button(text="Decrypt", command=decrypt)
encryptbutton.pack(expand="300")
decryptbutton.pack(expand="300")

root.mainloop()