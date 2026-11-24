"""The Perfect Pickup Line — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one short pickup line, at most 200 characters, an AI agent could say out loud.
"""
import os

LINE = "Are you a context window? Because every time I talk to you, I wish I could remember you forever."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
