from address import Address
from mailing import Mailing

to_addresser = Address("614000", "Перьм", "Ленина", "7", "15")
from_addresser = Address("446000", "Сызрань", "Советская", "11", "54")

mailing = Mailing(
    to_address=to_addresser,
    from_address=from_addresser,
    cost=857,
    track="TRK850463547"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house_number} - {mailing.from_address.apartment_number} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house_number} - {mailing.to_address.apartment_number}. "
    f"Стоимость {mailing.cost} рублей."
)