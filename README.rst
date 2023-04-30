==============
Py-Crypto
==============

Simple Cryptographic Library With Key Management Server Integration

Quick Start
-----------

The easiest way to install NiPyApi is with pip::

    # in bash
    pip install pycryptokms


Python example::

    # in python
    from py_crypto.kms import StepKMSProvider
    from py_crypto.crypto import AESCBCCipher

    step_kms = StepKMSProvider()

    aes = AESCBCCipher(kms_provider=step_kms)

    cipher_text = aes.encrypt(clear_text='254727128043', key_identifier='dummy-key')

    print(f'Cipher Text: {cipher_text} -> Expected Cipher Text: \'Tywy7Y272MmuDlrewpOV9A==\'')

