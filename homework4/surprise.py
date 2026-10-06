# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_star_names(targets):
    for star in targets:
        print(star)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_star_spectral_types(targets):
    for star in targets:
        print(star, targets[star]["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def mag_check_star(targets):
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star, targets[star]["Magnitude"])

# 4) Look up another target, add all the necessary information to the targets list.

targets["Fomalhaut"] = {
    "RA": "22h 57m 39.0s",
    "Dec": "-29° 37′ 20″",
    "Magnitude": 1.16,
    "Spectral Type": "A0Va"}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def find_brightest_star_closest_to_20(targets):
    closest_dist = float("inf")
    closest_stars = []
    for star in targets:
        dist = abs(int(targets[star]["Dec"][1:3]) - 20)
        if dist < closest_dist:
            closest_dist = dist
            closest_stars = [star]
        elif dist == closest_dist:
            closest_stars += [star]
    brightest = closest_stars[0]
    for star in closest_stars:
        if targets[star]["Magnitude"] < targets[brightest]["Magnitude"]:
            brightest = star
    return brightest

print(find_brightest_star_closest_to_20(targets))

# 6) What is your favorite constellation?

# Cancer


lists = [2,2,3,4,5,1]

print(lists.index(min(lists)))

print(abs(int(targets["Sirius"]["Dec"][1:3]) - 20))
