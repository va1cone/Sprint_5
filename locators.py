#вход и регистрация https://stellarburgers.nomoreparties.site/login, https://stellarburgers.nomoreparties.site/register

registration_name_entry_field = './/label[text()="Имя"]/following-sibling::input' #поле ввода имени
registration_email_entry_field = './/label[text()="Email"]/following-sibling::input' #поле ввода почты
registration_password_entry_field = 'Пароль' #поле ввода пароля
register_button = "//button[text()='Зарегистрироваться']" #кнопка зарегистрироваться
login_button = "//button[text()='Войти']" #кнопка войти
text_incorrect_password = "//p[text()='Некорректный пароль']" #надпись некорректный пароль
recover_password_button = "//a[text()='Восстановить пароль']" #кнопка Восстановить пароль
Login_button_when_recovering_password = "//a[text()='Войти']"  #кнопка войти при восстановлении пароля

#главная страница https://stellarburgers.nomoreparties.site/

login_button_on_the_main_page = "//button[contains(@class, 'button_button') and text()='Войти в аккаунт']"  #кнопка "войти в аккаунт" на главной
personal_account_button = "//p[text()='Личный Кабинет']"  #кнопка личный кабинет
exit_button = "//button[text()='Выход']"  #кнопка выход в личном кабинете
stellar_burgers_button = "//div[@class = 'AppHeader_header__logo__2D0X2']" #кнопка stellar burgers
button_constructor = "//a[@class = 'AppHeader_header__link__3D_hX']" #кнопка конструктор
collect_burger_text = "//h1[text()='Соберите бургер']" #текст соберите бургер

#конструктор

bun_button = "//span[text()='Булки']/parent::div"  #кнопка булка
sauces_button = "//span[text()='Соусы']/parent::div" #кнопка соусы
stuffing_button = "//span[text()='Начинки']/parent::div" #кнопка начинки

#адресные строки
registration_page = "https://stellarburgers.nomoreparties.site/register" #страница регистрации
login_page = "https://stellarburgers.nomoreparties.site/login" #страница авторизации
home_page = "https://stellarburgers.nomoreparties.site/" #главная страница
profile_page = "https://stellarburgers.nomoreparties.site/account/profile" #страница профиля

#тестовый аккаунт
test_login = "lerochka11@yandex.ru" #почта
test_password = "123456789"  #пароль