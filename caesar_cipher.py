alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# range 벗어날 경우 대비, index 함수는 찾으려는 index의 첫 번째 값만 반환
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): # 필요한 parameter만큼 적어주기
    cipher_text = "" # 암호화할 문자를 저장할 단어
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def dencrypt(changed_text, shift_amount):
    plain_text = ""
    for letter in changed_text:
        position = alphabet.index(letter)
        original_position = position-shift_amount
        plain_text += alphabet[original_position]
    print(f"The encoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    dencrypt(changed_text=text, shift_amount=shift)