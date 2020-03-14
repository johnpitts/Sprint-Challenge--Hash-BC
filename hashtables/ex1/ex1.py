#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    answer = []

    #  Insert all the wieghts into a hash table

    for i in weights:
        # key = str(i)
        hash_table_insert(ht, i, i)
    
    # print("PRINT LIST \n")
    # for z in range(len(ht.storage)):
    #     print(z)
    #     if ht.storage[z] is not None:
    #         print(ht.storage[z])
    
    # pick the first wieght, and calculate what value would lead to a match
    # print("finding proper wate \n")

    for wate in weights:
        target = limit - wate
        # print(wate)
        
        # simply search for the value using O(1) search in the hash_table to get the answer
        preanswer = hash_table_retrieve(ht, target)
        if wate > target and preanswer != None:
            # arrange the tuple in "answer" with largest value first in the "0" position, and smaller in the "1" position
            # print("wate > target")
            # print_answer([wate, target])
            answer.append(weights.index(wate))
            answer.append(weights.index(target))
            break
        elif preanswer != None:
            # print("target > wate")
            # print_answer([target, wate])
            answer.append(weights.index(target))
            answer.append(weights.index(wate))
            break
        
    print(f"answer: {answer}")
    return answer


def print_answer(answer):
    if answer is not None:
        print("answers", answer[0], answer[1])
    else:
        print("None")


# weights = [4, 2, 1, 7]
# length = 4
# limit = 3
# get_indices_of_item_weights(weights, length, limit)
