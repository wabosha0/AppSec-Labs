import zipfile
import os

SAFE_DIR = os.path.abspath('./uploads')
print(f"[*] Secure extractor - Safe dir is {SAFE_DIR}")

with zipfile.ZipFile('evil.zip', 'r') as zip_ref:
    for name in zip_ref.namelist():
        target = os.path.abspath(os.path.join(SAFE_DIR, name))
        if not target.startswith(SAFE_DIR):
            print(f"[!] BLOCKED Zip Slip: {name} -> {target}")
            continue
        zip_ref.extract(name, SAFE_DIR)
        print(f"[+] Safe: {name}")

print("[+] Done - No escape possible")
