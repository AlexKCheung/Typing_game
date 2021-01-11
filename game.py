# pip install essential_generators 
# get random values of sentances
from essential_generators import DocumentGenerator
gen = DocumentGenerator()

# measure elapsed time
import time
start = time.time()


# print a paragraph for user to type
print()
print("When you see \"GO!\", Type in the sentence below as fast as you can!")

sentence_to_type = gen.sentence()
print(sentence_to_type) 

# sleep 3 seconds before starting 
time.sleep(3)
print("GO!")

# user done typing sentence so end time
end = time.time()
print(end - start)

