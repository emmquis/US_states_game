import turtle
import pandas
from scoreboard import Scoreboard
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

scoreboard = Scoreboard()
states = States()
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()  # list of all states
total_states = len(state_list)

guessed_correct = 0
guessed_states = []
# TODO: 4 Use a loop to allow the user to keep guessing
while guessed_correct < total_states:
    screen.update()
    # TODO: 1 Convert the guess to Title Case
    answer_state = screen.textinput(title="Guess a State", prompt="What's a states name?").title()


    if answer_state == "Exit":
        # list comprehension for below for loop and if statement
        missed_states = [state for state in state_list if state not in guessed_states]
        # # alternative to above list comprehension
        # for state in state_list:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    # TODO: 2 Check if the guess is among the 50 states
    if answer_state in state_list:
        if answer_state in guessed_states:
            scoreboard.repeat_guess()
        else:
            # TODO: 5 Record the correct guesses in a list
            guessed_states.append(answer_state)

            # TODO: 6 Keep track of the score
            guessed_correct += 1
            scoreboard.increase_guess()
            # TODO: 3 Write correct guesses onto the map
            x_cord = data.loc[data.state == answer_state, "x"].values[0]
            y_cord = data.loc[data.state == answer_state, "y"].values[0]
            # another way to get x and y as integers
            # state_data = data[data.state == answer_state]
            # x_cord = int(state_data.x)
            # y_cord = int(state_data.y)
            states.state_map(answer_state, x_cord, y_cord)
    else:
        scoreboard.incorrect_guess()

screen.exitonclick()
