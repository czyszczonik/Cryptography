import jks

def getKey(keystore_path = None, identifier = None, keystore_password = None):
    try:
        keystore = jks.KeyStore.load(keystore_path, keystore_password)
    except Exception as exception:
        raise exception
    try:
        keyEntry = keystore.secret_keys[identifier]
    except Exception as exception:
        raise exception
    return keyEntry.key


def getDefaultKey():
    return getKey("keystores/default.jks", "default", "default")
