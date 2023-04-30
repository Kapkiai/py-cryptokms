import pytest

from py_crypto.crypto import AESCBCCipher
from py_crypto.kms import StepKMSProvider
from tests import conf_test


def test_encryption():
    step_kms = conf_test.step_kms
    aes = AESCBCCipher(kms_provider=step_kms)

    assert isinstance(aes.kms_provider, StepKMSProvider)
    cipher_text = aes.encrypt(clear_text='254727128043',
                              key_identifier='dummy-key')
    assert isinstance(cipher_text, str)

    # cache check
    assert aes.kms_provider.get_encryption_key.cache_info().misses == 1
    # check that our retrieved key has actually been cached
    assert aes.kms_provider.get_encryption_key.cache_info().currsize == 1

    # assert that we encrypted our clear text well
    assert cipher_text == 'Tywy7Y272MmuDlrewpOV9A=='

    # just assert that actually out encryption was fine with a negative test
    with pytest.raises(AssertionError):
        assert cipher_text != 'Tywy7Y272MmuDlrewpOV9A=='


def test_decryption():
    step_kms = conf_test.step_kms
    aes = AESCBCCipher(kms_provider=step_kms)

    assert isinstance(aes.kms_provider, StepKMSProvider)
    clear_text = aes.decrypt(cipher_text='i2v/RyXZHmfEUWZgcMx+XQ==',
                             key_identifier='dummy-key')
    assert isinstance(clear_text, str)

    # cache check
    assert aes.kms_provider.get_encryption_key.cache_info().misses == 1
    # check that our retrieved key has actually been cached
    assert aes.kms_provider.get_encryption_key.cache_info().currsize == 1

    # assert that we encrypted our clear text well
    assert clear_text == '727399473'

    # just assert that actually out encryption was fine with a negative test
    with pytest.raises(AssertionError):
        assert clear_text != '727399473'


def test_encrypt_decrypt_cache():
    step_kms = conf_test.step_kms
    aes = AESCBCCipher(kms_provider=step_kms)
    assert isinstance(aes.kms_provider, StepKMSProvider)

    # Encryption
    cipher_text = aes.encrypt(clear_text='My name is Mathew',
                              key_identifier='dummy-key')
    assert isinstance(cipher_text, str)

    # cache miss check, should be 1 after first encryption call
    assert aes.kms_provider.get_encryption_key.cache_info().misses == 1
    # check that our retrieved key has actually been cached
    assert aes.kms_provider.get_encryption_key.cache_info().currsize == 1

    # Decryption
    clear_text = aes.decrypt(cipher_text=cipher_text,
                             key_identifier='dummy-key')
    assert isinstance(clear_text, str)

    # cache miss check, should still be 1 as the key does nt change
    assert aes.kms_provider.get_encryption_key.cache_info().misses == 1
    # check that our retrieved key has actually been cached
    assert aes.kms_provider.get_encryption_key.cache_info().currsize == 1
    # check cache hit, should not be 0 as we expect that cached key will be used
    assert aes.kms_provider.get_encryption_key.cache_info().hits != 0

    # Encryption assertion
    assert clear_text == 'My name is Mathew'
    assert cipher_text == 'DxyvpB7QqEt9JOED7iMJVRgSTiRyYVjPizZmOpHdVSM='


def test_invalid_key():
    step_kms = conf_test.invalid_kms
    aes = AESCBCCipher(kms_provider=step_kms)
    assert isinstance(aes.kms_provider, StepKMSProvider)

    with pytest.raises(ValueError):
        aes.encrypt(clear_text='My name is Mathew', key_identifier='dummy-key')
