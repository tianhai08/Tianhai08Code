# generate_qr_code.py
import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter data for the QR code: ")
    filename = input("Enter filename to save the QR code: ")
    generate_qr_code(data, filename)
    print(f"QR code saved as {filename}")
