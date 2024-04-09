# HackerRank basic Python test1

import math
import os
import random
import re
import sys



def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    answer = ""
    sentence = sentence.split(" ")

    smaller_start, smaller_end = ord("a"), ord("z")
    bigger_start, bigger_end = ord("A"), ord("Z")

    for i in range(len(sentence) - 1, -1, -1):
        word = sentence[i]
        temp = ""
        for char in word:
            if smaller_start <= ord(char) <= smaller_end:
                temp += char.upper()
            else:
                temp += char.lower()

        answer += temp
        if i:
            answer += " "

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
