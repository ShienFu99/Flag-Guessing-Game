from os import system
from random import shuffle


def main():
    score = 0
    flag_counter = 1

    country_flags = [
        {"country_name": "afghanistan", "img_file_name": "af.png"},
        {"country_name": "albania", "img_file_name": "al.png"},
        {"country_name": "algeria", "img_file_name": "dz.png"}
    ]

    # Shuffles the entries in the list
    shuffle(country_flags)

    for d in country_flags:
        print(f"Flag {flag_counter}")
        print(d["img_file_name"])
        user_guess = input("What country is this? ").lower().strip()

        if user_guess == d["country_name"]:
            score += 1

        flag_counter += 1
        system("clear")

    print(f"You guessed {score}/{len(country_flags)} flags correct.")


if __name__ == "__main__":
    main()
