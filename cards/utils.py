
CONDITION_CHOICES = (
    ('Новый', 'new'),
    ('Бу', 'used')
)

CAR_BODY = (
    ('Седан', 'sedan'),
    ('Хэтчбек', 'hatchback'),
    ('Универсал', 'wagon'),
    ('Купе', 'coupe'),
    ('Кабриолет', 'convertible'),
    ('Кроссовер', 'crossover'),
    ('Внедорожник', 'suv'),
    ('Минивэн', 'minivan'),
    ('Пикап', 'pickup'),
    ('Лифтбек', 'liftback'),
)

FUEL = (
    ('Бензин', 'Gasoline'),
    ('Дизель', 'Diesel'),
    ('Электрический', 'Electric'),
    ('Гибридные', 'Hybrid')
)

COLOR_CAR = (
    ('Белый', 'White'),
    ('Черный', 'Black'),
    ('Серый', 'Gray'),
    ('Серебристый', 'Silver'),
    ('Синий', 'Blue'),
    ('Красный', 'Красный'),
    ('Коричневый', 'Brown'),
    ('Бронзовый', 'Bronze'),
    ('Зеленый', 'Green'),
    ('Желтый', 'Yellow'),
    ('Оранжевый', 'Orange')
)

AVAILABILITY = (
    ('В наличии', 'In stock'),
    ('Нет', 'No')
)

TECHNICAL_CONDITION = (
    ('Новый', 'New'),
    ('Как новый', 'Like new'),
    ('Хорошее состояние', 'Good condition'),
    ('Удовлетворительное состояние', 'Satisfactory condition'),
    ('Неисправное состояние', 'Faulty condition'),
    ('После аварии', 'After the accident'),
    ('Требует капитального ремонта', 'Needs major renovation'),
    ('На запчасти', 'For spare parts')
)

TRANSMISSION = (
    ('Механическая', 'Manual'),
    ('Автоматическая', 'Automatic'),
    ('Роботизированная', 'Robotized'),
    ('Роботизированная с двумя сцеплениями', 'Dual-Clutch'),
    ('Вариатор', 'Continuously Variable')
)

STEERING_WHEEL = (
    ('Слева', 'Left'),
    ('Справа', 'Right')
)

DRIVE = (
    ('Передний', 'Front'),
    ('Задний', 'Rear'),
    ('Полный', 'Full')
)

VIN_CODE = (
    ('с VIN кодом', 'with VIN code'),
    ('без VIN кодом', 'without VIN code')
)

CUSTOMS_CLEARANCE = (
    ('Растаможен', 'Cleared by customs'),
    ('Не растаможен', 'Not cleared by customs')
)