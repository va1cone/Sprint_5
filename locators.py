import random
#вход:
registration_name_entry_field = './/label[text()="Имя"]/following-sibling::input' #поле ввода имени на странице регистрации
registration_email_entry_field = './/label[text()="Email"]/following-sibling::input' #поле ввода почты на странице регистрации
registration_password_entry_field = 'Пароль' #поле ввода пароля на странице регистрации
register_button = "//button[text()='Зарегистрироваться']" #кнопка зарегистрироваться
new_email = f"valeria_shishkina_13{random.randint(100, 999)}@yandex.ru" #создание новой почты
#header_input = "//div/main/div/h2" #надпись вход на странице входа
text_incorrect_password = "//div/main/div/form/fieldset[3]/div/p" #надпись некорректный пароль

login_button = "//div/main/div/form/button" #кнопка войти
button_place_an_order = "//div/main/section[2]/div/button" #кнопка оформить заказ
login_button_on_the_main_page = "//div/main/section[2]/div/button"  #кнопка "войти в аккаунт" на главной
personal_account_button = "//div/header/nav/a/p"  #кнопка личный кабинет
exit_button = "//div/main/div/nav/ul/li[3]/button"  #кнопка выход
stellar_burgers_button = "//div/header/nav/div/a" #кнопка stellar burgers
recover_password_button = "//div/main/div/div/p[2]/a" #кнопка Восстановить пароль
Login_button_when_recovering_password = "//div/main/div/div/p/a"  #кнопка войти при восстановлении пароля
button_constructor = "//div/header/nav/ul/li[1]/a/p" #кнопка конструктор

#конструктор

bun_button = "//div/main/section[1]/div[1]/div[1]"  #кнопка булка
sauces_button = "//div/main/section[1]/div[1]/div[2]" #кнопка соусы
stuffing_button = "//div/main/section[1]/div[1]/div[3]" #кнопка начинки