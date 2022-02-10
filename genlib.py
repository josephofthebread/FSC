import random

WORDS = [
    "sys", "ptr", "data", "address", "runtime", "compiler"
]

HEADERS = [
"<assert.h>", "<limits.h>" ,"<signal.h>", "<stdlib.h>",
"<ctype.h>", "<locale.h>" ,"<stdarg.h>", "<string.h>",
"<errno.h>", "<math.h>" ,"<stddef.h>", "<time.h>",
"<float.h>", "<setjmp.h>" ,"<stdio.h>"]

EXTS = [
    "zip", "psd", "doc", "png","jpg", "jar"
]

def shuffle(l: list):
    c = l.copy()
    random.shuffle(c)
    return c

def random_uppercase(count = 5) -> str:
    return ''.join(shuffle([chr(i) for i in range(ord('A'), ord('Z')+1)])[:count])

def genword(count = 10) -> str:
    res = ""
    for i in range(random.randint(0, 3)):
        res += "_"
    for _ in range(count):
        res += random.choice([random.choice(WORDS), random_uppercase(5)])
        for i in range(random.randint(0, 3)):
            res += "_"
    
    return res

strings = []

def make_connected(prev: str):
    for _ in range(300):
        w = genword(5)
        strings.append(f"#define {w} {prev}")
        prev = w
    
    return prev

HEADER_DEFINES = []
EMPTY_DEFINES = []

for _ in range(15):
    HEADER_DEFINES.append(make_connected(random.choice(HEADERS).replace(".h", "." + random.choice(EXTS))))

for _ in range(5):
    EMPTY_DEFINES.append(make_connected(""))

prev = make_connected("<printf.zip>")

random.shuffle(strings)

# TARGETS = ["PKG."]

with open("include/AZX.jar", "w") as f:
    for s in strings:
        f.write(s + "\n")

TARGET_DEFINE = "KLIB_instr_sys_urt00__127316720472917"
print(f"#define {TARGET_DEFINE} {' '.join(shuffle(shuffle(EMPTY_DEFINES)[:4] + [prev]))}")