
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.map = {}
        self.handler = handler

    def insert(self, child):
        # Insert the node as before
        self.map[child] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, default_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.default_handler = default_handler
        self.root = RouteTrieNode(root_handler)
        self.root.map[""] = RouteTrieNode(root_handler)

    def insert(self, paths, handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.root
        for path in paths:
            if path not in curr.map:
                curr.map[path] = RouteTrieNode(self.default_handler)
            curr = curr.map[path]
        curr.handler = handler if handler else self.default_handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root
        for path in paths:
            if path not in curr.map:
                return self.default_handler
            curr = curr.map[path]
        return curr.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, default_handler):
        default_handler = "not found handler" if not default_handler else default_handler
        self.router_trie = RouteTrie(root_handler, default_handler)

    def add_handler(self, url, handler):
        paths = self.split_path(url)
        self.router_trie.insert(paths, handler)

    def lookup(self, url):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(url)
        return self.router_trie.find(paths)

    @staticmethod
    def split_path(url):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return url.strip("/").split("/")

# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
# should print 'root handler'
print(router.lookup("/home"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))
# should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup(""))
# root handler
