import os
import time
import random

G = "\033[92m"
R = "\033[91m"
C = "\033[96m"
Y = "\033[93m"
W = "\033[97m"
X = "\033[0m"

def slow(text, delay=0.035):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def bar(label):
    print(C + "\n" + label + X)
    for i in range(31):
        print("\r" + G + "[" + "█"*i + "░"*(30-i) +
              f"] {i*100//30}%", end="", flush=True)
        time.sleep(0.06)
    print(X)

def main():
    os.system("clear")
    print(G + r"""
███████╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗
██╔════╝██╔═══██╗██╔══██╗██╔═══██╗████╗ ████║
█████╗  ██║   ██║██████╔╝██║   ██║██╔████╔██║
██╔══╝  ██║   ██║██╔══██╗██║   ██║██║╚██╔╝██║
██║     ╚██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║
""" + X)
    print(R + "          F O R O M A T   B O T" + X)
    print(Y + "          VISUAL DEMO SYSTEM" + X)
    print(G + "="*48 + X)

    slow(C + "\n[1] Take Photo Number" + X)
    number = input(G + "\n[+] Phone Number: " + W)

    if not number.strip():
        print(R + "No number entered!" + X)
        return

    print(G + "\n[+] Target: " + number + X)
    time.sleep(1)

    bar("Initializing visual engine...")
    bar("Scanning simulated photo gallery...")
    slow(Y + "\n[!] SIMULATION: Photos are NOT accessed." + X)

    bar("Preparing virtual format sequence...")
    bar("Loading Foromat Bot modules...")
    bar("Finalizing visual effects...")

    print(R + "\n" + "="*48 + X)
    slow(R + ">>> PHONE FORMATTED SUCCESSFULLY <<<" + X, 0.07)
    print(G + ">>> DEMO COMPLETE - NO REAL DATA CHANGED <<<" + X)
    print(R + "="*48 + X)

    input(W + "\nPress Enter to exit..." + X)

if __name__ == "__main__":
    main()
