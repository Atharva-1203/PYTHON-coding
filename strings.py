s="""My name is Atharva Adsul. I am studying Btech as well as IIT M BS    """
print(s.lower())
print(s.upper())
print(s.capitalize())

s.replace("i","y")
print(s)

print(s.count("At"))

print(s.endswith("At"))
print(s.startswith("oo"))

s=s.strip()
print(s)

t="My name is Atharva..."
print(t.split(" "))

l=["A","t","h"]
print("".join(l))