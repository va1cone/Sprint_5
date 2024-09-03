import random

#вход и регистрация https://stellarburgers.nomoreparties.site/login, https://stellarburgers.nomoreparties.site/register

registration_name_entry_field = './/label[text()="Имя"]/following-sibling::input' #поле ввода имени
registration_email_entry_field = './/label[text()="Email"]/following-sibling::input' #поле ввода почты
registration_password_entry_field = 'Пароль' #поле ввода пароля
register_button = "//button[text()='Зарегистрироваться']" #кнопка зарегистрироваться
login_button = "//div/main/div/form/button" #кнопка войти
text_incorrect_password = "//div/main/div/form/fieldset[3]/div/p" #надпись некорректный пароль
recover_password_button = "//div/main/div/div/p[2]/a" #кнопка Восстановить пароль
Login_button_when_recovering_password = "//div/main/div/div/p/a"  #кнопка войти при восстановлении пароля

#генератор новых почт для теста

new_email = f"valeria_shishkina_13{random.randint(100, 9999)}@yandex.ru" #создание новой почты
new_email2 = f"valeria_shishkina_13{random.randint(10, 9999)}@yandex.ru" #создание новой почты
new_email3 = f"valeria_shishkina_13{random.randint(10, 9999)}@yandex.ru" #создание новой почты
new_email4 = f"valeria_shishkina_13{random.randint(10, 9999)}@yandex.ru" #создание новой почты

#главная страница https://stellarburgers.nomoreparties.site/

button_place_an_order = "//div/main/section[2]/div/button" #кнопка оформить заказ
login_button_on_the_main_page = "//div/main/section[2]/div/button"  #кнопка "войти в аккаунт" на главной
personal_account_button = "//div/header/nav/a/p"  #кнопка личный кабинет
exit_button = "//div/main/div/nav/ul/li[3]/button"  #кнопка выход в личном кабинете
stellar_burgers_button = "//div/header/nav/div/a" #кнопка stellar burgers
button_constructor = "//div/header/nav/ul/li[1]/a/p" #кнопка конструктор

#конструктор

bun_button = "//div/main/section[1]/div[1]/div[1]"  #кнопка булка
sauces_button = "//div/main/section[1]/div[1]/div[2]" #кнопка соусы
stuffing_button = "//div/main/section[1]/div[1]/div[3]" #кнопка начинки