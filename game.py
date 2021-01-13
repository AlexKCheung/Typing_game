# pip install essential_generators 
# ^ remember to install this in order to fetch random sentences ^ 

# get random values of sentances
from essential_generators import DocumentGenerator
gen = DocumentGenerator()

# measure elapsed time
import time

# print a paragraph for user to type
print("In three seconds, when you see \"GO!\", type in the sentence below as fast as you can!")
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

# break loop when input matches sentence
# user done typing sentence so end time
# print rounded time of tiem to type
end = time.time()
total_time = end - start
total_time = round(total_time, 2)
print("You typed the sentence in ", total_time, " seconds!")


# characters in the sentence to type
characters = 0
for i in sentence_to_type:
    characters += 1

# calculate cpm and wpm
cpm = characters * 60 / total_time
cpm = round(cpm)

# standard calculation of wpm from cpm
wpm = cpm / 5
wpm = round(wpm)

print("Your speed is:", wpm, "words per minute / ", cpm, "characters per minute.")

# congratulates players for their hard work
congragulations = {0: "Keep it up! I know you can type faster!",
                   50: "Nice work! Keep it up!",
                   80: "Good job! You sure can type!", 
                   100: "Wow! You are fast at typing!"}

# average typing speed is 41 wpm 
if wpm >= 100:
    print(congragulations[100])
elif wpm >= 80:
    print(congragulations[80])
elif wpm >= 50:
    print(congragulations[50])
else:
    print(congragulations[0])
