import os
import sys
import time

import requests
import string
import random
import json
import re
import telebot
import ua_generator
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
from concurrent.futures import ThreadPoolExecutor


import stepLabLib

attempts_for_response = 0
found_numbers = 0
sucsesful = 0
invalid_account = 0
mails_for_regestration = []
number_list = []
path_to_dir = os.path.dirname(sys.executable)

botEx = telebot.TeleBot('6516240750:AAHHSC0BlT4xloCif5DP-45NoHBVbQ9Ogtk')
bot2 = telebot.TeleBot('7076742172:AAHXae2zRAvlUrin_yo4vrpD35DESjwJyOU')

# >>> Ввод имени (ФОРМА РЕГИСТРИАЦИИ)
xpath_entry_FirstName = stepLabLib.get_path('xpath_entry_FirstName', 'AUTO_REG_PATHS')

# >>> Ввод фамилии (ФОРМА РЕГИСТРАЦИИ)
xpath_entry_SecondName = stepLabLib.get_path('xpath_entry_SecondName', 'AUTO_REG_PATHS')

# >>> Ввод дня рождения (ФОРМА РЕГИСТРАЦИИ)
xpath_entry_birthDay = stepLabLib.get_path('xpath_entry_birthDay', 'AUTO_REG_PATHS')

# >>> Ввод паролья (ФОРМА РЕГИСТРАЦИИ)
xpath_entry_password = stepLabLib.get_path('xpath_entry_password', 'AUTO_REG_PATHS')

# >>> Ввод подтверждения пароль (ФОРМА РЕГИСТРАЦИИ)
xpath_entry_passwordTwo = stepLabLib.get_path('xpath_entry_passwordTwo', 'AUTO_REG_PATHS')

# >>> Ввод почты (ФОРМА РЕГИСТРАЦИИ)
xpath_entry_Email = stepLabLib.get_path('xpath_entry_Email', 'AUTO_REG_PATHS')

# >>> Подтвердить данные для регистрации (ФОРМА РЕГИСТРАЦИИ)
xpath_accpet_registration = stepLabLib.get_path('xpath_accpet_registration', 'AUTO_REG_PATHS')

# >>> Переход на сайт после регистрации (ФОРМА РЕГИСТРАЦИИ)
xpath_btn_next = stepLabLib.get_path('xpath_btn_next', 'AUTO_REG_PATHS')

# >>> Ввод номера телефона

# >>> Кнопка войти (ГЛАВНАЯ СТРАНИЦА ММ)
xpath_entrance = stepLabLib.get_path('xpath_entrance', 'AUTO_REG_PATHS')

auth_with_sberID_btn_path = stepLabLib.get_path('auth_with_sberID_btn_path', 'AUTO_REG_PATHS')

# >>> Ввод номера телефона для регистрации
xpath_entry_number = stepLabLib.get_path('xpath_entry_number', 'AUTO_REG_PATHS')

# >>> Подтверждение введеного номера телефона для регистрации
xpath_entry_number_accept_btn = stepLabLib.get_path('xpath_entry_number_accept_btn', 'AUTO_REG_PATHS')

xpath_entry_verification = stepLabLib.get_path('xpath_entry_verification', 'AUTO_REG_PATHS')


# >>> Прогрев

# Кнопка купить в карточке товара
buy_btn_path = stepLabLib.get_path('buy_btn_path', 'AUTO_REG_PATHS')

# Кнопка перейти в корзину в карточке товара

go_to_cors_list_path = stepLabLib.get_path('go_to_cors_list_path', 'AUTO_REG_PATHS')

# Кнопка оформить заказ

go_to_order_create_path = stepLabLib.get_path('go_to_order_create_path', 'AUTO_REG_PATHS')
# Предложение об оформлении карты

cancle_window_path = stepLabLib.get_path('cancle_window_path', 'AUTO_REG_PATHS')

# Ввод адреса

entry_addres_path = stepLabLib.get_path('entry_addres_path', 'AUTO_REG_PATHS')

# Выбор способа оплаты

sber_pay_span_path = stepLabLib.get_path('sber_pay_span_path', 'AUTO_REG_PATHS')

cancle_order_path = stepLabLib.get_path('cancle_order_path', 'AUTO_REG_PATHS')

