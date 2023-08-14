import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt="What's anther stat's name?").title()
data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()
guessed_states = []
state_to_learn = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's anther state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_data:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_location = data[data.state == answer_state]
        t.goto(int(state_location.x), int(state_location.y))
        t.write(answer_state)

for state in state_data:
    if state not in guessed_states:
        state_to_learn.append(state)


df = pandas.DataFrame(state_to_learn)
df.to_csv("states_to_learn.csv")