import streamlit as st

# Define the encryption function
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted_message += encrypted_char
    return encrypted_message

# Define the decryption function
def decrypt(encrypted_message, key):
    message = ""
    for i in range(len(encrypted_message)):
        encrypted_char = encrypted_message[i]
        key_char = key[i % len(key)]
        char = chr((ord(encrypted_char) - ord(key_char)) % 256)
        message += char
    return message

# Define the Streamlit app
def app():
    st.title("End-to-End Encryption")
    
    # Get the message and key from the user
    message = st.text_input("Enter your message:")
    key = st.text_input("Enter your encryption key:")
    
    # Encrypt the message if the user has entered both a message and key
    if message and key:
        encrypted_message = encrypt(message, key)
        st.write(f"Encrypted message: {encrypted_message}")
        
        # Decrypt the message if the user clicks the "Decrypt" button
        if st.button("Decrypt"):
            decrypted_message = decrypt(encrypted_message, key)
            st.write(f"Decrypted message: {decrypted_message}")

# Run the app
if __name__ == "__main__":
    app()
