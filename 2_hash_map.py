# HashMap
  # lookup, insert, delete O(1) Time
  # not ordered
    # key is hashed, moded, and put in bucket
    # collisions are turned into a LinkedList, HashMap, BST depending on the 
    # language
# Type 'python' in terminal for interactive terminal


# Create
hash = {}
hash['a'] = 1
hash['b'] = 2
hash

# Iterate
for key in hash:
  print(key)

# Print Key Value Pairs
for key in hash:
  print(key, hash[key])

# Print Hash
print(hash)

# Check If Key Exists
print('a' in hash) 
print('x' in hash)

# Lookup Value
print(hash['a'])

# Delete Item
del hash['a']
print(hash)

# Not ordered
hash['c'] = 3
hash['a'] = 1
print(hash)