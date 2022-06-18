import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from hashlib import sha256


def hashing(text):
    return sha256(text.encode('utf-8')).hexdigest()


def create_salt() -> bytes:
    new_salt = os.urandom(16)
    return new_salt


def encrypt_data(salt: bytes, data: str, password: str) -> str:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    encoded = data.encode()
    ff = Fernet(key)
    encrypted = ff.encrypt(encoded)
    encrypted = encrypted.decode()
    return encrypted


def decrypt_data(salt: bytes, data: str, password: str) -> str:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    encrypted = data.encode()
    decrypted = f.decrypt(encrypted)
    decrypted = decrypted.decode()
    return decrypted


if __name__ == "__main__":

    # tests

    salt = b'\xc8S\x91in\xd2\xd8\xa7\xce,\xa0\xee|\xe6\x92\xab' # exemple. Please change that.

    def test_encrypt():
        data = "usuario" + ";" + "senha"
        password_app = "1234"
        ecpt = encrypt_data(salt, data, password_app)
        print(ecpt)

    def test_decrypt():
        data_encrypted = "gAAAAABhnSHpGWxosJ_aF70-MVX-VGXUJGHFbdDpchSBBartlzC_rQRXBzrmVvhZwl_uZkXl5zuoHD6GUGj7c2yRj1KOlWMeBw=="
        password_app = "1234"
        dcp = decrypt_data(salt, data_encrypted, password_app)
        print(dcp)

    def test_salt():
        new_salt = create_salt()
        print(new_salt)

    test_encrypt()
    test_decrypt()
    #test_salt()
