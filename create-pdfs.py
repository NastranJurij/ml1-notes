import os

chapters = (
    ("introduction", 5),
    ("trees-and-forests", 17),
    ("feature-selection", 30),
    ("END", 42)
)


def pairs(x):
    for i in range(len(x)-1):
        yield x[i], x[i+1]

for a, b in pairs(chapters):
    cmd = "pdfjam notes.pdf %d-%d -o pdfs/%s.pdf" % (a[1], b[1]-1, a[0])
    os.system(cmd)