reason_cancel_path = stepLabLib.get_path('reason_cancel_path', 'AUTO_REG_PATHS')

accept_btn_cancel_order_path = stepLabLib.get_path('accept_btn_cancel_order_path', 'AUTO_REG_PATHS')

entry_entrance_path = stepLabLib.get_path('entry_entrance_path', 'AUTO_REG_PATHS')

entry_floor_path = stepLabLib.get_path('entry_floor_path', 'AUTO_REG_PATHS')

entry_block_path = stepLabLib.get_path('entry_block_path', 'AUTO_REG_PATHS')

entry_domofon_path = stepLabLib.get_path('entry_domofon_path', 'AUTO_REG_PATHS')

on_sber_bonus_path = stepLabLib.get_path('on_sber_bonus_path', 'AUTO_REG_PATHS')

accept_on_sber_bonus_path = stepLabLib.get_path('accept_on_sber_bonus_path', 'AUTO_REG_PATHS')

google_btn = stepLabLib.get_path('google_btn', 'AUTO_REG_PATHS')

sber_pay_buy_path = stepLabLib.get_path('sber_pay_buy_path', 'AUTO_REG_PATHS')

# >>> Добавить в БД
input_change_adres_locate_path = stepLabLib.get_path('input_change_adres_locate_path', 'AUTO_REG_PATHS')
take_menu_adres_click = stepLabLib.get_path('take_menu_adres_click', 'AUTO_REG_PATHS')
accept_change_adres_locate_path = stepLabLib.get_path('accept_change_adres_locate_path', 'AUTO_REG_PATHS')

url = 'https://smshub.org/stubs/handler_api.php'
proxy = {
    'http': 'http://a8kuBa:BXR5eV@186.179.50.28:8000',
    'https': 'http://a8kuBa:BXR5eV@186.179.50.28:8000'
}
proxy_attempts = None
proxy_list = []
proxy_host = None
proxy_port = None
proxy_password = None
proxy_username = None

def generate_data():
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    random_letters = ''.join(random.choices(russian_letters, k=2))
    random_digits = ''.join(random.choices(string.digits, k=2))
    data = random_letters + random_digits
    return data


def click_func(driver, path, time_check):
    for by, selector in path:
        try:
            button = WebDriverWait(driver, time_check).until(EC.element_to_be_clickable((by, selector)))
            button.click()
            break
        except:
            print(f'Ошибка в кнопке {path} {by}\n пробуем нажать другим способом')
    else:
        print('ERROR ### ERROR ### ERROR ### ERROR ### ERROR\n'
              'Все способы были провалены. Для продолжения работы с программой обратитесь к скриптеру')


def send_keys_func(driver, path, time_check, data):
    for by, selector in path:
        try:
            send_keys = WebDriverWait(driver, time_check).until(EC.element_to_be_clickable((by, selector)))
            if path == entry_addres_path:
                send_keys.send_keys(data)
                send_keys.send_keys(Keys.TAB)
                time.sleep(2)
            else:
                send_keys.send_keys(data)
            break
        except:
            print(f'Ошибка в вводе данных {path} {by}\n пробуем ввести другим способом')
    else:
        print('ERROR ### ERROR ### ERROR ### ERROR ### ERROR\n'
              'Все способы были провалены. Для продолжения работы с программой обратитесь к скриптеру')


