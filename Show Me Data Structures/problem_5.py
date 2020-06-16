import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        return f"Block is: \n Data: {self.data} \n Timestamp: {self.timestamp} \n Hash: {self.hash}"

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode(
            'utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.tail = None

    def append(self, data):

        if self.tail is None:
            self.tail = Block(time.time(), data, previous_hash=None)
        else:
            self.tail = Block(time.time(), data, previous_hash=self.tail)

    def search(self, data):

        if self.tail is None:
            return "Blockchain is empty!"
        else:
            position = self.tail

            while(position):
                if position.data == data:
                    return position
                position = position.previous_hash
            return None

    def size(self):
        """Return the size of the blockchain"""
        position = self.tail
        size = 0

        while position is not None:
            position = position.previous_hash
            size += 1
        return size

    def to_list(self):
        """Transforms the BlockChain content into a list"""
        l = []
        block = self.tail
        while block:
            l.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return l


blockchain = BlockChain()

blockchain.append('Name: X | ID:01 | Semester:6th')
blockchain.append('Name: Y | ID:02 | Semester:8th')
blockchain.append('Name: A | ID:04 | Semester:1st')

# test case 1
print(blockchain.size())  # should return 3

# test case 2
print(blockchain.to_list())
"""
[['Name: A | ID:04 | Semester:1st', 1590152842.6222556, '2e55458ea7f7bff1c5d83a17289ab99b75dcf6876a8921bf34758436cae63108'], ['Name: Y | ID:02 | Semester:8th', 1590152842.6222556, '7de5344e0637f4be21a5e12c5948de28b162f1a0d92a754d2723f1fd05d1d1ea'], ['Name: X | ID:01 | Semester:6th', 1590152842.6222556, '618bdb9acdc1c3e5ae6dd195e32c0dc1119edd4f499d3acdf2050969f3f616b3']]
"""
# test case 3
print(blockchain.search('Name: X | ID:01 | Semester:6th'))
"""
Block is:
 Data: Name: X | ID:01 | Semester:6th
 Timestamp: 1590153502.930327
 Hash: eb91b347e08e425002ee154a2383882090eba691a9979a72e1af6056976262e4
"""

# test case 4
blockchain = BlockChain()

print(blockchain.search('Name:A | ID:01 | Semester:1st'))
# should return Blockchain is empty!
