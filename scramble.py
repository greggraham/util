import random

# Read the input file in.txt
# The file should contain lines like:
# 1) Answer 1
with open("in.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
answers = [line[3:] for line in lines] if lines[0][:2] == "A)" else lines

# Shuffle the answers
random.shuffle(answers)

# Write the scrambled answers to out.txt
with open("out.txt", "w") as f:
    for letter, answer in zip("ABCDE", answers):
        f.write(f"    {letter}) {answer}\n")
