words = ['california','florida','texas']

capitalized = []
for word in words:
    capitalized.append(word.title())

otherWayToCapitalize = [word.title() for word in words]

print(words)
print(capitalized)
print(otherWayToCapitalize)