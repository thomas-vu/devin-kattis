def thursday_offer_price(y):
    base_price = 1000
    yearly_increase = 100
    years_since_2020 = y - 2020
    price = base_price + years_since_2020 * yearly_increase
    return price

y = int(input())
print(thursday_offer_price(y))