### Explanation

The problem required to store a key value pair, this gave me the idea 
to use a dictionary. Also, the lookup and deletion time should be O(1),
which is usually the case with dictionary (why we used mostly dictionaries
during the hashing chapter). 
The second concern was to keep a track of the order of filling in of the 
inputs (required to delete the Last used item), for this I decided to choose
lists as they are pretty versatile and have relevant functions.
