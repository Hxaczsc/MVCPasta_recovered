class PastaView:
    def __init__(self, controller):
        self.controller = controller


    def print_restaurant_menu(self):
        print(self.controller.get_restaurant_menu)

    def print_web_menu(self):
        print(self.controller.get_web_menu)

    def set_ingredients(self, user_rights, new_ingredients):
        if type(new_ingredients) is not list:
            print("Неверный тип данных")
        set_ingredients_response = self.controller.set_ingredients(user_rights, new_ingredients)
        if set_ingredients_response == "forbidden":
            print("Нет права доступа")
        else:
            print(set_ingredients_response)

    def set_price(self, user_rights, new_price):
        if new_price.isdigit() is False:
            print("Неверный тип данных")
            return
        set_price_response = self.controller.set_price(user_rights, new_price)
        if set_price_response == "forbidden":
            print("Нет права доступа")
        else:
            print(set_price_response)

    def set_weight(self, user_rights, new_weight):
        if new_weight.isdigit() is False:
            print("Неверный тип данных")
            return
        set_weight_response = self.controller.set_weight(user_rights, new_weight)
        if set_weight_response == "forbidden":
            print("Нет права доступа")
        else:
            print(set_weight_response)


    def save_order_to_json(self, order):
        print(self.controller.save_order_to_json(order))

    def get_data_from_json(self, user_rights, filename):
        get_data_from_json_response = self.controller.get_data_from_json(user_rights, filename)
        print("Начало чтения файла...")
        if get_data_from_json_response == "Forbidden":
            print("Отказано в доступе")
        else:
            print(get_data_from_json_response)