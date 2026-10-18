def encrypt(word, passkey):
  encrypted_word = ''
  
  while len(word) > len(passkey):
    passkey += passkey
  
  for i in range(len(word)):
    word_char = ord(word[i]) - ord('A')
    key_char = ord(passkey[i]) - ord('A')
    
    new_char = (word_char + key_char) % 26
    encrypted_word += chr(new_char + ord('A'))
    
  return encrypted_word

def decrypt(word, passkey):
  decrypted_word = ''
  
  while len(word) > len(passkey):
    passkey += passkey
  
  for i in range(len(word)):
    word_char = ord(word[i]) - ord('A')
    key_char = ord(passkey[i]) - ord('A')
    
    new_char = (word_char - key_char) % 26
    decrypted_word += chr(new_char + ord('A'))
    
  return decrypted_word

def main():
  passkey = ''

  while True:
    command = input().upper().split()
    
    if not command:
      print('ERROR Please enter a command')
      continue
    elif command[0] not in ['PASS', 'ENCRYPT', 'DECRYPT', 'QUIT']:
      print('ERROR Unknown command')
      continue
      
    if command[0] == 'QUIT':
          break
    elif len(command) != 2 or not command[1].isalpha():
      print('ERROR Input string should only consist of letters')
    elif command[0] == 'PASS':
      passkey = command[1]
      print('RESULT')
    elif command[0] == 'ENCRYPT':
      if passkey == '':
        print('ERROR Password not set')
      else:
        result = encrypt(command[1], passkey)
        print('RESULT', result)
    elif command[0] == 'DECRYPT':
        if passkey == '':
          print('ERROR Password not set')
        else:
          result = decrypt(command[1], passkey)
          print('RESULT', result)

if __name__ == '__main__':
  main()