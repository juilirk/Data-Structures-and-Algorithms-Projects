# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, splitted_path, handler):
        """Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path"""
        root = self.root
        for path in splitted_path:
            root.insert(path)
            root = root.children[path]
        root.handler = handler

    def find(self, splitted_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        route = self.root
        for path in splitted_path:
            if path in route.children:
                route = route.children[path]
            else:
                return None
        return route.handler


""" A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler."""


class RouteTrieNode:
    def __init__(self, root_handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = root_handler

    def insert(self, small_path):
        if small_path not in self.children:
            self.children[small_path] = RouteTrieNode()
        else:
            pass


class Router:
    def __init__(self, handler, not_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        splitted_path = self.split_path(path)
        self.route_trie.insert(splitted_path, handler)

    def lookup(self, path):

        splitted_path = self.split_path(path)

        if len(splitted_path) == 0:
            return self.route_trie.root.handler

        result = self.route_trie.find(splitted_path)
        if result != None:
            return result
        return self.not_found_handler

    def split_path(self, raw_path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if raw_path:
            splitted_path = raw_path.split(sep='/')
            return [element for element in splitted_path if element != '']
        else:
            return []


# Here are some test cases and expected outputs
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home"))
# should print 'not found handler'

print(router.lookup("/home/about"))
# should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler'

print(router.lookup("/home/about/me"))
# should print 'not found handler'


router = Router("root handler", "not found handler")
router.add_handler("/home/about/me", "about me")

print(router.lookup("/home/about/"))
# should print 'not found handler'

print(router.lookup("/home/about/me"))
# should print 'about me'

print(router.lookup("/home/about/"))
# should print 'not found handler'
