def run():
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3
    }

    population_countries = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }

    for country in population_countries.keys():
        print(country)

    for country in population_countries.values():
        print(country)

    for country, population in population_countries.items():
        print(country + ' has ' + str(population) + ' population')


if __name__ == "__main__":
    run()
