import os

# List of known malicious file names
MALICIOUS_FILE_NAMES = [
    "virus.exe",
    "malware.bat",
    "trojan.scr",
    "ransomware.py",
    "keylogger.dll",
    "MEMZ.exe",
]

def scan_directory(directory):
    """Scan the specified directory for malicious file names."""
    if not os.path.isdir(directory):
        print(f"The specified path '{directory}' is not a valid directory.")
        return

    print(f"Scanning directory: {directory}")
    found_malicious_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in MALICIOUS_FILE_NAMES:
                found_malicious_files.append(os.path.join(root, file))

    # Report results
    if found_malicious_files:
        print("Malicious files found:")
        for malicious_file in found_malicious_files:
            print(f" - {malicious_file}")
    else:
        print("No malicious files found.")

def main():
    drive = input("Enter the drive or directory to scan (e.g., C:\\ or /): ")
    scan_directory(drive)

if __name__ == "__main__":
    main()
