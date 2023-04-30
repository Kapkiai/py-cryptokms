import logging
from py_crypto.kms import StepKMSProvider

log = logging.getLogger(__name__)
step_kms = StepKMSProvider()


# Just for testing invalid keys
class InvalidKMSProvider(StepKMSProvider):
    def __init__(self):
        super(InvalidKMSProvider, self).__init__()

    def get_encryption_key(self, key_identifier: str) -> str:
        return 'invalid-key'


invalid_kms = InvalidKMSProvider()
