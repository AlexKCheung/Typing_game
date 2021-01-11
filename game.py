# pip install essential_generators 
# get random values of sentances
from essential_generators import DocumentGenerator
gen = DocumentGenerator()

# measure elapsed time
import time


# print a paragraph for user to type
print()
time.sleep(1)
print("When you see \"GO!\", Type in the sentence below as fast as you can!")
time.sleep(2)
sentence_to_type = gen.sentence()
print(sentence_to_type) 

# sleep 3 seconds before starting 
time.sleep(4)
start = time.time()
print("GO!")


while True:
    player_input = input()
    if player_input == sentence_to_type:
        break
    else:
        print("Wrong input! Please try again. \n")
    # else pass and keep going until you get it right


# break loop when match 
# user done typing sentence so end time
# print rounded time of tiem to type
end = time.time()
total_time = end - start
total_time = round(total_time, 3)
print("It took you", total_time, "to type the sentance!")

