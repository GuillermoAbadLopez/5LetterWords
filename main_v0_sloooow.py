import time

start = time.time()

words = []
abc = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

counter = 0

# words_alpha.txt from https://github.com/dwyl/english-words
with open("./words_alpha.txt") as f:
    for word in f:
        word = word[:-2]
        word_set = set(word)
        if len(word_set) == len(word) == 5:
            words.append(word)
            for letter in abc:
                if word.startswith(letter):
                    abc[letter] = counter
            counter += 1


def function():
    for word in words:
        start_i = abc[word[0]]
        for wj in words[start_i:]:
            if len(set(word) - set(wj)) == 5:
                start_j = abc[wj[0]]
                for wk in words[(start_j):]:
                    if len(set(wk) - set(wj)) == len(set(word) - set(wk)) == 5:
                        start_k = abc[wk[0]]
                        for wl in words[start_k:]:
                            if len(set(wl) - set(wj)) == len(set(word) - set(wl)) == len(set(wk) - set(wl)) == 5:
                                start_l = abc[wl[0]]
                                for w in words[start_l:]:
                                    if (
                                        len(set(w) - set(word))
                                        == len(set(w) - set(wj))
                                        == len(set(w) - set(wk))
                                        == len(set(w) - set(wl))
                                        == 5
                                    ):
                                        set_words = {word, wj, wk, wl, w}
                                        print(set_words)
                                        return


function()
end = time.time()

print(f"Time: {end-start}")
