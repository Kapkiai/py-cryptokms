import logging
from abc import ABC, abstractmethod
from functools import lru_cache


class KMSProvider(ABC):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    @abstractmethod
    def get_encryption_key(self, key_identifier: str) -> str:
        """
        Method used to retrieve encryption key from a key management server.
        Implement this method for different providers.
        Implementations might choose to cache the key
        :param key_identifier: key identifier in the key management server
        :return: encryption key
        """


class StepKMSProvider(KMSProvider):

    def __init__(self):
        super().__init__()

    @lru_cache(maxsize=10)
    def get_encryption_key(self, key_identifier: str) -> str:
        return 'n9Tp9+69gxNdUg9F632u1cCRuqcOuGmN'
