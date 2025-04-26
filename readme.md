# Terminal Auto Clicker
A simple terminal-based auto clicker built with Python. It uses the pynput library to simulate mouse clicks, threading 
for a smooth background operation, and pandas to create a table consisting of the status of the auto clicker. 

## Key Features

- 🖱️ Automated mouse clicks at customizable intervals.
- 🧵 Threaded clicking to start/stop without freezing the terminal. 
- 📈 Status table using a simple pandas DataFrame (e.g., target app, interval, mouse status, etc)
- ⌨️ Hotkeys to start and stop ([T] to start and [Q] to stop). 

## Installation

First, make sure you have Python 3.8+ installed. Second, clone the git repository as the following, 

```commandline
git clone https://github.com/PrayagPatel1/Auto-Clicker.git 
cd Auto-Clicker 
```

Before running any files from this package make sure you have the following packages and if not then copy the code 
towards the end of the list, 

- pandas
- pynput
- tabulate
- pywin32 
- time (built-in)
- sys (built-in)
- os (built-in)
- threading (built-in)

```commandline
pip install pandas pynput tabulate pywin32
```

## Usage

To run the auto clicker run the following script, 

```commandline
python main.py
```

Then enter the click interval to your liking, press enter, and then press t to toggle the auto clicker. It's going to 
display a status table with information about target app, click interval, total clicks, and whether the auto clicker 
is running or not. 

## Notes 

- **Disclaimer:** USE RESPONSIBLY. Some games or software may prohibit the use of auto-clickers. This is meant to be 
educational and not to cause harm in any way, shape or form. 
