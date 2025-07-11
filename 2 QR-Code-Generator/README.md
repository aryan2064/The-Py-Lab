# QR Code Generator

A terminal-based tool that generates QR codes from text or URLs and saves them as PNG image files.

## Features

- Convert any text or URL into a QR code
- Fixed output filename: `QR code.png`
- Three size options: Small, Medium, Large
- Default PNG output format
- Loop to generate multiple QR codes in one session

## Requirements

- Python 3.x
- `qrcode` library with PIL support

```bash
pip install qrcode[pil]
```

## How to Run

```bash
python qr_generator.py
```

## Example Output

```
Enter text or URL: https://github.com

Choose image size:
  1 - Small
  2 - Medium (default)
  3 - Large
Enter choice (1/2/3): 2

[OK] QR code saved as 'QR code.png'
   Content: https://github.com

Generate another QR code? (y/n): n

Thanks for using QR Code Generator!
```

## Generated QR Code

![Generated QR code](QR%20code.png)

