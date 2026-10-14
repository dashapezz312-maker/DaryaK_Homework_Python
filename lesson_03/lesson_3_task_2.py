from smartphone import Smartphone

catalog = [
    Smartphone("model_1", "brand_1", "+79999999999"),
    Smartphone("model_2", "brand_2", "+79888888888"),
    Smartphone("model_3", "brand_3", "+79777777777"),
    Smartphone("model_4", "brand_4", "+79666666666"),
    Smartphone("model_5", "brand_5", "+79555555555"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
