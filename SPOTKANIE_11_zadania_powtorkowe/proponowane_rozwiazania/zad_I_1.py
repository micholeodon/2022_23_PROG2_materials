distanceKm = 187        # in km
fuelConsumptionPerKm = 7/100    # in liters per km
pricePerLiter = 6.65    # in PLN

# ile zatankowac
load = distanceKm*fuelConsumptionPerKm

# ile zaplace za benzyne do poznania
pricePerTrip = load*pricePerLiter

print(f"Zatankuj {round(load,2)} litrów. ")
print(f"Przy cenie {pricePerLiter} PLN za litr zapłacisz {round(pricePerTrip,2)} PLN")
