# Keylogger Program
This project involves the development of a simple yet organized keylogger using Python. The keylogger utilizes the pynput library to capture and log every key pressed by the user, recording the data into a text file (key_log.txt). Each keystroke is stored on a new line, and special keys such as "Enter", "Space", "Tab", and "Backspace" are clearly labeled to enhance readability. The keylogger runs in the background and continuously logs keyboard inputs in an organized manner until manually terminated.

# Features
1. Keystroke Logging: Captures and logs every keystroke made by the user, including both regular characters and special keys.
  
2. Organized Log Output: Each keystroke is logged on a separate line in the log file, ensuring clarity and easy readability. Special keys such as "Space", "Enter", "Backspace", and "Tab" are clearly labeled with their names.

3. Support for Special Keys: The program detects and logs special keys like Space, Enter, Tab, and Backspace, while other keys like Shift, Ctrl, and Alt are recognized and labeled appropriately.

4. Background Operation: The keylogger runs silently in the background, continuously monitoring and logging keystrokes without interrupting the user's workflow.

5. File Logging: Keystrokes are written to a text file (key_log.txt) in append mode, so no data is lost, and logs are continuously updated as new keys are pressed.

6. Extensibility: The program can be easily extended or customized, for example, to log more metadata (like timestamps) or to transmit logs remotely for more advanced use cases.

7. Simplicity: The program is simple, lightweight, and easy to implement using the pynput library, making it accessible for beginners to understand keylogging principles.

# Ethical Considerations
While keyloggers are powerful tools, they come with significant ethical considerations. This project is intended for educational purposes and emphasizes the importance of consent and responsible usage when dealing with software that monitors user activity. The organized logging format makes it easier to analyze recorded keystrokes, making the program suitable for controlled environments, such as research or cybersecurity awareness training.
