#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # First insert all the tickets into a hash table so we can easily access the sources by key

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    # Search for key  with None as the source, for home city

    homecity = hash_table_retrieve(hashtable, "NONE")
    print("\n test starts here!!!!!!!!!!!!!!!!!!!!!!!")
    print(homecity)
    route[0] = homecity

    # use the homecity value to get the next destination
    previous_city = homecity

    for z in range(1, length-1):
        next_city = hash_table_retrieve(hashtable, previous_city)
        if next_city is not "NONE" and next_city is not None: 
            print("NOT NOT is hit")                                 # WHY THIS NOT WORKING?
            route[z] = next_city
            print(next_city)
        previous_city = next_city
    # route.remove("NONE")
    print("here's the list:")
    print(route)
    

    return route[:-1]
