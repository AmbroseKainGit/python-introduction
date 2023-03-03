movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something youve watched recently: ")
if user_movie in movies_watched:
    print('MOVIE ALREADY WATCHER')
else:
    print('havent watched that yet')

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()
if user_input in ("y", "Y") :
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print('YOU WIN')
    elif abs(number - user_number) == 1:    
        print('You were off by one.')
    else:
        print('YOU LOSE ')
