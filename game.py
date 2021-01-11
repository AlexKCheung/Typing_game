# pip install essential_generators 
# ^ remember to install this in order to fetch random sentences ^ 

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
time.sleep(3)
start = time.time()
print("GO!")

# keep prompting user for input until it matches the sentence to type
while True:
    player_input = input()
    if player_input == sentence_to_type:
        break
    else:
        print("Wrong input! Please try again.")
    # else pass and keep going until you get it right

# break loop when match 
# user done typing sentence so end time
# print rounded time of tiem to type
end = time.time()
total_time = end - start
total_time = round(total_time, 2)
print("You typed the sentence in ", total_time, " seconds!")

congragulations = {60: "Keep it up! I know you can type faster!",
                   30: "Nice work! Keep it up!",
                   20: "Good job! You sure can type!", 
                   10: "Wow! You are fast at typing!"}

if total_time <= 10:
    print(congragulations[10])
elif total_time <= 20:
    print(congragulations[20])
elif total_time <= 30:
    print(congragulations[30])
else:
    print(congragulations[60])
