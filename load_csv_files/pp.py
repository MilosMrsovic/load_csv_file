def reci(rr):
    return [r for r in rr if len(r) > 5]

print(reci(["Python", "programiranje", "kultura", "auto", "razvoj"]))