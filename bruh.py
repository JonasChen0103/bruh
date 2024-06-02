import os
import subprocess
import sys

def open_terminal_and_run_curl():
    if sys.platform.startswith('win'):
        # Windows
        subprocess.call('start cmd /K "curl ascii.live/rick"', shell=True)
    elif sys.platform.startswith('darwin'):
        # macOS
        subprocess.call('open -a Terminal "curl ascii.live/rick"', shell=True)
    elif sys.platform.startswith('linux'):
        # Linux
        subprocess.call('gnome-terminal -- bash -c "curl ascii.live/rick; exec bash"', shell=True)
    else:
        print("Unsupported platform")

if __name__ == "__main__":
    open_terminal_and_run_curl()