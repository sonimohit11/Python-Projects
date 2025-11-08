import qrcode
import cv2

def generate_qr():
    data = input("Enter the text or link for the QR code: ")
    filename = input("Enter the filename to save (with .png): ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR code created and saved as '{filename}'")

def read_qr():
    filename = input("Enter the QR code image filename (with .png or .jpg): ")

    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print(f"QR Code Data: {data}")
        cv2.imshow("QR Code", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No QR code found in the image.")

def main():
    while True:
        print("\n=== QR Code Project ===")
        print("1. Generate QR Code")
        print("2. Read QR Code from Image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            generate_qr()
        elif choice == "2":
            read_qr()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()