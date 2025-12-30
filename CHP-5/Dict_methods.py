marks = {
    "Parth" : 95,
    "Hetvi": 100,
    "Meet" : 98
}

# print(marks.items())
# print(marks.keys())
print(marks.values())
marks.update({"Parth": 94 , "prince" : 95})
print(marks["Hetvi2"]) # will give error if key not found
print(marks.get("Hetvi2")) # will give None if key not found 