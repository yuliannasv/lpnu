def get_person_info():
    full_name = input("Введіть Прізвище Ім'я: ")
    birth_year = input("Введіть рік народження: ")
    return full_name, birth_year


def display_info(full_name, birth_year):
    print(f"{full_name} {birth_year} р. н.")

    surname, name = full_name.split()

    print(f"Прізвище: {surname}")
    print(f"Ім’я: {name}")
    print(f"Рік народження: {birth_year}")


if __name__ == "__main__":
    full_name, birth_year = get_person_info()
    display_info(full_name, birth_year)