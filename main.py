import turtle
from answer_label import AnswerLabel
import pandas

# Screen setup
screen = turtle.Screen()
screen.title('USA States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Import csv data & initialize Pandas
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
all_x = data.x.to_list()
all_y = data.y.to_list()


# Create label object
answer_label = AnswerLabel()

game_on = True
guessed_states = []
# Count number of correctly guessed states
state_counter = 0

while state_counter < 50:
    answer_state = str(screen.textinput(title=f"{state_counter}/50 States Correct", prompt="What's another state's name?")).title()
    for i in range(0, 49):
        if answer_state == all_states[i]:
            answer_label.create_label(answer=all_states[i], x=all_x[i], y=all_y[i])
            # Ensure no duplicates in state_counter

            if answer_state not in guessed_states:
                guessed_states.append(answer_state)
                state_counter += 1
        if answer_state == 'Exit':
            break

turtle.mainloop()
