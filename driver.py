from subprocess import Popen, PIPE
import sys

def show_history(history):
  print('\n-------------------------------------------------------------')
  print('                          History                              ')
  print('-------------------------------------------------------------\n')

  # items = []
  # for entry in history:
  #   items.append(entry['input'])

  #   if not entry['result'].startswith('Error:'):
  #       items.append(entry['result'])
  
  if not history:
    print('No history available.')

  for i, item in enumerate(history, start=1):
    print(f'{i}. {item}')

  print(f'{len(history) + 1}. (Go Back)')
  print('\n-------------------------------------------------------------')

  while True:
    selection = input('Enter number to select string: ').strip()

    if selection.isdigit():
        index = int(selection)

        if 1 <= index <= len(history):
            return history[index - 1]

        elif index == len(history) + 1:
            return None
          
    print('ERROR Invalid history selection')

def main():
  if len(sys.argv) != 2:
    print('ERROR Enter python3 driver.py <log_filename>')
    return
  
  encryption = Popen([sys.executable, 'encrypt.py'], stdout=PIPE, stdin=PIPE, text=True)
  logger = Popen([sys.executable, 'logger.py', sys.argv[1]], stdin=PIPE, text=True)
  
  logger.stdin.write('START Logging Started.\n')
  logger.stdin.flush()
  
  history = []
  
  while True:
    print('\n-------------------------------------------------------------')
    print('                          Menu                               ')
    print('-------------------------------------------------------------\n')
    print('password - set password for encryption/decryption')
    print('encrypt  - encrypt string')
    print('decrypt  - decrypt string')
    print('history  - show history')
    print('quit     - exit program')
    print('\n-------------------------------------------------------------\n')
    
    command = input('Enter Command: ').upper()
    
    if command == 'QUIT':
      break
    # PASS ---------------------------------------------------------------------------
    elif command == 'PASSWORD':
      use_history = input('Would you like to use history? (y/n) ').upper()
      if use_history == 'Y':
          password = show_history(history)

          if password is None:
              password = input('Enter password: ').strip()
          elif password == 'INVALID':
              continue
      else:
          password = input('Enter password: ').strip()
      
      logger.stdin.write('SET_PASSWORD Setting passkey.\n')
      logger.stdin.flush()
      
      if not password.isalpha():
        error_message = 'Password should only consist of letters.'
        print(f'ERROR {error_message}')
        logger.stdin.write(f'SET_PASSWORD Error: {error_message}\n')
        logger.stdin.flush()
      else:
        encryption.stdin.write(f'PASS {password}\n')
        encryption.stdin.flush()

        response = encryption.stdout.readline().strip()

        if response == "RESULT":
            print('Password set successfully.')
            logger.stdin.write('SET_PASSWORD Success.\n')
            logger.stdin.flush()
        else:
            print(response)
            logger.stdin.write(f'SET_PASSWORD Error: {response}\n')
            logger.stdin.flush()
    # ENCRYPT ---------------------------------------------------------------------------
    elif command == 'ENCRYPT':
        use_history = input('Would you like to use history? (y/n) ').upper()

        if use_history == 'Y':
            word = show_history(history)

            if word is None:
                word = input('Enter string to encrypt: ').strip()
            elif word == 'INVALID':
                continue
        else:
            word = input('Enter string to encrypt: ').strip()
        
        logger.stdin.write(f'ENCRYPT {word}\n')
        logger.stdin.flush()
                    
        if not word.isalpha():
            error_message = 'Input string should only consist of letters.'
            print(f'ERROR {error_message}')
            logger.stdin.write(f'ENCRYPT Error: {error_message}\n')
            logger.stdin.flush()
        else:
            encryption.stdin.write(f'ENCRYPT {word}\n')
            encryption.stdin.flush()

            response = encryption.stdout.readline().strip()

            if response.startswith('RESULT '):
                result = response[len('RESULT '):]
                print(f'Result: {result}')

                if word not in history:
                  history.append(word.upper())
                if result not in history:
                  history.append(result.upper())

                logger.stdin.write(f'ENCRYPT Success: {result}\n')
                logger.stdin.flush()
            else:
                print(f'{error_message}')

                if word not in history:
                  history.append(word.upper())
                if result not in history:
                  history.append(result.upper())

                logger.stdin.write(f'ENCRYPT Error: {error_message}\n')
                logger.stdin.flush()
    # DECRYPT ---------------------------------------------------------------------------
    else:
      print('ERROR Invalid command')

  logger.stdin.write('QUIT \n')
  logger.stdin.flush()
  logger.stdin.close()
  logger.wait()

  encryption.stdin.write('QUIT\n')
  encryption.stdin.flush()
  encryption.stdin.close()
  encryption.wait()
    

if __name__ == '__main__':
  main()