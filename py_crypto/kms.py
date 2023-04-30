import logging
from abc import ABC, abstractmethod
from functools import lru_cache

import requests
import urllib3


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

    def __init__(self, kms_base_url: str, kms_username: str, kms_password, *args, **kwargs):
        super().__init__()
        self.kms_base_url = kms_base_url
        self.kms_username = kms_username
        self.kms_password = kms_password
        self.args = args
        self.kwargs = kwargs
        self.key_url = kms_base_url + '/api/v1/key'

        # TODO: Look for a way to disable this
        # Don't disable globally.
        from urllib3.exceptions import InsecureRequestWarning
        urllib3.disable_warnings(InsecureRequestWarning)

    @lru_cache(maxsize=10)
    def get_encryption_key(self, key_identifier: str) -> str:
        try:
            session = requests.Session()
            # TODO: Look for a way to disable this
            session.verify = False
            response = session.get(url=self.key_url, auth=(self.kms_username, self.kms_password),
                                   params={'id': key_identifier, 'username': 'hive'}, timeout=300)
            if response.status_code != 200:
                raise ValueError(f"Could not retrieve key from kms. "
                                 f"Key might not be existing or user `hive` isn't authorized. "
                                 f"Status code [{response.status_code}], "
                                 f"Message [{response.content.decode('utf-8')}]")
            kms_res = response.json()
            # TODO: catch all responses well i.e when key is not found, server error when kms is unreachable
            return kms_res['key']
        except Exception as e:
            raise e


class NOOPKMSProvider(KMSProvider):
    def __init__(self):
        super().__init__()
        self.log.info('Initializing NOOP KMS Provider')

    def get_encryption_key(self, key_identifier: str) -> str:
        return 'n9Tp9+69gxNdUg9F632u1cCRuqcOuGmN'


class FileBasedKMSProvider(KMSProvider):
    def __init__(self):
        super().__init__()
        self.log.info('Initializing File Based KMS Provider')

    def get_encryption_key(self, key_identifier: str) -> str:
        return 'n9Tp9+69gxNdUg9F632u1cCRuqcOuGmN'

    def read_key_from_file(self, path):
        pass


class RangerKMSProvider(KMSProvider):
    def __init__(self):
        super().__init__()

    def get_encryption_key(self, key_identifier: str) -> str:
        pass
