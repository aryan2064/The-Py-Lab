# Image to ASCII

A terminal-based tool that converts any image into ASCII art and saves the result to a text file.

## Features

- Converts any image (JPG, PNG, etc.) to ASCII art
- Adjustable scale factor (lower = higher detail, larger output)
- Maps pixel brightness to ASCII characters: `#`, `X`, `%`, `&`, `*`, `/`, `'`, and space
- Outputs to a `.txt` file

## Requirements

- Python 3.x
- `Pillow` (PIL)

```bash
pip install Pillow
```

## How to Run

Edit the function call at the bottom of `image_to_ascii.py` with your own image path and preferences, then run:

```bash
python image_to_ascii.py
```

### Parameters

```python
asciiConvert(image, type, saveas, scale)
```

| Parameter | Description |
|-----------|-------------|
| `image`   | Path to input image file |
| `type`    | Image format (e.g. `"jpg"`, `"png"`) |
| `saveas`  | Output text file name |
| `scale`   | Downscale factor (e.g. `"3"` = divide dimensions by 3) |

### Example

```python
asciiConvert("photo.jpg", "jpg", "output.txt", "4")
```

This reads `photo.jpg`, resizes it to 1/4 of its original dimensions, and writes the ASCII art to `output.txt`.