from nacl.signing import SigningKey
import base64

# Generate Ed25519 key
private_key = SigningKey.generate()

# Raw bytes
raw_key_bytes = private_key.encode()

# Hex format
hex_key = raw_key_bytes.hex()
print(f"Private Key (Hex): {hex_key}")

# Base64 format
b64_key = base64.b64encode(raw_key_bytes).decode('utf-8')
print(f"Private Key (Base64): {b64_key}")

raw_public_key = private_key.verify_key.encode()

# Hex format
hex_public_key = raw_public_key.hex()
print(f"Public Key (Hex): {hex_public_key}")

# Base64 format
b64_public_key = base64.b64encode(raw_public_key).decode('utf-8')
print(f"Public Key (Base64): {b64_public_key}")
