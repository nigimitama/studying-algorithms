def get_score(a):
    scores = a
    while len(scores) >= 2:
        scores = get_scores(scores)
    return scores


def get_scores(a):
    scores = []
    for i in range(1, len(a)):
        score = a[i-1] + a[i]
        if score > 101:
            score -= 101
        scores.append(score)
    return scores


s, t = input().split()
letters = [chr(i) for i in range(97, 97+26)]
numbers = [i for i in range(1, 27)]
letters = dict(zip(letters, numbers))

s_n = [letters[s_i] for s_i in s]
t_n = [letters[t_i] for t_i in t]
scores = get_score(s_n + t_n) + get_score(t_n + s_n)
print(max(scores))
