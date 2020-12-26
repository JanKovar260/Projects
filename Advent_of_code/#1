import logging

logging.basicConfig(filename='puzzle.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='w')

listed = open("input.txt", "r").readlines()
listed = [int(i.strip("\n")) for i in listed]
final_sum = 2020
part1 = set()
part2 = set()

# first part - find 2 numbers from the loaded list that sum up to 2020
for first_number in listed:
    complementary_number = final_sum - first_number
    if complementary_number in listed:
        part1.add(complementary_number * first_number)

logging.info('The resulting multiplication of the two seeked numbers is {}'.format(part1))

# second part - find 3 numbers from the loaded list that sum up to 2020
for first_number in listed:
    for second_number in listed:
        third_number = final_sum - first_number - second_number
        if third_number in listed:
            part2.add(first_number * second_number * third_number)

logging.info('The resulting multiplication of the three seeked numbers is {}'.format(part2))
