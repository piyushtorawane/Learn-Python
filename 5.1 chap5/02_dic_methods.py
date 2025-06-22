marks ={
    "Piyush": 110,
    "Harry": 100,
    "Suyash":99,
    0: "Piyush"
}
#print(marks, type(marks))
#print(marks.items())
#print(marks.keys())
#print(marks.values())
marks.update({"Harry":99, "Kash":88})
print(marks)
print(marks.get("Harry2"))# Prints none
print(marks["Harry2"]) # Returns error