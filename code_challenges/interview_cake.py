def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    print(sorted_meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
# [(0, 1), (3, 8), (9, 12)]


def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1

    return list_of_chars

print(reverse(['h', 'e', 'l', 'l', 'o']))
print(reverse(['j', 'e', 's', 's', 'i', 'c', 'a']))


def merge_lists(my_list, alices_list):

    answer = []


    while len(my_list) > 0 or len(alices_list) > 0:

        if my_list == []:
            answer.append(alices_list.pop(0))
        elif alices_list == []:
            answer.extend(my_list.pop(0))

        elif my_list[0] < alices_list[0]:
            answer.append(my_list.pop(0))
            
        else:
            answer.append(alices_list.pop(0))
            

    return answer


print(merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))

def enough_time(flight_length, movie_lengths):

    for x in movie_lengths:
        if flight_length - x in movie_lengths:
            return True
        else:
            return False



print(enough_time(300, [60, 120, 200, 300, 250, 330, 500, 400, 100]))

def word_cloud(sentence):

    sentence = list(sentence.lower())

    punctuation = ['.', ',', '(', ')', '!']

    new_sentence = []

    for x in sentence:
        if x not in punctuation:
            new_sentence.append(x)

    new_sentence = ''.join(new_sentence)

    new_sentence_2 = new_sentence.split(' ')

    dictionary = {}

    for word in new_sentence_2:
        dictionary[word] = dictionary.get(word, 0) + 1

    return dictionary


print(word_cloud('Add milk and eggs, then add flour and sugar.'))
print(word_cloud("We came, we saw, we conquered... then we ate Bill's (Mille-Feuille) cake."))



def get_max_profit(stock_prices):

    # min_price  = stock_prices[0]
    # max_profit = stock_prices[1] - stock_prices[0]

   
    # for current_time in range(1, len(stock_prices)):
    #     current_price = stock_prices[current_time]

    #     potential_profit = current_price - min_price

    #     max_profit = max(max_profit, potential_profit)

    #     min_price  = min(min_price, current_price)

    # return max_profit

    max_profit = 0

    for earlier_time, earlier_price in enumerate(stock_prices):

        for later_time in range(earlier_time + 1, len(stock_prices)):
            later_price = stock_prices[later_time]

            potential_profit = later_price - earlier_price

            max_profit = max(max_profit, potential_profit)


print(get_max_profit([10, 7, 5, 8, 11, 9]))


def highest_product_of_3(list_of_ints):


    highest = max(list_of_ints[0], list_of_ints[1]) #10
    lowest  = min(list_of_ints[0], list_of_ints[1]) #1
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1] #1*10=10
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1] #1*10=10

   
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2] #-50

    # Walk through items, starting at index 2
    for i in range(2, len(list_of_ints)): #range(2, 5)
        current = list_of_ints[i]

        
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        
        highest = max(highest, current)

        
        lowest = min(lowest, current)

    return highest_product_of_3

print(highest_product_of_3([1, 10, -5, 1, -100])) # -100 * -5 * 10 = 5000


def get_products_of_all_ints_except_at_index(int_list):

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)
    #[None, None, None, None]

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far 
        product_so_far *= int_list[i]

        # print(product_so_far)
        # 1*1
        # 1*7
        # 1*7*3
        # 1*7*3*4

        print(products_of_all_ints_except_at_index)

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1): #range(3, -1, -1)
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

        # print(product_so_far)
        # 4*1
        # 4*3
        # 4*3*7
        # 4*3*7*1

        print(products_of_all_ints_except_at_index)

    return products_of_all_ints_except_at_index


print(get_products_of_all_ints_except_at_index([1, 7, 3, 4])) #  [84, 12, 28, 21]

def find_rotation_point(words):

    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
        else:
            # Go left
            ceiling_index = guess_index

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index

print(find_rotation_point([6,7,8,9,10,11,12,1,2,3,4])) # index 7
print('')


def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)
    print(score_counts)

    # Populate score_counts
    for score in unsorted_scores:
        print(score)
        score_counts[score] += 1

    print(score_counts)

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        print(count)

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores


print(sort_scores([3,7,3,5,2,1], 8))
print('')


def merge_ranges(meetings):
    """Your company built an in-house calendar tool called HiCal. You want to add 
    a feature to see the times in a day when everyone is available.
    To do this, you’ll need to know when any team is having a meeting. In HiCal, 
    a meeting is stored as a tuple of integers (start_time, end_time). These 
    integers represent the number of 30-minute blocks past 9:00am."""

    # Sort by start time
    sorted_meetings = sorted(meetings)
    print(sorted_meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    print(merged_meetings)

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])) #[(0, 1), (3, 8), (9, 12)]






