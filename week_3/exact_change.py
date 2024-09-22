coin_types = [
    ("Dollar", 100),
    ("Quarter", 25),
    ("Dime", 10),
    ("Nickel", 5),
    ("Penny", 1),
]

change_amount = int(input())

if change_amount == 0:
    print("No change needed.")
i = 0
while change_amount > 0 and i < len(coin_types):
    coin_name, coin_value = coin_types[i]
    coin_count = change_amount // coin_value
    if coin_count > 0:
        if coin_count == 1:
            print(f"1 {coin_name}")
        else:
            print(f"{coin_count} {coin_name}s")
    change_amount %= coin_value
    i += 1
