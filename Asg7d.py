leapyearlist = list(
    filter(
        lambda x: ((x % 400 == 0) or (x % 100 != 0 and x % 4 == 0)), range(2024, 3011)
    )
)
print("All Leap Years Between 2024 To 3010 Are: ", leapyearlist)
