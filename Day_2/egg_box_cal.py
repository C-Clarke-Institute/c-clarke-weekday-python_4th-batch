#One box can contain 12 eggs, user wants to find out how many boxes needed to store the eggs.
#when user enter number of eggs , calculate how many full boxes and remaining eggs

#how many boxes need to store all the eggs


while 1:
    number_of_eggs = int(input("\nEnter Egg Count : "))

    full_boxes = number_of_eggs // 12
    remaining_eggs = number_of_eggs % 12

    print(f"Full Boxes : {full_boxes}\nRemaining Eggs : {remaining_eggs}")

    needed_final_box_count = (number_of_eggs + 11) // 12

    print(f"Final Box Count : {needed_final_box_count}")