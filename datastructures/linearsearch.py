#solution of below mentioned question is example of linear search algorithm

# question -  Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card

""" pseudo code

1-Create a variable position with the value 0.
2-Check whether the number at index position in card equals query.
3-If it does, position is the answer and can be returned from the function
4-If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
5-If the number was not found, return -1

"""
def locate_card(cards, query):
    position = 0 

    while True:
        if cards[position] == query:
            return position
        
        position = +1

        if position == len(cards):

            return -1