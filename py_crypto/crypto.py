import base64
import binascii
import logging
from abc import ABC, abstractmethod

from Crypto.Cipher import AES

from py_crypto.kms import KMSProvider

class Krypto(ABC):
    def __init__(self, kms_provider: KMSProvider):
        self._log = logging.getLogger(__name__)
        self.kms_provider = kms_provider

    @abstractmethod
    def encrypt(self, clear_text: str, key_identifier: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, cipher_text: str, key_identifier: str) -> str:
        pass

    @staticmethod
    def _pad(byte_array: bytes, block_size: int) -> bytes:
        """
        # AES 'pad' byte array to multiple of BLOCK_SIZE bytes. CBC requirement
        :param byte_array: byte array to pad
        :param block_size: block size
        :return: padded byte array to the given block size
        """
        pad_len = block_size - len(byte_array) % block_size
        return byte_array + (bytes([pad_len]) * pad_len)

    @staticmethod
    def _un_pad(byte_s: bytes) -> bytes:
        """
        # Remove padding at end of byte array
        :param byte_s: bytes to un pad
        :return: up padded bytes
        """
        last_byte = byte_s[-1]
        return byte_s[0:-last_byte]


class AESCBCCipher(Krypto):

    def __init__(self, kms_provider: KMSProvider):
        super().__init__(kms_provider=kms_provider)

    def encrypt(self, clear_text: str, key_identifier: str) -> str:
        key = self._get_key_bytes(key_identifier=key_identifier)

        # Initialization vector for CBC. Empty with length of 16
        iv = bytearray(16)
        aes = AES.new(key, AES.MODE_CBC, iv)
        # Aes CBC expects the clear text blocks to be of size 16
        padded_clear_text_bytes = self._pad(clear_text.encode('utf-8'), 16)
        cipher_text = aes.encrypt(padded_clear_text_bytes)

        # Return base64 encoded cipherText for easier transmission/use
        return base64.b64encode(cipher_text).decode("UTF-8")

    def decrypt(self, cipher_text: str, key_identifier: str) -> str:
        key = self._get_key_bytes(key_identifier=key_identifier)
        cipher_text_bytes = base64.b64decode(cipher_text)
        # Initialization vector for CBC. Empty with length of 16
        iv = bytearray(16)
        aes = AES.new(key, AES.MODE_CBC, iv)
        plain_text_bytes = self._un_pad(aes.decrypt(cipher_text_bytes))

        return plain_text_bytes.decode("utf-8")

    def _get_key_bytes(self, key_identifier: str) -> bytes:
        """
        Helper method to retrieve key from kms provider and decode the
        key to bytes
        :param key_identifier: key identifier used for look up in kms
        :return: base64 decoded key
        :raises: Value error if the key cannot be base64 decoded.
                Key might be invalid
        """
        try:
            key = self.kms_provider\
                .get_encryption_key(key_identifier=key_identifier)
            return base64.b64decode(key, validate=True)
        except binascii.Error as e:
            raise e
