# Oct 17 9:35pm

Before I begin any coding, I am going to rewrite the project instructions in my own words. This is to make sure I understand the requirements, and hopefully it should help me figure out the steps to complete this project.

Essentially, this project creates an encryption/decryption system that a user would be able to use to encrypt different words and view their activity history as well using processes and pipes. The driver program is what starts the system and sends encryption information to the other two programs. It also stores all encrypted and decrypted strings as can display the history when prompted.

Based on the instructions and what has been mentioned by Dr. Salazar in class, I will make a few assumptions and notes to help with my coding. First is that it was mentioned in class that the history does not persistent. Thus, if a user quits the driver program and enters it again, the encryptions/decryptions from the previous session will not be displayed. Also, the history will maintain ANY attempts at encryption, including those that may be tried before a password is set. Second, the encrpytion program will always recieve input in uppercase. The driver program (or the user if testing the encrpytion program separately) will convert any lowercase letters to uppercase before giving it to the encryption program. Addtionally, since the Vigenere cypher only accepts letters, I will assume whitespace is invalid. Any inputs with whitespace will give an error message. Similarly, if an empty string is inputted when prompted for encryption/decryption, a message will be displayed and the user will be prompted to enter a proper string (but will not be taken back to the main menu). These are my current assumptions for this project, but others may arise as I work.

This project also asks for 3 programs:

1. logger - logs activity with timestamps. It starts logging when the driver program is run and keeps logging until the it recieves QUIT from the user. For each encryption/decryption, two different messages will be logged. The first will be the command the user chooses, along with the input to be encrypted. The second will be the resulting string, with information on whether the encryption was successful or gave an error. Setting passwords will be similar, except the password will NOT be explicitly logged. For checking history and quitting, only one message will be logged with the action that was taken. All activity will be stored in a log file.
2. encryption - takes commands in one line and outputs a response. The program will only accept the 4 given command types in the instructions as valid input. Anything else will throw an error. Similarly, responses will be of either type RESULT or ERROR.
3. driver - main program that the user talks to. The other two are executed by the driver automatically; not by the user. It will accept the name of the log file for the logger. On launch, it will pass that name to the logger program along with a message to log that the driver has started. The driver will also use pipes to communicate with the logger and encryption programs. When executed, it will display a menu to the user with the given commands. After each encrpytion/decrpytion, it will store the result in history.

For this project, I'm choosing to code in Python, mainly because I have some experience with writing process-based scripts in Python. It is also more concise and readable, so I can ensure the project requirements will be met and show how each program is separate.

In the next session, I'll begin coding. I'm thinking that I will start with the encryption program, then the logger, and finally the driver. I'm choosing to implement the encrpyion program first because it will be the core part of the project, and could influence how the other two programs will be written.

# Oct 18 12:51pm

As mentioned last session, this session I'm building the encryption program. My thinking for implementation is to first build the encrpytion/decrpytion funcionalities and make sure its accurate, and then format it properly to fit the project's requirements (using RESULT or ERROR).

# Oct 18 3:12pm

For this session, I worked on my encryption program. I built it to work with the given commands, and also tested edgecases, such as empty inputs or adding non-alphabet characters.

One question I ran into while coding was how to deal with inputs that only have a command (like PASS or ENCRYPT) with no input after. I'm thinking that if that edge case occurs, the program should output an ERROR message and wait for next input, rather than encrypting an empty string or erasing the current passkey.

Overall, this was a productive session. My encryption program works well and should be fairly simple to connect to the driver as well. I was also able to format my results to match the project instructions as well. Next session, I will continue with the plan I had in my initial planning, to implement the logger.

# Oct 18 3:25pm

I'm jumping directly into the next session here because I'm pretty focused on the project and I don't want to forget any ideas I had. For this session, I will be implementing the logger. For the timestamps, I can use Python's datetime module, and the user's encrpytion input for the action and message. I think I will test this with the encryption program to make sure it logs the activity properly, then add both to the driver in a future session. I don't think I will need to touch the encryption implementation too much for this session either.
