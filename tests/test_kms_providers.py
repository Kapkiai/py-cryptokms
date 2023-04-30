from tests import conf_test


def test_get_key():
    key = 'n9Tp9+69gxNdUg9F632u1cCRuqcOuGmN'
    step_kms = conf_test.step_kms
    retrieved_key = step_kms.get_encryption_key(key_identifier='dummy-key')
    conf_test.log.info('Key retrieved: [%s]', retrieved_key)

    assert retrieved_key is not None
    assert isinstance(retrieved_key, str)
    assert retrieved_key == key


def test_key_cache():
    step_kms = conf_test.step_kms
    assert step_kms.get_encryption_key.cache_info().hits != 0
    step_kms.get_encryption_key(key_identifier='dummy-key')
    assert step_kms.get_encryption_key.cache_info().misses == 1
    step_kms.get_encryption_key(key_identifier='dummy-key')
    assert step_kms.get_encryption_key.cache_info().hits != 0
