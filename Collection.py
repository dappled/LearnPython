import collections
import json

if __name__ == "__main__":
    tree = lambda: collections.defaultdict(tree)
    some_dict = collections.defaultdict(dict) #tree()
    some_dict['colours']['favourite'] = "yellow"
    print(json.dumps(some_dict))