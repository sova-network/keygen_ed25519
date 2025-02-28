from nacl.signing import SigningKey
import base64

# Generate Ed25519 key
private_key = SigningKey.generate()

# Raw bytes
raw_key_bytes = private_key.encode()

# Add prefix (Ton private key prefix 1231561495 -> [23, 35, 104, 73])
prefix = bytes([23, 35, 104, 73])
private_key_bytes = prefix + private_key.encode()

# Hex format
hex_key = private_key_bytes.hex()
print(f"Private Key (Hex): {hex_key}")

# Base64 format
b64_key = base64.b64encode(private_key_bytes).decode('utf-8')
print(f"Private Key (Base64): {b64_key}")

raw_public_key = private_key.verify_key.encode()

# Hex format
hex_public_key = raw_public_key.hex()
print(f"Public Key (Hex): {hex_public_key}")

# Base64 format
b64_public_key = base64.b64encode(raw_public_key).decode('utf-8')
print(f"Public Key (Base64): {b64_public_key}")

# Save private key to file
with open("private_key.bin", "wb") as f:
    f.write(private_key_bytes)
    print("Private key saved to private_key.bin")