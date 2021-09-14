# Modified-Playfair-cipher

In our proposed system we have made an Encryption and Decryption mechanism where messages will be encoded and decoded using a modified Playfair cipher. In the modified Playfair cipher, we will add 2 more parameters along with the key to encode and decode the plaintext. These two parameters will be exchanged like keys and without knowledge of the two additional parameters, one cannot decrypt the ciphertext even if they have a key. This will help in assuring data integrity.
Figure 1 shows us the Proposed System Diagram for the Sender side.


Sender Side Proposed System Diagram
      Figure 2 shows us the Proposed System Diagram for the Receiver side. 
     
Receiver Side Proposed System Diagram 

Encryption and Decryption Rules

Take Keyword, Formula, and Flag value as the input data.
Generate 20 numbers using the formula.
If Flag = 0          (9 x 5 matrix)
Create sets of 5 numbers from 20 numbers generated.
Add these sets alternately with an alphabet matrix.
	If Flag = 1         (5 x 9 matrix)
Create sets of 4 numbers from 20 numbers generated.
Merge the rows of alphabet list and number list such that it starts with the alphabet and ends with the alphabet.
Encrypt the ciphertext by using the same rules as the Playfair cipher.
Decrypt by applying the same rules as Playfair cipher.
Illustration

Keyword: WorldPeace
Flag = 1
Formula value = “ even“
			5x 9 matrix
Rules:
	Rule1:Same row “next element
	Rule2:Same column : below element
	Rule3:Otherwise : diagonally opposite
Using the generated matrix and input parameter from user Encryption will be as
plaintext=Warwillend
Split plaintext into pair of two letters

wa
rw
il
le
nd

Encryption using Playfair cipher rules	
w a → r p (by rule3)
r w → 6 2(by rule1)
i l   → s c (by rule2)
l e  → o c (by rule3 )
n d →  t o (by rule3)
  Ciphertext= rp62scocto
For Decryption
	Rules:
		 Rule1:same row left element
		 Rule2:same column above element
		 Rule3:Otherwise = diagonally opposite
Split Cihertext into pair of two
      r p   l o   28 8   o c   t o
Applying decryption  rules on 5 x 9 matrix
r p →  w a(by rule3)
6 2 → r w(by rule1)
s c   → i l (by rule2)
o c  → l e (by rule3 )
t o → n d  (by rule3)
Keyword: WorldPeace
Flag = 0
Formula value = “even “

Plaintext = Warwillend
Split plaintext into pair of two letters
      w a    r w   i l  l e  n d 
Encryption using Playfair cipher rules	
w a → r p (by rule3)
r w → l o(by rule1)
i l   → 28 8 (by rule2)
l e  → o c (by rule3 )
n d →  t o (by rule3)
	 3.    Ciphertext=rplo288octo
	For Decryption
	Rules:
		 Rule1:same row: previous element
		 Rule2:same column: above element
		 Rule3:Otherwise: diagonally opposite
Split Cihertext into pair of two
       r p  l o  28 8  o c   t o
Applying decryption  rules on 9 x 5 matrix
r p →  w a(by rule3)
l o → r w(by rule1)
28 8   → i l (by rule2)
o c  → l e (by rule3 )
t o → n d  (by rule3)

![Screenshot (6)](https://user-images.githubusercontent.com/51523547/120109033-55d89300-c185-11eb-9dc3-4be05a8e8f33.png)
![Screenshot (7)](https://user-images.githubusercontent.com/51523547/120109036-57a25680-c185-11eb-85d2-84dcb841be0f.png)
![Screenshot (8)](https://user-images.githubusercontent.com/51523547/120109042-5a04b080-c185-11eb-80c8-4a3bb840ebe0.png)
![Screenshot (9)](https://user-images.githubusercontent.com/51523547/120109043-5b35dd80-c185-11eb-9d61-9aa27365e2cc.png)

