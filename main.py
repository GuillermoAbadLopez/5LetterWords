import time

start = time.time()

words = []
abc_set = {
    "a": set(),
    "b": set(),
    "c": set(),
    "d": set(),
    "e": set(),
    "f": set(),
    "g": set(),
    "h": set(),
    "i": set(),
    "j": set(),
    "k": set(),
    "l": set(),
    "m": set(),
    "n": set(),
    "o": set(),
    "p": set(),
    "q": set(),
    "r": set(),
    "s": set(),
    "t": set(),
    "u": set(),
    "v": set(),
    "w": set(),
    "x": set(),
    "y": set(),
    "z": set(),
}

# words_alpha.txt from https://github.com/dwyl/english-words
with open("./words_alpha.txt") as f:
    for word in f:
        word = word[:-2]
        word_set = set(word)
        if len(word_set) == len(word) == 5:
            words.append(word)

for word in words:
    for letter in abc_set:
        if letter not in word:
            abc_set[letter].add(word)


def function():
    for word in words:
        second_words = (
            abc_set[word[0]]
            .intersection(abc_set[word[1]])
            .intersection(abc_set[word[2]])
            .intersection(abc_set[word[3]])
            .intersection(abc_set[word[4]])
        )
        if second_words == set():
            break
        for second_word in second_words:
            third_words = (
                second_words.intersection(abc_set[second_word[0]])
                .intersection(abc_set[second_word[1]])
                .intersection(abc_set[second_word[2]])
                .intersection(abc_set[second_word[3]])
                .intersection(abc_set[second_word[4]])
            )
            if third_words == set():
                break
            for third_word in third_words:
                fourth_words = (
                    third_words.intersection(abc_set[third_word[0]])
                    .intersection(abc_set[third_word[1]])
                    .intersection(abc_set[third_word[2]])
                    .intersection(abc_set[third_word[3]])
                    .intersection(abc_set[third_word[4]])
                )
                if fourth_words == set():
                    break
                for fourth_word in fourth_words:
                    fifth_words = (
                        fourth_words.intersection(abc_set[fourth_word[0]])
                        .intersection(abc_set[fourth_word[1]])
                        .intersection(abc_set[fourth_word[2]])
                        .intersection(abc_set[fourth_word[3]])
                        .intersection(abc_set[fourth_word[4]])
                    )
                    if fourth_words == set():
                        break
                    for fifth_word in fifth_words:
                        print({word, second_word, third_word, fourth_word, fifth_word})
                        return


function()
end = time.time()

print(f"Time: {end-start}")
