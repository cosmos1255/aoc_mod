import requests


# may use this some day lmao, deff need to work on it though
def submit(level, answer, year, day, SESSION_ID, USER_AGENT):
    URL_DAY_MAIN = f"https://adventofcode.com/{year}/day/{day}/answer"

    day_res = requests.post(
        URL_DAY_MAIN,
        data={"level": level, "answer": answer},
        cookies={"session": SESSION_ID, "User-Agent": USER_AGENT},
        timeout=5,
    )

    message = day_res.content

    if b"That's the right answer" in message:
        print("You got the correct answer!!")
    elif b"Did you already complete it" in message:
        print("Already completed this challenge.")
    elif b"That's not the right answer" in message:
        if b"too high" in message:
            print("Wrong answer, too high, try again.")
        elif b"too low" in message:
            print("Wrong answer, too low, try again.")
        else:
            print("Wrong answer, try again.")
    elif b"You gave an answer too recently" in message:
        print("Gave an answer too recently, try again later.")
