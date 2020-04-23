from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()
