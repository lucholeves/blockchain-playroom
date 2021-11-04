import hashlib as hasher


class Block:
    """Block structure"""

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        
        sha.update(data.encode("utf-8"))

        return sha.hexdigest()
