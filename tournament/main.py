from points import tally

x = tally([
    "Courageous Californians;Devastating Donkeys;win",
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Allegoric Alaskans;loss",
    "Courageous Californians;Blithering Badgers;win",
    "Blithering Badgers;Devastating Donkeys;draw",
    "Allegoric Alaskans;Courageous Californians;draw",
])

for itens in x:
    print(itens)