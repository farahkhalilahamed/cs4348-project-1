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

# Oct 18 4:10pm

This session, I worked on the logger program. It was fairly quick to implement; I decided I would keep it simple and just log any messages that come in for now, since the driver and encryption program should handle formatting and any edgecases.

Additionally, I've decided that if messages with only one word come in, and the command is not QUIT, they will not be logged. This could be inputs that are only one command or simply invalid inputs. I don't think it would be relevant to log these errors for the purpose of this project.

For the next session, I will implement my driver program. I will also connect to the logger and encryption files written through pipes.

# Oct 18 4:43pm

I took a short break and am now starting a new session. This time, I'm working on the driver implementation. One thing I realized I wasn't really clear on was what strings to store in history. I will be storing any inputs from the user, and the results after encrypting/decrypting. I also won't be storing the same string twice.

# Oct 18 7:28pm

I've got my driver program implemented, and it talks to the logger and encryption files through pipes using Python's subprocess module. The bulk of my time was mainly spent ensuring each input and output were validated, as well as formatting everything. I refered back to the assumptions I made in my initial planning session, so that was definitely helpful in my design. For the encryption/decryption, I kept my code about the same, since the logic was simply reverse of each other.

I ran into some challenges with implementing history. I think my previous sessions helped, but I also had to spend some time and actually walk through what inputs would be added to the history, and how those would be shown. One example would be if the user tried to encrypt a word before a password was set. Initially, I just saved every input and result at the same time to history. I also wanted to save any attempts without a password in the history, but also ensure that the user would be given an error about the missing password/key. I also didn't want duplicates, so I had to add extra checks and appends in those places.

Another thing I struggled with was also when to write to my logger. There were times when two different conditions could still needed to be logged the same way; for example, I wanted to log that the user tried to encrypt/decrypt a word regardless of whether it was successful. I originally had a lot of writes that did the same thing, so I had to clean it up and reorganize my code. I used the example Python process files given to help me write the overall pipe declarations and reads/writes.

I was also able to test my code properly. I made a list of edgecases, such as encrypting an empty string or selecting an invalid history selection (if there were 3 strings in history, inputting 6 should give an error). I tested each one for each command to find all edge cases. A test.log file is included as an example of the log messages for my testing. Another assumption I made as I tested was which errors would be logged on the file and which onces wouldn't. I made some assumptions prior as well, but I finally decided only errors with input validation for passwords and encryption/decryption strings would be tracked. So, something like an invalid history selection would not be logged, although the user will still be asked to select a valid entry.
