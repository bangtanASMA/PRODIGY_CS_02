from PIL import Image

def encrypt_image(image_path):
    img_path = "Internship/Task_02/image.jpg"
    img = Image.open(image_path)
    
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            
            pixel = img.getpixel((x, y))

            encrypted_pixel = (pixel[2], pixel[1], pixel[0])  
            
            img.putpixel((x, y), encrypted_pixel)
    
    # the encrypted image
    img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path):
    encrypted_img = Image.open(encrypted_image_path)

    width, height = encrypted_img.size
 
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = (encrypted_pixel[2], encrypted_pixel[1], encrypted_pixel[0]) 
  
            encrypted_img.putpixel((x, y), decrypted_pixel)

    encrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

encrypt_image("image.jpg")
decrypt_image("encrypted_image.png")
