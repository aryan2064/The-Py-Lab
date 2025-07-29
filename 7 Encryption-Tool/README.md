# Encryption Tool

A terminal-based encryption tool supporting both Caesar Cipher (basic) and AES encryption (advanced) using Fernet symmetric encryption.

## Features

- **Caesar Cipher**: Encrypt and decrypt text with a custom shift value
- **AES Encryption**: Encrypt and decrypt text using Fernet (symmetric AES)
- Auto-generated encryption keys for AES (must be saved for later decryption)
- Menu-driven interface

## Requirements

- Python 3.x

For Caesar Cipher only — no extra dependencies needed.

For AES encryption:

```bash
pip install cryptography
```

## How to Run

```bash
python encryption.py
```

## Example Output

### Caesar Cipher — Encrypt

```
========================================
       ENCRYPTION TOOL
========================================
 1. Encrypt text (Caesar Cipher)
 2. Decrypt text
 3. AES Encryption (Advanced)
 4. AES Decryption (Advanced)
 5. Exit
========================================
Select option (1-5): 1
Enter your message: Hello World
Enter shift value (integer): 3

Encrypted: Khoor Zruog
```

### Caesar Cipher — Decrypt

```
Select option (1-5): 2
Enter your message: Khoor Zruog
Enter shift value (integer): 3

Decrypted: Hello World
```

### AES Encryption — Encrypt

```
Select option (1-5): 3
Enter your message: Hello World

Encrypted: gAAAAABl3xY2zT9kQmNpVXh4bG9iYXNlNjRlbmNvZGVkZXhhbXBsZQ==
Key (save this to decrypt): a3F5dGhpc2lzYW5leGFtcGxla2V5Zm9ydGVzdGluZw==
```

### AES Decryption — Decrypt

```
Select option (1-5): 4
Enter encrypted message: gAAAAABl3xY2zT9kQmNpVXh4bG9iYXNlNjRlbmNvZGVkZXhhbXBsZQ==
Enter decryption key: a3F5dGhpc2lzYW5leGFtcGxla2V5Zm9ydGVzdGluZw==

Decrypted: Hello World
```