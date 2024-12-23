klutz = {
    "znak1": "Alive",
    "znak2": "Alive",
    "znak3": "Alive",
    "znak4": "Alive",
    "znak5": "Alive",
    "znak6": "Alive",
    "znak7": "Alive",
    "znak8": "Alive",
    "znak9": "Alive",
    "znak10": "Alive",
}
#
klutz["znak2"] = "Dead"
klutz["znak7"] = "Dead"
#
del klutz["znak3"]
klutz["znak4"] = None
#
print(klutz)