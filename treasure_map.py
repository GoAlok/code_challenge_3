"""
    Instruction:
        You are going to write a program which will mark a spot with a x. The map is made up of blank squares.
            - Your program should allow you to enter the position of the treasure using two-digit system. \
            The first digit is the vertical column and the second digit is the horizontal row number. 
            
        emoji used = ⬜
"""
#          1    2     3
row1 =  ["⬜","⬜","⬜"]   # 1
row2 =  ["⬜","⬜","⬜"]   # 2
row3 =  ["⬜","⬜","⬜"]   # 3

map = [row1,row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


