from nacl.signing import SigningKey
import base64

# User inputs private key in Base64
b64_private_key = input("Enter your Base64-encoded private key: ")

# Decode Base64 private key
try:
    raw_key_bytes = base64.b64decode(b64_private_key)
    if len(raw_key_bytes) != 32:
        raise ValueError("Invalid private key length. Ed25519 private key must be 32 bytes.")
except Exception as e:
    print(f"Error decoding private key: {e}")
    exit(1)

# Add prefix (Ton private key prefix 1231561495 -> [23, 35, 104, 73])
prefix = bytes([23, 35, 104, 73])
private_key_bytes = prefix + raw_key_bytes

# Create SigningKey object
private_key = SigningKey(raw_key_bytes)

# Hex format
print(f"New Private Key (Hex): {private_key_bytes.hex()}")
print(f"New Private Key (Base64): {base64.b64encode(private_key_bytes).decode()}")

# Public Key
raw_public_key = private_key.verify_key.encode()
print(f"Public Key (Hex): {raw_public_key.hex()}")
print(f"Public Key (Base64): {base64.b64encode(raw_public_key).decode()}")

# Save private key to file
with open("private_key.bin", "wb") as f:
    f.write(private_key_bytes)
print("Private key saved to private_key.bin")