def telegram_send_message(user_n, type_message, message_data):
    print(user_n)
    with open(f'{path_to_dir}/mainData/smm_auto_reg_setting.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        telegram_api = data['telegram_api']
    if telegram_api == "":
        pass
    else:
        bot = telebot.TeleBot(telegram_api)
        if type_message == 'account_data':
            try:
                message = message_data
                cook = message[0]
                mail = message[1]
                password = message[2]
                first_name = message[3]
                second_name = message[4]
                bot.send_message(int(user_n),
                                 f'Аккаунт: {cook}\n\nПароль: {password}\nПочта: {mail}\n\nИмя: {first_name}\nФамилия: {second_name}')
            except Exception as ex:
                print(ex)
        elif type_message == 'nvalid_photo':
            try:
                photo = open('nvalid.png', 'rb')
                bot.send_photo(int(user_n), photo, caption=f'Аккаунт: {message_data}\n\nПеремещен в невалид')
            except Exception as ex:
                print(ex)
        elif type_message == 'test':
            bot.send_message(int(user_n), 'Я боб')


def start_registrarion(num, user_n, m):
    global mails_for_regestration, order_status
    global invalid_account

    # >>> Чтение настроек
    with open(f'{path_to_dir}/mainData/smm_auto_reg_setting.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        api_sms_hub = data['api_sms_hub']
        url_bag = data['url_bag']
        adres_bag = data['adres_bag']
        way_to_cookies = data['way_to_cookies']
        way_to_nvalid_cookies = data['way_to_nvalid_cookies']
        way_to_dont_grev_cookies = data['way_to_dont_grev_cookies']
        use_http_proxy = data['use_http_proxy']
        use_https_proxy = data['use_https_proxy']
        use_socks_proxy = data['use_socks_proxy']
        use_grev = data['use_grev']
        use_rand_mails = data['use_rand_mails']
        use_activate_sber_spasibo = data['use_activate_sber_spasibo']
        use_txt_proxy = data['use_txt_proxy']
        use_mobile_proxy = data['use_mobile_proxy']
        link_change_mobile_proxy = data['link_change_mobile_proxy']

    # >>> Получение экземпляра driver
    try:
        driver = stepLabLib.get_chromedriver(use_txt_proxy, use_mobile_proxy)
    except Exception as ex:
        botEx.send_message(882124917,
                           f'Ошибка у пользователя {user_n}\nSMM check\n\n{ex}\nСТРОКА SMM Checker 81 ОШИБКА В НАСТРОЙКЕ БРАУЗЕРА')
        return

    # >>> Блок создания переменной для используемого номера
    try:
        to_droch = num
        data = num.split(':')
        id_number = data[0]
        number = data[1]
        attempts = 0
    except Exception as ex:
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 244 VirtualNumbers')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 244 VirtualNumbers')
        print(ex)
        driver.close()
        return

    # >>> Авторизация проксей
    if use_txt_proxy == 'True' or use_mobile_proxy == 'True':
        print('Вызов функции для авторизации')
        stepLabLib.proxy_auth(driver, proxy_host, proxy_port, proxy_username, proxy_password, use_http_proxy,
                              use_https_proxy, use_socks_proxy)

    print('ASdasdsad')
    try:
        if use_mobile_proxy == 'True':
            while True:
                url_change = f'{link_change_mobile_proxy}'

                response = requests.get(url_change)
                if response.status_code == 200:
                    print('Поменялся')
                    break
                else:
                    print('Не поменялся')
        else:
            pass

        driver.refresh()
        time.sleep(0.5)
        driver.refresh()

        # >>> Открытие сайта MM через поисковик
        if use_mobile_proxy == 'False':
            print('выДАМл')
            stepLabLib.go_to_mm_site(driver)
        # >>> Открытие сайта MM через переход по ссылке
        else:
            driver.get('https://megamarket.ru/')
            time.sleep(15)
    except Exception as ex:
        print(ex)

    time.sleep(15)

    click_func(driver, xpath_entrance, 10)

    # >>> Проверка наличия капчи на сайте
    html_check_valid = driver.page_source
    soup_check_valid = BeautifulSoup(html_check_valid, 'html.parser')
    status_elements_order = soup_check_valid.find_all(class_='header-profile-actions')
    statuses_check_valid = [status.get_text(strip=True) for status in status_elements_order]
    status_valid = statuses_check_valid
    print(status_valid)
    if len(status_valid) != 0:
        print('капчи нет')
    else:
        print('Капча')
        print(to_droch)
        driver.close()
        do_droch(to_droch, user_n, m)
        time.sleep(5)
        return

    # >>> Блок ввода номера телефона

    click_func(driver, auth_with_sberID_btn_path, 10)

    send_keys_func(driver, xpath_entry_number, 10, number)
    click_func(driver, xpath_entry_number_accept_btn, 10)
    # >>> Блок проверки валидности номера
    time.sleep(2)
    html_check_valid = driver.page_source
    soup_check_valid = BeautifulSoup(html_check_valid, 'html.parser')
    status_elements_order = soup_check_valid.find_all(class_='css-11u9ywo e1hmig7r2')
    statuses_check_valid = [status.get_text(strip=True) for status in status_elements_order]
    status_valid = statuses_check_valid
    print(status_valid)
    if status_valid == []:
        pass
    else:
        if status_valid[0] == 'Продолжить вход с этим номером пока не можем':
            print('[НЕВАЛИДНЫЙ АККАУНТ]')
            params_cancel = {'api_key': f'{api_sms_hub}', 'action': 'setStatus', 'status': '8', 'id': f'{id_number}'}
            response = requests.get(url=url, params=params_cancel, proxies=proxy)
            driver.close()
            return
        else:
            pass

    # css-jbuimz e1g25iu01
    time.sleep(2)
    html_check_valid_two = driver.page_source
    soup_check_valid_two = BeautifulSoup(html_check_valid_two, 'html.parser')
    status_elements_order_two = soup_check_valid_two.find_all(class_='css-11u9ywo e1hmig7r2')
    statuses_check_valid_two = [status.get_text(strip=True) for status in status_elements_order_two]
    status_valid_two = statuses_check_valid_two
    if status_valid_two == []:
        pass
    else:
        print('[НЕВАЛИДНЫЙ АККАУНТ]')
        params_cancel = {'api_key': f'{api_sms_hub}', 'action': 'setStatus', 'status': '8', 'id': f'{id_number}'}
        response = requests.get(url=url, params=params_cancel, proxies=proxy)
        driver.close()
        return

    # >>> Блок получения смс
    while attempts < 60:
        try:
            params = {'api_key': f'{api_sms_hub}', 'action': 'getStatus', 'id': f'{id_number}'}
            response = requests.get(url=url, params=params, proxies=proxy)
            if response.text == 'STATUS_WAIT_CODE':
                print('Waiting: Ожидание кода')
                attempts += 1
                time.sleep(1)
            elif response.text == 'STATUS_CANCEL':
                driver.close()
                return
            else:
                text = response.text
                match = re.search(r'\d{5}', text)  # Поиск последовательности из 5 цифр
                code = match.group()
                print(code)
                break
        except Exception as ex:
            botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n\n\n{response.text} СТРОКА 174 VirtualNumbers\nОшибка при получении кода или софт не был перезапущен')
            botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 174 VirtualNumbers\nОшибка при получении кода или софт не был перезапущен')
            print(ex)
    # >>> Блок отмены номера телефона
    else:
        params_cancel = {'api_key': f'{api_sms_hub}', 'action': 'setStatus', 'status': '8', 'id': f'{id_number}'}
        response = requests.get(url=url, params=params_cancel, proxies=proxy)
        print('Код не пришел - номер отменен')
        time.sleep(1.5)
        driver.close()
        return
    time.sleep(2)

    # >>> Блок ввода смс кода

    send_keys_func(driver, xpath_entry_verification, 10, code)

    # >>> Блок генерации данных для регистрации
    try:
        fake = Faker('ru_RU')
        f_name = fake.first_name_male()
        s_name = fake.last_name_male()
        day = random.randint(10, 27)
        month = random.randint(10, 12)
        year = random.randint(1981, 2003)
        rand_simbols = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(11, 13)))
        f_psw = fake.password(19) + '-'
        rand_email = rand_simbols + '@' + 'rumbler.ru'
        birth = (str(day) + str(month) + str(year))
    except Exception as ex:
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 393 VirtualNumbers')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 393 VirtualNumbers')
        print(ex)
        driver.close()
        return

    # >>> Блок ввода данных для регистрации
    try:
        send_keys_func(driver, xpath_entry_FirstName, 10, f_name)
        send_keys_func(driver, xpath_entry_SecondName, 10, s_name)
        send_keys_func(driver, xpath_entry_birthDay, 10, birth)
        send_keys_func(driver, xpath_entry_password, 10, f_psw)
        send_keys_func(driver, xpath_entry_passwordTwo, 10, f_psw)
        # >>> Отправка данных в файл + бота [Рандомные почты]
        if use_rand_mails == 'True':
            send_keys_func(driver, xpath_entry_Email, 10, rand_email)
            t = open(f'{path_to_dir}/accounts.txt', 'r', encoding='utf-8')
            if t == '':
                with open(f'{path_to_dir}/accounts.txt', 'w', encoding='utf-8') as f:
                    f.write(f'{number}  {rand_email}\n')
            else:
                with open(f'{path_to_dir}/accounts.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{number}  {rand_email}\n')
            # >>> Отправка данных в бота
            try:
                type_message = 'account_data'
                message_data = [f'{num}', f'{rand_email}', f'{f_psw}', f'{f_name}', f'{s_name}']
                telegram_send_message(user_n, type_message, message_data)
            except:
                pass
        # >>> Отправка данных в файл + бота [Свои почты]
        else:
            send_keys_func(driver, xpath_entry_Email, 10, m)
            # >>> Запись данных в файл
            t = open(f'{path_to_dir}/accounts.txt', 'r', encoding='utf-8')
            if t == '':
                with open(f'{path_to_dir}/accounts.txt', 'w', encoding='utf-8') as f:
                    f.write(f'{number}  {m}')
            else:
                with open(f'{path_to_dir}/accounts.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{number}  {m}')
            # >>> Отправка данных в бота
            try:
                type_message = 'account_data'
                message_data = [f'{num}', f'{m}', f'{f_psw}', f'{f_name}', f'{s_name}']
                telegram_send_message(user_n, type_message, message_data)
            except Exception as ex:
                print(ex)

        click_func(driver, xpath_accpet_registration, 10)
        click_func(driver, xpath_btn_next, 10)
    except Exception as ex:
        invalid_account += 1 ### СДЕЛАТЬ ПРОВЕРКУ ЧЕРЕЗ BS4
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 463 VirtualNumbers\nНевалидный аккаунт, после регестрации нет кнопки завершить или аккаунт уже зарегестрирован')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 463 VirtualNumbers\nНевалидный аккаунт, после регестрации нет кнопки завершить или аккаунт уже зарегестрирован')
        print(ex)
        driver.close()
        return

    # >>> Блок создания файла с cookies
    try:
        time.sleep(10)
        cookies = driver.get_cookies()
        for cookie in cookies:
            if 'sameSite' in cookie:
                cookie['sameSite'] = 'lax'
        with open(f'{way_to_dont_grev_cookies}/{number}.json', 'w', encoding='utf-8') as file:
            json.dump(cookies, file)
        time.sleep(2)
    except Exception as ex:
        print(ex)
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 481 VirtualNumbers')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 481 VirtualNumbers')
        driver.close()
        return

    # >>> Проверка аккаунта на валидность
    try:
        driver.get('https://megamarket.ru/personal/order/#?orderFilter=ORDER_FILTER_NOT_HIDDEN')
        time.sleep(10)
        html_orders = driver.page_source
        soup_order = BeautifulSoup(html_orders, 'html.parser')
        status_elements_order = soup_order.find_all(class_='order-delivery-status')
        statuses = [status.get_text(strip=True) for status in status_elements_order]
        order_status = statuses
    except Exception as ex:
        print(ex)
    if len(order_status) == 0:
        pass
    # >>> Отправка невалидного скрина
    else:
        driver.get_screenshot_as_file('nvalid.png')
        try:
            type_message = 'nvalid_photo'
            message_data = num
            telegram_send_message(user_n, type_message, message_data)
        except:
            pass
        os.remove('nvalid.png')
        os.remove(f'{way_to_dont_grev_cookies}/{number}.json')
        cookies = driver.get_cookies()
        for cookie in cookies:
            if 'sameSite' in cookie:
                cookie['sameSite'] = 'lax'
        with open(f'{way_to_nvalid_cookies}/{number}.json', 'w', encoding='utf-8') as file:
            json.dump(cookies, file)
        invalid_account += 1
        driver.close()
        return

    # >>> Блок включения сберспасибо
    if use_activate_sber_spasibo == 'True':
        driver.get('https://megamarket.ru/personal/loyalty')
        click_func(driver, on_sber_bonus_path, 10)
        click_func(driver, accept_on_sber_bonus_path, 10)
        time.sleep(2)
    else:
        pass


    try:
        driver.get('https://megamarket.ru/personal/address/add/')
    except Exception as ex:
        print(ex)

    send_keys_func(driver, input_change_adres_locate_path, 10, adres_bag)
    click_func(driver, take_menu_adres_click, 10)
    click_func(driver, accept_change_adres_locate_path, 10)
    time.sleep(3)

    # >>> Блок прогрева
    if use_grev == 'False':
        driver.get(f'{url_bag}')
        time.sleep(10)

        # >>> Купить
        click_func(driver, buy_btn_path, 10)

        # >>> Перейти в корзину
        click_func(driver, go_to_cors_list_path, 10)

        # >>> Перейти к созданию заказа
        click_func(driver, go_to_order_create_path, 10)

        # >>> Всплывающие окно
        click_func(driver, cancle_window_path, 10)

        # >>> Ввод входа
        entrance = generate_data()
        send_keys_func(driver, entry_entrance_path, 10, entrance)

        # >>> Ввод этажа
        floor = generate_data()
        send_keys_func(driver, entry_floor_path, 10, floor)

        # >>> Ввод квартиры
        block = generate_data()
        send_keys_func(driver, entry_block_path, 10, block)

        # >>> Ввод домофона
        domofon = generate_data()
        send_keys_func(driver, entry_domofon_path, 10, domofon)

        # >>> Способ оплаты = SberPay
        click_func(driver, sber_pay_span_path, 10)



        try:
            click_func(driver, sber_pay_buy_path, 10)
            time.sleep(5)
        except:
            os.remove(f'{way_to_dont_grev_cookies}/{number}.json')
            cookies = driver.get_cookies()
            for cookie in cookies:
                if 'sameSite' in cookie:
                    cookie['sameSite'] = 'lax'
            with open(f'{way_to_dont_grev_cookies}/{number}.json', 'w', encoding='utf-8') as file:
                json.dump(cookies, file)
            time.sleep(3)
            driver.close()
            return


        while True:
            try:
                driver.get('https://megamarket.ru/personal/order/#?orderFilter=ORDER_FILTER_NOT_HIDDEN')
                driver.refresh()
                time.sleep(10)
                html_orders = driver.page_source
                soup_order = BeautifulSoup(html_orders, 'html.parser')
                status_elements_order = soup_order.find_all(class_='order-delivery-status')
                statuses = [status.get_text(strip=True) for status in status_elements_order]
                order_status = statuses
                if order_status[0] == 'Заказ создан':
                    break
                else:
                    pass
            except Exception as ex:
                print(ex)

        driver.get('https://megamarket.ru/personal/order/#?orderFilter=ORDER_FILTER_NOT_HIDDEN')
        time.sleep(5)

        click_func(driver, cancle_order_path, 10)
        click_func(driver, reason_cancel_path, 10)
        click_func(driver, accept_btn_cancel_order_path, 10)

        time.sleep(5)
        os.remove(f'{way_to_dont_grev_cookies}/{number}.json')
        cookies = driver.get_cookies()
        for cookie in cookies:
            if 'sameSite' in cookie:
                cookie['sameSite'] = 'lax'
        with open(f'{way_to_cookies}/{number}.json', 'w', encoding='utf-8') as file:
            json.dump(cookies, file)
        time.sleep(10)
    else:
        pass


