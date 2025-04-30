from qrcodex import QRCodeX

def main():
    # Create a basic QR code
    qr = QRCodeX()
    qr.add_data("Hello, World!")
    qr.generate("basic_qr.png")
    print("Generated basic QR code: basic_qr.png")

    # Create a QR code with custom settings
    qr = QRCodeX(
        error_correction='H',
        box_size=15,
        border=4
    )
    qr.add_data("https://example.com", data_type='url')
    qr.generate(
        "custom_qr.png",
        fill_color="#FF0000",
        back_color="white"
    )
    print("Generated custom QR code: custom_qr.png")

    # Create an SVG QR code
    qr = QRCodeX()
    qr.add_data("SVG QR Code Example")
    qr.generate(
        "svg_qr.svg",
        format="svg",
        fill_color="#0000FF"
    )
    print("Generated SVG QR code: svg_qr.svg")

if __name__ == "__main__":
    main()
