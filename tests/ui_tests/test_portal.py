import time

from pages.login_page import LoginPage
from pages.product_page import ProductPage


"""
Тест 1
1. Авторизоваться на портале (получить логин и пароль с футера)
2. Добавить любой товар в корзину
3. Перейти в корзину
4. Подтвердить заказ
5. Заполнить информацию заказа
6. Завершить заказ
7. Проверить что заказ успешно завершен
"""

"""
Тест 2
1. Авторизоваться на портале (получить логин и пароль с футера)
2. Отсортировать товары от минимального до максимального (по цене)
3. Добавить товар с минимальной ценой в корзину
4. Перейти в корзину
5. Подтвердить заказ
6. Заполнить информацию заказа
7. Завершить заказ
8. Проверить что заказ успешно завершен
"""

"""
Тест 3
1. Авторизоваться на портале (получить логин и пароль с футера)
2. Отсортировать товары в обратном алфавитном порядке
3. Добавить товар в корзину
4. Перейти в корзину
5. Удалить заказ
6. Проверить что заказ удален (корзина должна быть пуста)
"""


"""
Тест 4
1. Авторизоваться на портале заблоченым пользователем(получить логин и пароль с футера)
2. Проверить что отображается ошибка что пользователь заблокирован
"""


"""
Тест 5
1. Авторизоваться на портале (получить логин и пароль с футера)
2. Добавить все товары в корзину
3. Перейти в корзину
4. Подтвердить заказ
5. Заполнить информацию заказа
6. Завершить заказ
7. Проверить что заказ успешно завершен
"""