"""Advanced usage examples for QRCodeX."""

import os
from pathlib import Path
from qrcodex import QRCodeX

def main():
    """Run advanced usage examples."""
    # Create output directory
    output_dir = Path("advanced_examples")
    output_dir.mkdir(exist_ok=True)
    
    # Example 1: Binary data
    binary_data = bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05])
    qr = QRCodeX()
    qr.add_data(binary_data, data_type='binary')
    qr.generate(output_dir / "binary_qr.png")
    print(f"Generated binary QR code: {output_dir}/binary_qr.png")
    
    # Example 2: Image data
    # Use a minimal data URI
    data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    qr = QRCodeX()
    qr.add_data(data_uri, data_type='image')
    qr.generate(output_dir / "image_qr.png")
    print(f"Generated image QR code: {output_dir}/image_qr.png")
    
    # Example 3: Multiple data types
    qr = QRCodeX()
    qr.add_data("https://example.com", data_type='url')
    qr.add_data("Hello, World!", data_type='text')
    qr.add_data(bytes([0xFF, 0xFE, 0xFD]), data_type='binary')
    qr.generate(output_dir / "multiple_qr.png")
    print(f"Generated multiple data QR code: {output_dir}/multiple_qr.png")
    
    # Example 4: Custom styling
    qr = QRCodeX(
        error_correction='H',
        box_size=20,
        border=2
    )
    qr.add_data("Custom styled QR code")
    qr.generate(
        output_dir / "styled_qr.png",
        fill_color="#FF0000",
        back_color="#FFFFFF"
    )
    print(f"Generated styled QR code: {output_dir}/styled_qr.png")
    
    # Example 5: SVG output
    qr = QRCodeX()
    qr.add_data("SVG QR code")
    qr.generate(
        output_dir / "svg_qr.svg",
        format="svg",
        fill_color="#0000FF"
    )
    print(f"Generated SVG QR code: {output_dir}/svg_qr.svg")

if __name__ == "__main__":
    main()
