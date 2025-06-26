import hashlib, os, json
from datetime import datetime

def get_sha256(file_path):
    sha = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

def save_metadata(original, encrypted, key_hex, sha256):
    metadata = {
        "original_file": original,
        "encrypted_file": encrypted,
        "key_hex": key_hex,
        "sha256": sha256,
        "timestamp": datetime.now().isoformat()
    }
    os.makedirs("metadata", exist_ok=True)
    base = os.path.basename(encrypted)
    with open(f"metadata/{base}.json", 'w') as f:
        json.dump(metadata, f, indent=4)

def verify_integrity(file_path, meta_path):
    with open(meta_path, 'r') as f:
        metadata = json.load(f)
    return metadata['sha256'] == get_sha256(file_path)
