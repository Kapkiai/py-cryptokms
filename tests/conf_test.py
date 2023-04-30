import logging
import os

from py_crypto.kms import StepKMSProvider

log = logging.getLogger(__name__)

# set this in case service is behind proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''
step_kms = StepKMSProvider(kms_base_url='https://localhost', kms_username='kms', kms_password='kms')


# Just for testing invalid keys
class InvalidKMSProvider(StepKMSProvider):
    def __init__(self):
        super(InvalidKMSProvider, self).__init__()

    def get_encryption_key(self, key_identifier: str) -> str:
        return 'invalid-key'


invalid_kms = InvalidKMSProvider()
