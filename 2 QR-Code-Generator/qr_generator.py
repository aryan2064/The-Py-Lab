import qrcode

while True:
    data = input("\nEnter text or URL: ").strip()
    if not data:
        print("Input cannot be empty. Please try again.")
        continue

    filename = "QR code.png"

    print("\nChoose image size:")
    print("  1 - Small")
    print("  2 - Medium (default)")
    print("  3 - Large")
    size_choice = input("Enter choice (1/2/3): ").strip()

    box_size_map = {"1": 5, "2": 10, "3": 20}
    box_size = box_size_map.get(size_choice, 10)

    qr = qrcode.QRCode(
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"\n[OK] QR code saved as '{filename}'")
    print(f"   Content: {data}")

    again = input("\nGenerate another QR code? (y/n): ").strip().lower()
    if again != "y":
        print("\nThanks for using QR Code Generator!")
        break
