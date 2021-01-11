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
    pass


# break loop when match 
# user done typing sentence so end time
end = time.time()
print(end - start)

