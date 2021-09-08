def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            number_dishes = int(file.readline())
            dish_list = []
            for ingredient in range(number_dishes):
                ingredient_name, quantity, measure = file.readline().split('|')
                dish_list.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()}
                )
            result[dish_name] = dish_list
            file.readline()
    return result

result_dict = prepare_dict("recipes.txt")

print(result_dict)