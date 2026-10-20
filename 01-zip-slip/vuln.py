import zipfile

print("[*] Vulnerable extractor - extracts anything without checking")
with zipfile.ZipFile('evil.zip', 'r') as zip_ref:
    zip_ref.extractall('./uploads')
    print("[+] Done extracting to ./uploads")
