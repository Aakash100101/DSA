class MyHashMap:
    EMPTY = -1
    TOMBSTONE = -2

    def __init__(self):
        self.size = 20011
        self.keys = [self.EMPTY] * self.size
        self.values = [0] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        first_tombstone = -1
        # Probe until we find the key or an empty slot
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.values[index] = value
                return
            if self.keys[index] == self.TOMBSTONE and first_tombstone == -1:
                first_tombstone = index
            index = (index + 1) % self.size
        # Insert at first tombstone if found, otherwise at empty slot
        if first_tombstone != -1:
            index = first_tombstone
        self.keys[index] = key
        self.values[index] = value

    def get(self, key: int) -> int:
        index = self._hash(key)
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.keys[index] = self.TOMBSTONE
                return
            index = (index + 1) % self.size