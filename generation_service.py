import random
from collections import defaultdict

from generate_dino.models import Dino

START = "^"
END = "$"


def collect_ngram_dist(corpus, n):
    """
    Compute next letter frequencies based on the collected ngrams
    """
    ngram_dist = defaultdict(dict)
    for line in corpus:
        line_split = list(line)

        for i in range(len(line_split) - n + 1):
            key = "".join(line_split[i:i + n - 1])
            val = line_split[i + n - 1]
            try:
                ngram_dist[key][val] += 1
            except:
                ngram_dist[key][val] = 1
    return ngram_dist


def freqs_to_probs(ngram_freqs):
    """
    Сompute next letter probabilities based on the collected ngrams
    """
    ngram_probs = defaultdict(dict)
    for k, v in list(ngram_freqs.items()):
        total = sum(v.values())
        ngram_probs[k] = dict()
        for i in v.keys():
            ngram_probs[k][i] = v[i] / total
    return ngram_probs


def generate_letter(context, ngram_probs):
    try:
        options = ngram_probs[context]
        rand_num = random.random()
        total = 0
        for k in options.keys():
            total += options[k]
            if total > rand_num:
                return k
    except:
        return END


def generate_dino(start, ngram_probs, n, end_sym):
    """
    Generate a new dino species
    """
    next_letter = generate_letter(start, ngram_probs)
    dino_name = start + next_letter
    while next_letter != end_sym:
        next_letter = generate_letter(dino_name[-1 * (n - 1):], ngram_probs)
        dino_name += next_letter
    return dino_name


def create_new_dino_name():
    dino_names = []
    for dino in Dino.objects.all():
        dino_names.append(START + str(dino.name) + END)

    N = 5
    ngram_freqs = collect_ngram_dist(dino_names, N)
    ngram_probs = freqs_to_probs(ngram_freqs)
    possible_begs = [k for k in ngram_probs.keys() if k.startswith(START)]

    random.shuffle(possible_begs)

    for start in possible_begs[:1]:
        return generate_dino(start, ngram_probs, N, END)[1:-1]
