# Project 1 README

This project implements a command-line application to take in strings and encrypt/decrypt them using the Vigenere cipher. Users can set passkeys, encrypt/decrypt strings, and view history. There are 3 separate programs for encryption, logging activity, and a driver.

## Files

**driver.py:** the main program that talks to the user. It communicates with the other two files via pipes and handles input validation, history, errors, and formatting.
**encrypt.py:** handles all encryption logic, including setting passkeys. It reads commands from the driver and then sends back a resulting string or error message.
**logger.py:** logs all activity done by the driver and encryption programs, with the exception of passwords which are never directly logged. It includes timestamps for each action taken, including starting and exiting the driver.

## How to Run

# Prerequisites

- Python 3 installed (I wrote this program in Python 3.14, specifically)
- All files should be in the same directory

# To Run

1. Open terminal and navigate to project directory

```
cd project1
```

2. To run the driver program:

```
python3 driver.py <logfile.log>
```

Replace `<logfile.log>` with the name of the file the logger will record messages in. 3. Follow the menu display to set passwords, view history, encrypt/decrypt, and quit the program.

The driver launches encrypt.py and logger.py as subprocesses, so both files must be present in the same directory.

## Other Notes

- Passwords and strings must contain only letters to be considered valid inputs
- Any invalid will be rejected, and the user shown an error message
- Since the requirements of this projects (and the cipher) require input to be case insensitive, all strings are converted to uppercase. So, "Hello", "hello", and "HELLO" will all be treated as the same.
