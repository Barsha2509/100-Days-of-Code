import turtle
import pandas as pnd

data = pnd.read_csv("50_states.csv")
states = data["state"]
# print(states)

guessed_states = []


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    if answer_state.title() == "Exit":
        not_guessed_states = []
        for state in states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        print(len(not_guessed_states))
        print(len(guessed_states))
        data_dict = {"State": not_guessed_states}
        DF = pnd.DataFrame(data_dict)
        DF.to_csv("states_to_learn.csv")
        break


    else:

        def write_state_name(pos):
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(pos)
            t.write(f"{answer_state.title()}", align="Center", font=("Calibri", 12, "normal"))


        for state in states:
            if answer_state.title() == state:
                correct_state = data[data["state"] == answer_state.title()]
                coord = (int(correct_state.iloc[0, 1]), int(correct_state.iloc[0, 2]))
                write_state_name(coord)
                guessed_states.append(answer_state.title())


#screen.exitonclick()
