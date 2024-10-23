import os.path

from Models.PastaModel import PastaModel
from Controllers.PastaController import PastaController
from Views.PastaView import PastaView

if __name__ == "__main__":
    ImagePath = os.path.abspath("D:/PastaCarbonara.jpg")
    print(ImagePath)
    PastaModel = PastaModel(name="Карбонара",
                             ingredients=["Спагетти", "оливковое масло", "чеснок", "ветчина", "сыр пармезан", "сливки", "соль", "черный перец"],
                             price=475,
                             weight=350,
                             picture=ImagePath,
                             client_ingredients=["двойная порция сыра"]
                             )

    PastaController = PastaController(PastaModel)
    PastaView = PastaView(PastaController)
    PastaView.print_restaurant_menu()
    PastaView.print_web_menu()
    # PastaView.save_order_to_json("Карбонара, измененная")
    PastaView.get_data_from_json("IsSuperuser", r"orders/1729716892.04--Карбонара, измененная.json")
    print("---")
    PastaView.set_ingredients("user", ["Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки", "соль"])
    PastaView.set_ingredients("Admin",("Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки","соль"))
    PastaView.set_ingredients("IsSuperuser",["Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки","соль"])
    print("---")
    PastaView.set_price("user", "500")
    PastaView.set_price("IsStaff", "Пятьсот")
    PastaView.set_price("ISSuperuser", "500")
    print("---")
    PastaView.set_weight("user", "375")
    PastaView.set_weight("IsStaff", "Триста семьдесят пять")
    PastaView.set_weight("ISSuperuser", "375")
    print("---")
    PastaView.print_restaurant_menu()