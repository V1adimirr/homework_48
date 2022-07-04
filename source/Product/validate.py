def product_validate(product, remainder, price):
    errors = {}
    if not product:
        errors["product"] = "Поле обязательное"
    elif len(product) > 100:
        errors["product"] = "Должно быть меньше 100 символов"
    if not remainder:
        errors["remainder"] = "Поле обязательное"
    elif int(remainder) < 0:
        errors["remainder"] = "Должно быть больше ноля"
    if not price:
        errors["price"] = "Поле обязательное"
    elif int(price) < 0:
        errors["price"] = "Должно быть больше нуля"
    return errors
