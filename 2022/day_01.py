with open('day_01.txt') as file:
    file.seek(0)
    elf_calories = file.read()

elf_calories_split = elf_calories.split("\n\n")
array_calories = []

for elf_calories in elf_calories_split:
    elf_calories_lines = elf_calories.splitlines()
    array_one_calorie = []
    for food_item in elf_calories_lines:
        array_one_calorie.append(int(food_item))
    array_calories.append(sum(array_one_calorie))

array_calories.sort(reverse = True)
# Find the Elf carrying the most Calories.
print(f"The Elf carrying the most calories carries {max(array_calories)} calories.")
# Find the top three Elves carrying the most Calories.
print(f"The top three Elves carrying the most calories carries {sum(array_calories[0:3])} calories.")