import json

booklist = ["The Gruffalo", "The Frog Princess", "Moonlight on the Magic Flute", "Charlotte's Web"]
with open("booklist.json", "w") as outfile:
    outfile.write(booklist)