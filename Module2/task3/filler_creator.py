import random

# Создание и заполнение таблицы Product
makers = ["A", "B", "C", "D", "E"]
models_pc = list(range(1000, 2000))
models_laptop = list(range(2000, 3000))
models_printer = list(range(3000, 4000))
random.shuffle(models_pc)
random.shuffle(models_laptop)
random.shuffle(models_printer)

with open("Module2/task3/create_and_fill_Product.sql", "w") as file:
    file.write(
        "CREATE TABLE Product (maker CHAR(1), model INTEGER, type VARCHAR(10));\n"
    )
    file.write("INSERT INTO Product\nVALUES\n")
    product_values = []

    # Генерация PC
    for maker in makers:
        num = random.randint(20, 40)
        selected = models_pc[:num]
        models_pc = models_pc[num:]
        for model in selected:
            product_values.append(f"('{maker}', {model}, 'PC')")

    # Генерация Laptop (не все производители)
    for maker in makers:
        if random.choice([True, False]):
            num = random.randint(20, 40)
            selected = models_laptop[:num]
            models_laptop = models_laptop[num:]
            for model in selected:
                product_values.append(f"('{maker}', {model}, 'Laptop')")

    # Генерация Printer
    for maker in makers:
        if random.choice([True, False]):
            num = random.randint(20, 40)
            selected = models_printer[:num]
            models_printer = models_printer[num:]
            for model in selected:
                product_values.append(f"('{maker}', {model}, 'Printer')")

    file.write(",\n".join(product_values) + ";\n")

# Скрипт для PC
with open("Module2/task3/create_and_fill_PC.sql", "w") as file:
    file.write(
        "CREATE TABLE PC (code INTEGER PRIMARY KEY, model INTEGER, speed INTEGER, ram INTEGER, hd NUMERIC(10,1), cd VARCHAR(50), price NUMERIC(10,4));\n"
    )
    file.write("INSERT INTO PC\nVALUES\n")
    values = []
    for code in range(1, 101):
        model = random.choice(models_pc[:100])  # Берем существующие модели из Product
        speed = random.randrange(500, 901, 100)
        ram = random.randrange(32, 129, 32)
        hd = random.randrange(5, 21, 5)
        cd = f"{random.randrange(12, 53, 4)}x"
        price = random.randrange(350, 1001, 50)
        values.append(f"({code}, {model}, {speed}, {ram}, {hd}, '{cd}', {price})")

    # Добавляем 2 дубликата
    values.append("(101, 1232, 500, 64, 5.0, '12x', 600.00)")
    values.append("(102, 1232, 500, 64, 5.0, '12x', 600.00)")

    file.write(",\n".join(values) + ";\n")

# Скрипт для Laptop
with open("Module2/task3/create_and_fill_Laptop.sql", "w") as file:
    file.write(
        "CREATE TABLE Laptop (code INTEGER PRIMARY KEY, model INTEGER, "
        "speed INTEGER, ram INTEGER, hd NUMERIC(10,1), "
        "screen NUMERIC(4,1), price NUMERIC(10,4));\n"
    )
    file.write("INSERT INTO Laptop\nVALUES\n")

    laptop_values = []
    for code in range(1, 101):
        model = random.choice(
            models_laptop[:100]
        )  # Берем существующие модели из Product
        speed = random.randrange(500, 901, 100)
        ram = random.randrange(32, 129, 32)
        hd = random.randrange(5, 21, 5)
        screen = round(random.uniform(11.0, 17.0), 1)
        price = random.randrange(500, 2001, 50)

        laptop_values.append(
            f"({code}, {model}, {speed}, {ram}, {hd}, {screen}, {price})"
        )

    # Добавляем 2 дубликата
    laptop_values.append("(101, 2001, 600, 64, 10.0, 15.6, 1200.00)")
    laptop_values.append("(102, 2001, 600, 64, 10.0, 15.6, 1200.00)")

    file.write(",\n".join(laptop_values) + ";\n")

# Скрипт для Printer
with open("Module2/task3/create_and_fill_Printer.sql", "w") as file:
    file.write(
        "CREATE TABLE Printer (code INTEGER PRIMARY KEY, model INTEGER, "
        "color CHAR(1), type VARCHAR(10), price NUMERIC(10,4));\n"
    )
    file.write("INSERT INTO Printer\nVALUES\n")

    printer_values = []
    printer_types = ["Laser", "Jet", "Matrix"]

    for code in range(1, 101):
        model = random.choice(
            models_printer[:100]
        )  # Берем существующие модели из Product
        color = random.choice(["y", "n"])
        pr_type = random.choice(printer_types)
        price = random.randrange(100, 501, 50)

        printer_values.append(f"({code}, {model}, '{color}', '{pr_type}', {price})")

    # Добавляем 2 дубликата
    printer_values.append("(101, 3001, 'n', 'Matrix', 150.00)")
    printer_values.append("(102, 3001, 'n', 'Matrix', 150.00)")

    file.write(",\n".join(printer_values) + ";\n")
