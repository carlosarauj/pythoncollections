familia = ["Roger", "cris", "Manu", "Vini", "selina"]

print(familia[3])
print(familia[-1])
print(familia[2:4])

familia[3] = "Roger"

print(familia[3])

familia.extend(["Carlos"])

print(familia)

familia.append("Bob")

print(familia)

familia.insert(2,"Spock")

print(familia)

familia.pop()

print(familia)

familia.remove("Manu")

print(familia)

print(familia.count("Carlos"))

familia.reverse()

print(familia)