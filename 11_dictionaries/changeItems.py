import this


print("Change Values in dictionary")
thisdict1 = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1960
}
thisdict1["year"] = 1980

print(thisdict1)

print("=================")
print("Update dictionary")
thisdict2 = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1970
}
thisdict2.update({"year" : 1990})
print(thisdict2)