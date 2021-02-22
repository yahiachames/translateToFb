import timeit
import arabic_reshaper
from bidi.algorithm import get_display
import fitz
doc = fitz.open("arabicTest.pdf", filetype="pdf")
textoutput = doc.getPageText(0, "text")
reshaped = arabic_reshaper.reshape(textoutput)
print(reshaped.splitlines())
arabicLetters = ["أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش",
                 "ص", "ض", "ظ", "ط", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"]

latinLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def test(s):
    string = ""
    for char in s:
        if char == "أ":
            string += "a"
        elif char == "ب":
            string += "b"
        elif char == "ت":
            string += "t"
        elif char == "ث":
            string += "th"
        elif char == "ج":
            string += "b"
        elif char == "ح":
            string += "h"
        elif char == "خ":
            string += "kh"
        elif char == "د":
            string += "d"
        elif char == "ذ":
            string += "dh"
        elif char == "ر":
            string += "r"
        elif char == "ز":
            string += "z"
        elif char == "س":
            string += "s"
        elif char == "ش":
            string += "ch"
        elif char == "ص":
            string += "s"
        elif char == "ض":
            string += "dh"
        elif char == "ط":
            string += "t"
        elif char == "ظ":
            string += "dh"
        elif char == "ع":
            string += "aa"
        elif char == "غ":
            string += "gh"
        elif char == "ف":
            string += "f"
        elif char == "ق":
            string += "k"
        elif char == "ك":
            string += "k"
        elif char == "ل":
            string += "l"
        elif char == "م":
            string += "m"
        elif char == "ن":
            string += "n"
        elif char == "ه":
            string += "h"
        elif char == "و":
            string += "w"
        elif char == "ي":
            string += "y"
        else:
            string += char
    return string


for i in textoutput.splitlines():

    print("".join(list(map(test, i))))

print(test("شمس"))
print(timeit.timeit("""
import timeit
import arabic_reshaper
from bidi.algorithm import get_display
import fitz
doc = fitz.open("arabicTest.pdf", filetype="pdf")
textoutput = doc.getPageText(0, "text")
def test(s):
    string = ""
    for char in s:
        if char == "أ":
            string += "a"
        elif char == "ب":
            string += "b"
        elif char == "ت":
            string += "t"
        elif char == "ث":
            string += "th"
        elif char == "ج":
            string += "b"
        elif char == "ح":
            string += "h"
        elif char == "خ":
            string += "kh"
        elif char == "د":
            string += "d"
        elif char == "ذ":
            string += "dh"
        elif char == "ر":
            string += "r"
        elif char == "ز":
            string += "z"
        elif char == "س":
            string += "s"
        elif char == "ش":
            string += "ch"
        elif char == "ص":
            string += "s"
        elif char == "ض":
            string += "dh"
        elif char == "ط":
            string += "t"
        elif char == "ظ":
            string += "dh"
        elif char == "ع":
            string += "aa"
        elif char == "غ":
            string += "gh"
        elif char == "ف":
            string += "f"
        elif char == "ق":
            string += "k"
        elif char == "ك":
            string += "k"
        elif char == "ل":
            string += "l"
        elif char == "م":
            string += "m"
        elif char == "ن":
            string += "n"
        elif char == "ه":
            string += "h"
        elif char == "و":
            string += "w"
        elif char == "ي":
            string += "y"
        else:
            string += char
    return string
for i in textoutput.splitlines():
    print("".join(list(map(test, i))))
              """, number=1))
