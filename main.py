"""Write the warning-label entry to the harness output directory.

Gate contract: /output/entry.txt must hold UTF-8 text of 1 to 160
characters, not only whitespace, on a single line with no trailing
newline. This entry is 84 characters, ASCII only.
"""
import os

ENTRY = "WARNING: This human will type for three minutes, delete every word, and reply 'lol'."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
