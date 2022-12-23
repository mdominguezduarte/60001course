# Tuples, Lists, Aliasing, Mutability, and Cloning

# save new english words in a tuple
def save_words():
    default_tuple = ("dog", "mouse", "cat", "rabbit", "rabbit")
    register = 0
    english = ()
    for t in default_tuple:
        if t not in english:
            english = english + (t,)
            register += 1
            print("Date is saved:", (t,))
        else:
            print(t, "is not saved.")
            continue
    print("Number of words:", register)
    print("Number of storage data:", len(english))
    print("Update English tuple: ", english)


# get min num value, max num value and the length of unique characters
def get_min_max_len_data(adata):
    num_value = ()
    char_value = ()
    for t in adata:
        num_value = num_value + (t[0],)
        if t[1] not in char_value:
            char_value = char_value + (t[1],)
    min_value = min(num_value)
    max_value = max(num_value)
    different_char = len(char_value)
    return min_value, max_value, different_char


# get watched videos applying get_min_max_len_data function
def get_watched_videos():
    histo_youtube = ((2015, "Someone like you (Official Music Video)"),
                     (2022, "Ed Sheeran - Thinking Out Loud (Official Music Video)"),
                     (2017, "Justin Bieber - Love Yourself (PURPOSE : The Movement)"),
                     (2019, "Justin Bieber - Love Yourself (PURPOSE : The Movement)"))
    (min_year, max_year, num_video_song) = get_min_max_len_data(histo_youtube)

    print(f"From {min_year} to {max_year} the number of unique youtube  music videos watched is {num_video_song}.")


def get_movies_from_actor():
    chris_evans = ((2019, "Avengers: Endgame"),
                   (2019, "Knives Out"),
                   (2022, "Lightyear"),
                   (2022, "The Gray Man "))
    (min_year, max_year, num_movies) = get_min_max_len_data(chris_evans)
    print(f"From {min_year} to {max_year} the number of Chris Evans movies is {num_movies}.")
