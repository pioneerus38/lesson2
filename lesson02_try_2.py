product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5}

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError):
        print("Ошибка: передан аргумент неверного типа.") 
        print("Цена и скидка - вещественные числа, максимальная скидка - целое число.")
        return 0
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)
    