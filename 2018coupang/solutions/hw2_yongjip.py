#1
def square(xs):
    return [x**2 for x in xs]

#2
def even(xs):
    return [x for x in xs if x%2==0]

#3
def count_other_words(sentence, exclude):
    return len([word for word in sentence.split(' ') if word != exclude])

#4
def delta(xs):
    return [xs[i+1] - xs[i] for i in range(0, len(xs)-1)]

#5.1
def intersection(xs, ys):
    return [x for x in xs if x in ys]

#5.2
def union(xs, ys):
    return [val for i, val in enumerate(ys) if val not in ys[i+1:]] + \
            [val for i, val in enumerate(xs) if val not in xs[i+1:] and val not in ys]

#6
def net_asset_value(inventory, prices):
    return sum([prices[key] * inventory[key] for key in inventory.keys() if key in prices.keys()])

#7
def is_monotonic(xs):
    return abs(sum([(xs[i] - xs[i+1]) / abs(xs[i] - xs[i+1]) for i in range(len(xs)-1) if xs[i] - xs[i+1] != 0])) in [0,len(xs)-1]

#8
def zip(*args):
    min_len = min([len(x) for x in args])
    # out = []
    # for j in range(min_len):
    #     lst = []
    #     for arg in args:
    #         lst.append(arg[j])
    #     out.append(tuple(lst))
    # return out
    return [tuple([arg[j] for j in range(min_len)]) for arg in args]


#8.1
def unzip(iterables):
    min_len = min([len(x) for x in iterables])
    # out = []
    # for j in range(min_len):
    #     lst = []
    #     for iterable in iterables:
    #         lst.append(iterable[j])
    #     out.append(tuple(lst))
    # return out
    return [tuple([arg[j] for arg in iterables]) for j in range(min_len)]


