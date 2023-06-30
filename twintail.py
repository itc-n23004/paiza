def twintail(s, t):
    progress = "-" * s
    progress = progress[: t - 1] + "+" + progress[t:]
    return progress


s = int(input())
t = int(input())

result = twintail(s, t)
print(result)
