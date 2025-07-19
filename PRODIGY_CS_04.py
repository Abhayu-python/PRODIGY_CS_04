from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)  
        img_array = np.array(img)  

        key_array = np.full(img_array.shape, key, dtype=np.uint8) 

        encrypted_array = np.bitwise_xor(img_array, key_array)

        encrypted_img = Image.fromarray(encrypted_array)

        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully and saved as 'encrypted_image.png'")

    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(encrypted_image_path, key):
 
    try:
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_array = np.array(encrypted_img)  

        key_array = np.full(encrypted_array.shape, key, dtype=np.uint8)

        decrypted_array = np.bitwise_xor(encrypted_array, key_array)

        decrypted_img = Image.fromarray(decrypted_array)

        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully and saved as 'decrypted_image.png'")

    except FileNotFoundError:
        print(f"Error: Encrypted image not found at {encrypted_image_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main():
    print("Image Encryption and Decryption Tool")
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

        if choice == 'e':
            image_path = input("Enter the path to the image file you want to encrypt: ")
            try:
                key = int(input("Enter an integer key for encryption: "))
                encrypt_image(image_path, key)
            except ValueError:
                print("Invalid key. Please enter an integer.")

        elif choice == 'd':
            encrypted_image_path = input("Enter the path to the encrypted image file: ")
            try:
                key = int(input("Enter the same integer key used for encryption: "))
                decrypt_image(encrypted_image_path, key)
            except ValueError:
                print("Invalid key. Please enter an integer.")

        elif choice == 'q':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

