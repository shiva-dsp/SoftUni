def find_all_solutions(idx, target, words_by_index, words_count, used_words):
    if idx >= len(target):
        print(' '.join(used_words))
        return
    if idx not in words_by_index:
        return
    for word in words_by_index[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), target, words_by_index, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_by_index = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_index:
                words_by_index[idx] = []
            words_by_index[idx].append(word)
            idx += len(word)

    except ValueError:
        pass

find_all_solutions(0, target, words_by_index, words_count, [])

# --------- tests ----------

# text, me, so, do, m, ran
# somerandomtext
#
# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher
#
# tu, stu, p, i, d, pi, pid, s, pi
# stupid

#  --------- results ----------

# so me ran do m text

# Word c r un ch er
# Word c r unch er
# Word cr un c h er
# Word cr un ch er
# Word cr unch er
# Word cruncher

# s tu p i d
# s tu pi d
# s tu pid
# stu p i d
# stu pi d
# stu pid