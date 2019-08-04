import collections

DoubleEnded=collections.deque(["mon","tue"])

DoubleEnded.append("h")

DoubleEnded.appendleft("ddd")

DoubleEnded.append("gg")

DoubleEnded.popleft()
DoubleEnded.popleft()

print(DoubleEnded)