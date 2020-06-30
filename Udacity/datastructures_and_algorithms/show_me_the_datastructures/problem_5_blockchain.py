import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        if self.previous_hash:
            hash_str = self.timestamp + self.data + self.previous_hash
        else:
            hash_str = self.timestamp + self.data
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, timestamp, data):
        if self.tail:
            to_add = Block(timestamp, data, self.tail.hash)
            self.tail.next = to_add
            to_add.prev = self.tail
            self.tail = to_add
        else:
            to_add = Block(timestamp, data, None)
            self.head = self.tail = to_add

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"timestamp: {curr.timestamp}, data:{curr.data}, " \
                      f"previous hash:{curr.previous_hash}, hash: {curr.hash}\n"
            curr = curr.next
        return result

blockchain = BlockChain()
blockchain.insert_node("1233434", "data1")
blockchain.insert_node("1233435", "data2")
blockchain.insert_node("1233436", "data3")
blockchain.insert_node("1233437", "data4")
blockchain.insert_node("1233438", "data5")
blockchain.insert_node("1233439", "data6")

print(blockchain)

"""
timestamp: 1233434, data:data1, previous hash:None, hash: 6c3ce8b7a60d75d3ad9b0c017245484c8b6cd1953b24994a3eb8983c81455e7d
timestamp: 1233435, data:data2, previous hash:6c3ce8b7a60d75d3ad9b0c017245484c8b6cd1953b24994a3eb8983c81455e7d, hash: 687e0409f25f85e4577647a7844223147e0385544411498392f89b97449276cf
timestamp: 1233436, data:data3, previous hash:687e0409f25f85e4577647a7844223147e0385544411498392f89b97449276cf, hash: da6591cf768aa39528155d18a79c4deb0a078f16edd1610f6ac045fdd2e17945
timestamp: 1233437, data:data4, previous hash:da6591cf768aa39528155d18a79c4deb0a078f16edd1610f6ac045fdd2e17945, hash: c904959f7e7d93b1ecf3d1a1ba0a79a63d7bb0f74503584ff2ef34002f209549
timestamp: 1233438, data:data5, previous hash:c904959f7e7d93b1ecf3d1a1ba0a79a63d7bb0f74503584ff2ef34002f209549, hash: 821192dcb6f1ace0219817482ad19397f3393092f13a40e0ad56bbab1397c600
timestamp: 1233439, data:data6, previous hash:821192dcb6f1ace0219817482ad19397f3393092f13a40e0ad56bbab1397c600, hash: 30ad61f6cd246c67e592bdd6c404545e42ed33a011cbb2e0e88f707baf4ac9f5
"""

blockchain = BlockChain()
blockchain.insert_node("", "")
blockchain.insert_node("", "")
blockchain.insert_node("", "")
print(blockchain)

"""
timestamp: , data:, previous hash:None, hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
timestamp: , data:, previous hash:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, hash: cd372fb85148700fa88095e3492d3f9f5beb43e555e5ff26d95f5a6adc36f8e6
timestamp: , data:, previous hash:cd372fb85148700fa88095e3492d3f9f5beb43e555e5ff26d95f5a6adc36f8e6, hash: e67e72111b363d80c8124d28193926000980e1211c7986cacbd26aacc5528d48
"""

blockchain = BlockChain()
blockchain.insert_node("", "")
blockchain.insert_node("AA", "AAAA")
blockchain.insert_node("AA", "AAAA")
print(blockchain)

"""
timestamp: , data:, previous hash:None, hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
timestamp: AA, data:AAAA, previous hash:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, hash: dea5952c632d2f79a68c02e619daeebc70372b5c7e3c7ca83df4934b36dbe83b
timestamp: AA, data:AAAA, previous hash:dea5952c632d2f79a68c02e619daeebc70372b5c7e3c7ca83df4934b36dbe83b, hash: 05d05bbd0d3762c16c785a11ff03a74d32b21a62b95cc0cdf283c2f02208d6df
"""