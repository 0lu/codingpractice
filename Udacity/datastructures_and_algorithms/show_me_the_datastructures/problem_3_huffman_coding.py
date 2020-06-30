import sys
from collections import Counter
import heapq

class Node:
    def __init__(self, character=None, frequency=None, left_child=None, right_child=None):
        self.character = character
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"Node(character={self.character}, frequency={self.frequency}, left_child={self.left_child}" \
               f"right_child={self.right_child})"


def huffman_encoding(data):

    def get_encoding(root_, result_, path):
        if not root_:
            return
        if root_.character:
            result_[root_.character] = path
            return
        get_encoding(root_.left_child, result_, path + "0")
        get_encoding(root_.right_child, result_, path + "1")

    count = Counter(data)

    heap = []

    for character, frequency in count.items():
        heapq.heappush(heap, Node(character=character, frequency=frequency))

    if len(heap) == 1:
        node1 = heapq.heappop(heap)
        node2 = Node(frequency=node1.frequency + 0, left_child=node1, right_child=Node(0))
        heapq.heappush(heap, node2)
    else:
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            heapq.heappush(heap, Node(frequency=node1.frequency + node2.frequency, left_child=node1, right_child=node2))

    result = {}
    root = heap[0] if heap else None
    get_encoding(root, result, "")

    to_return = ""
    for char in data:
        to_return += result[char]

    return to_return, root


def huffman_decoding(data, tree):

    to_return = ""
    curr = tree

    for char in data:
        if char == "0":
            curr = curr.left_child
        else:
            curr = curr.right_child

        if curr.character:
            to_return += curr.character
            curr = tree

    return to_return


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

"""
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word


"""


testcase = "This is a text 0w4832948309384ijeijcsidfj sna dlfjioweur80wur0u3oriwerusfsf" \
            "sdfihjsldkhjfoishgiowuyrtooiruieurioewuripoeuriowehuriowehuriowehruiweorheiowrw" \
            "osfihdifhklkasdhro8u34yr8uhouhelkjsdhfljkershdreoiheihwesf"
encoded_data, tree = huffman_encoding(testcase)
print(encoded_data)
#1011000011100101001100000101001100000110011000001100011011111100001100010000101101011110001101101001101011000111111011000110110100110101101111110100110011011000110101111011010101111010001001001010101110010111101000010011111100101100110000101111111110010111100101100011111011010000011011011010111101000010110110100011011000000100111110100010101001001010010010100110111001001011101111010011111111011100111111011110001011000101001111010110011010110001111010100010100001100011001100010000101001011011010000010110011010111101000001010110010110011011010000010110001111101111010100000101100011111011110101000001011000111110111100001010010011111011100000111011010101100011100001111100100100100101110101110100010111000111111111001110110011001101111110000110001101101000110100011100010100001101101011101100101011101101111111001111111010011011111100010111111111100011111010001001111010111000110111000101110110101011100111110110010010

decoded_data = huffman_decoding(encoded_data, tree)
print(decoded_data)
#This is a text 0w4832948309384ijeijcsidfj sna dlfjioweur80wur0u3oriwerusfsfsdfihjsldkhjfoishgiowuyrtooiruieurioewuripoeuriowehuriowehuriowehruiweorheiowrwosfihdifhklkasdhro8u34yr8uhouhelkjsdhfljkershdreoiheihwesf


testcase = "AAAAA"
encoded_data, tree = huffman_encoding(testcase)
print(encoded_data)
#00000

decoded_data = huffman_decoding(encoded_data, tree)
print(decoded_data)
#AAAAA

testcase = ""
encoded_data, tree = huffman_encoding(testcase)
print(encoded_data)
#
decoded_data = huffman_decoding(encoded_data, tree)
print(decoded_data)
#