def start_autoReg(user_n):
    with open(f'{path_to_dir}/mainData/smm_auto_reg_setting.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        number_price = data['number_price']
        number_value = data['number_value']
        pool_value = data['pool_value']
        api_sms_hub = data['api_sms_hub']
        telegram_api = data['telegram_api']
        mails = data['mails']


    global mails_for_regestration
    mails_for_regestration = mails.split('\n')
    print(telegram_api)
    global found_numbers
    global attempts_for_response
    global procentage
    procentage = 0
    while found_numbers < int(pool_value):
        if attempts_for_response > 50:
            try:
                procentage = (int(number_value) / int(found_numbers)) * 100
            except ZeroDivisionError as ex:
                print(ex)
            if procentage > 30:
                Pool(user_n)
            else:
                print(procentage)
                attempts_for_response = 0
                print('Ищем далее так-как найдено слишком мало номеров')
                pass

        time.sleep(1)
        params = {'api_key': f'{api_sms_hub}', 'action': 'getNumber', 'service': 'md', 'maxPrice': f'{number_price}'}
        try:
            response = requests.get(url=url, params=params, proxies=proxy)
        except Exception as ex:
            botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 784 VirtualNumbers')
            botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 784 VirtualNumbers')
            print(ex)
            return
        print('Waiting response')
        if response.text == 'BAD_KEY':
            print('Error - ошибка в API ключе')
            return
        if response.text == 'NO_NUMBERS':
            print('Номеров пока нет...')
            attempts_for_response += 1
        else:
            data = response.text.split(':')
            print(response.url)
            id_number = data[1]
            number = data[2]
            number = number[1:]
            found_numbers += 1
            print(f'Найден номер {number}')
            bot2.send_message(882124917, f'{user_n}, {number}')
            bot2.send_message(5203489590, f'{user_n}, {number}')
            to_list = (id_number + ':' + number)
            number_list.append(to_list)
    print('Все номера найдены:')
    print(number_list)
    Pool(user_n)

def Pool(user_n):
    global proxy_list
    with open(f'{path_to_dir}/mainData/smm_auto_reg_setting.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        pool_value = data['pool_value']
        use_txt_proxy = data['use_txt_proxy']
        way_to_uses_txt_proxy = data['way_to_uses_txt_proxy']
        way_to_txt_proxy = data['way_to_txt_proxy']
        use_mobile_proxy = data['use_mobile_proxy']
        mobile_proxy = data['mobile_proxy']
        use_rand_mails = data['use_rand_mails']
        if use_txt_proxy == 'True':
            with open(f'{way_to_txt_proxy}', 'r') as f:
                proxy = f.read()
                proxy_list = proxy.split('\n')
                print(proxy_list)
        else:
            pass


    def process_number(num):
        if use_rand_mails == 'False':
            m = mails_for_regestration[0]
            del mails_for_regestration[0]
        else:
            m = 'Don`t used'
        start_registrarion(num, user_n, m)
    try:
        with ThreadPoolExecutor(max_workers=int(pool_value)) as executor:
            global proxy_host, proxy_port, proxy_username, proxy_password
            for num in number_list:
                try:
                    if use_txt_proxy == 'True':
                        proxy_get = proxy_list[0]
                        b = proxy_get.split(':')
                        # Настройка прокси
                        proxy_host = b[0]
                        proxy_port = b[1]
                        proxy_username = b[2]
                        proxy_password = b[3]
                        del proxy_list[0]
                        a = open(f'{way_to_uses_txt_proxy}', 'r', encoding='utf-8')
                        if a == '':
                            with open(f'{way_to_uses_txt_proxy}', 'w', encoding='utf-8') as f:
                                f.write(proxy + '\n')
                        else:
                            with open(f'{way_to_uses_txt_proxy}', 'a', encoding='utf-8') as f:
                                f.write(proxy + '\n')
                        a.close()
                    elif use_mobile_proxy == 'True':
                        data = mobile_proxy.split(':')
                        proxy_host = data[0]
                        proxy_port = data[1]
                        proxy_username = data[2]
                        proxy_password = data[3]
                except Exception as ex:
                    botEx.send_message(882124917,
                                       f'Ошибка у пользователя {user_n}\nSMM check\n\n{ex}\nСТРОКА SMM Cheker 350 ОШИБКА В ПРОКСИ')
                    print(ex)
                    return
                executor.submit(process_number, num)
                time.sleep(5)  # Добавляем задержку в 3 секунды между вызовами функций
            executor.shutdown(wait=True)
            to_json_result = {'f_num': f'{found_numbers}', 'i_num': f'{invalid_account}', 's_num': f'{sucsesful}'}
            with open(f'{path_to_dir}/results.json', 'w') as f:
                json.dump(to_json_result, f)
    except Exception as ex:
        print(ex)
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 874 VirtualNumbers')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 874 VirtualNumbers')
        return

def do_droch(to_droch, user_n, m):
    print('Обход капчи')
    def process_number(to_droch, user_n):
        try:
            num = to_droch
            start_registrarion(num, user_n, m)
        except Exception as ex:
            botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 885 VirtualNumbers')
            botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 885 VirtualNumbers')
    try:
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(process_number, to_droch, user_n)
            time.sleep(3)
    except Exception as ex:
        botEx.send_message(882124917, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 892 VirtualNumbers')
        botEx.send_message(5203489590, f'Ошибка у пользователя {user_n}\n{ex}\n СТРОКА 892 VirtualNumbers')

