def red():
    start = 10**12
    money = 0
    for minute in range(60*24):
        money += start
    return money

def blue():
    money = 0.01
    red_ = red()
    blue_is_more = False
    for second in range(60*60):
        money *= 2
        if not blue_is_more and money > red_:
            print(f"After {second//60}:{second%60} "\
                  "blue overtook red")
            blue_is_more = True
    return money

print(blue() > red()) # true
