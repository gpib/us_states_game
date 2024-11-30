import turtle
import pandas as pd
from datetime import datetime

# Inicjalizacja ekranu gry
screen = turtle.Screen()
screen.title("U.S. game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Inicjalizacja gry
answered = 0
game_on = True

# Wczytanie danych o stanach USA
us_df = pd.read_csv("50_states.csv")

# Inicjalizacja żółwia do wyświetlania komunikatów
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()

# Inicjalizacja żółwia do rysowania stanów
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

# Pętla gry
while game_on:
    user_answer = screen.textinput(title=f"{answered}/50 Guess the state", prompt="Give the name of the state").title()

    # Sprawdzenie, czy użytkownik chce zakończyć grę
    if user_answer == "Exit":
        current_time = datetime.now().strftime("%H%M%S")
        us_df.to_csv(f"remaining_states_{current_time}.csv", index=False)
        break

    # Sprawdzenie poprawności odpowiedzi
    if user_answer in us_df['state'].values:
        # Rysowanie stanu na mapie
        current_state = us_df[us_df.state == user_answer]
        state_turtle.goto(current_state.x.item(), current_state.y.item())
        state_turtle.write(user_answer)

        # Zwiększanie liczby odpowiedzi
        answered += 1

        # Usuwanie stanu z DataFrame
        us_df.drop(us_df[us_df.state == user_answer].index, inplace=True)

        # Czyszczenie komunikatu o błędzie, jeśli odpowiedź jest poprawna
        message_turtle.clear()

        # Sprawdzenie, czy gra powinna się zakończyć
        if answered == 50 or us_df.empty:
            game_on = False
    else:
        # Wyświetlanie komunikatu o błędnej odpowiedzi
        print(f"{user_answer} is not a valid state.")
        message_turtle.goto(0, 50)  # Możesz zmienić pozycję na odpowiednią
        message_turtle.write("Invalid state! Try again.", align="center", font=("Arial", 12, "normal"))

turtle.mainloop()