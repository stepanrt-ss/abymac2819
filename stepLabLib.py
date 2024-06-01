"""Библиотека работы с ChromeDriver | Develop by stepanrt_ss """
import json
import os
import pickle
import sys
import time

import ua_generator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from config import con
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


path_to_dir = os.path.dirname(sys.executable)


def go_to_mm_site(driver):
    google_link_for_mm = 'https://www.google.com/search?q=%D0%BC%D0%B5%D0%B3%D0%B0%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82&oq=%D0%BC%D0%B5%D0%B3%D0%B0%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDI5NDdqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8'
    print('выДАМл2222222222')
    driver.get('https://www.google.ru/')
    driver.set_window_size(1920, 1080)
    # >>> Подтверждение cookies в google.com

    try:
        tring = "//div[text()='Accept all']"
        trs = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, tring)))
        trs.click()
    except:
        pass

    # >>> Нажатие на кнопку мне повезет
    click_func(driver, google_btn, 10)
    time.sleep(1)
    driver.get(google_link_for_mm)

    # >>> Подтверждение cookies в google.com
    try:
        tring = "//div[text()='Accept all']"
        trs = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, tring)))
        trs.click()
    except:
        pass
    
    try:
        dont = "//div[text()='Не сейчас']"
        clasd = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, dont)))
        clasd.click()
    except:
        pass

    # >>> Переход на мм
    path = "//*[contains(text(), 'Мегамаркет')]"
    elements = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, path)))
    elements.click()
    time.sleep(15)


def proxy_auth(driver, proxy_host, proxy_port, proxy_username, proxy_password, use_http_proxy, use_https_proxy, use_socks_proxy):
    print(proxy_host)
    print(proxy_port)
    print(proxy_password)
    print(proxy_username)
    try:
        print('Тут')
        driver.get('chrome-extension://padekgcemlokbadohgkifijomclgjgif/options.html#!/profile/proxy')
        print('Там')
        tabs = driver.window_handles
        print(tabs)
        driver.switch_to.window(tabs[-1])
        driver.set_window_size(1920, 1080)
        for by, selector in skip_guide_proxy_path:
            try:
                skip_guide_proxy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                skip_guide_proxy.click()
                break
            except:
                pass

        if use_http_proxy == 'True':
            pass
        elif use_https_proxy == 'True':
            for by, selector in take_protokol_path:
                try:
                    take_protokol = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                    take_protokol.click()
                    break
                except:
                    pass

            for by, selector in take_protokol_https_path:
                try:
                    take_protokol_https = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                    take_protokol_https.click()
                    break
                except:
                    pass
        elif use_socks_proxy == 'True':
            for by, selector in take_protokol_path:
                try:
                    take_protokol = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                    take_protokol.click()
                    break
                except:
                    pass

            for by, selector in take_protokol_socks_path:
                try:
                    take_protokol_socks = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                    take_protokol_socks.click()
                    break
                except:
                    pass

        for by, selector in proxy_host_path:
            try:
                input_proxy_host = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                input_proxy_host.clear()
                input_proxy_host.send_keys(f'{proxy_host}')
                break
            except:
                pass

        for by, selector in proxy_port_path:
            try:
                input_proxy_port = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                input_proxy_port.clear()
                input_proxy_port.send_keys(f'{proxy_port}')
                break
            except:
                pass

        for by, selector in open_inputs_data_auth_path:
            try:
                open_inputs_data_auth = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                open_inputs_data_auth.click()
                break
            except:
                pass

        for by, selector in proxy_user_name_path:
            try:
                input_proxy_user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                input_proxy_user_name.send_keys(f'{proxy_username}')
                break
            except:
                pass
        print('time sleep')

        for by, selector in proxy_password_path:
            try:
                input_proxy_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                input_proxy_password.send_keys(f'{proxy_password}')
                break
            except:
                pass

        for by, selector in save_changes_path:
            try:
                save_changes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                save_changes.click()
                break
            except:
                pass

        for by, selector in proxy_accept_btn_path:
            try:
                proxy_accept_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                proxy_accept_btn.click()
                break
            except:
                pass
        time.sleep(2)
        driver.get('chrome-extension://padekgcemlokbadohgkifijomclgjgif/popup/index.html#')

        for by, selector in active_proxy_path:
            try:
                active_proxy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, selector)))
                active_proxy.click()
                break
            except:
                pass
        time.sleep(0.5)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[0])
        driver.get('https://megamarket.ru/')
    except Exception as ex:
        print(ex)


def get_chromedriver(use_txt_proxy, use_mobile_proxy):
    options = webdriver.ChromeOptions()
    ua = ua_generator.generate(device='desktop', browser='chrome')
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_argument(f'user-agent={ua}')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-offer-upload-credit-cards")
    print(ua)
    options.add_experimental_option("prefs", prefs)
    options.page_load_strategy = 'eager'
    if use_txt_proxy == 'True' or use_mobile_proxy == 'True':
        options.add_extension(f'{path_to_dir}/prx.crx')
        print('asd')
    else:
        pass
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver
# 'chrome-extension://padekgcemlokbadohgkifijomclgjgif/popup/index.html#' Вкелючаить

def get_path(name_path, data_base):
    with con.cursor() as cursor:
        command_for_db = f'SELECT * FROM {data_base}'
        cursor.execute(command_for_db)
        data_sql = cursor.fetchall()
        for data in data_sql:
            if data['name_path'] == str(name_path):
                if data['priority'] == 'xpath':
                    path = [
                        (By.XPATH, f"{data['xpath_value']}"),
                        (By.CSS_SELECTOR, f"{data['css_value']}"),
                        (By.CLASS_NAME, f"{data['calss_value']}")
                    ]
                    return path
                elif data['priority'] == 'css':
                    path = [
                        (By.CSS_SELECTOR, f"{data['css_value']}"),
                        (By.XPATH, f"{data['xpath_value']}"),
                        (By.CLASS_NAME, f"{data['calss_value']}")
                    ]
                    return path
                elif data['priority'] == 'class':
                    path = [
                        (By.CLASS_NAME, f"{data['calss_value']}"),
                        (By.XPATH, f"{data['xpath_value']}"),
                        (By.CSS_SELECTOR, f"{data['css_value']}")
                    ]
                    return path


def converter_cookies(cookies_way, cook_name):
    # Чтение данных из файла и преобразование в JSON
    with open(f'{cookies_way}/{cook_name}', 'r') as file:
        data = file.read()
        json_data = json.loads(data)

    os.remove(f'{cookies_way}/{cook_name}')
    load_txt_cook = cook_name.split('.')
    name_txt_cook = load_txt_cook[0]

    # Запись данных в JSON-файл
    with open(f'{cookies_way}/{name_txt_cook}.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    cook_name = f'{name_txt_cook}.json'
    return cook_name


def load_cookies(driver, use_sber_id_cookies, cook_name, cookies_way):
    cookies_data = None
    # >>> Загрузка JSON куков в браузер
    try:
        print('Выгрузка')
        try:
            with open(f'{cookies_way}/{cook_name}', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
        except json.JSONDecodeError as ex:
            print('Это гологин епта')
            if str(ex) == 'Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 column 1 (char 0)':
                with open(f'{cookies_way}/{cook_name}', 'r', encoding='utf-8-sig') as f:
                    cookies = json.load(f)

        # >>> Меняем Lax
        for cookie in cookies:
            if 'sameSite' in cookie:
                cookie['sameSite'] = 'Lax'

        # >>> Вытаскиваем токены
        if use_sber_id_cookies == 'True':
            id_user = None
            for cookie in cookies:
                if cookie.get('name') == 'id_user':
                    id_user = cookie
                    cookies_data = id_user
                    break
        else:
            ecom_token = None
            for cookie in cookies:
                if cookie.get('name') == 'ecom_token':
                    ecom_token = cookie
                    cookies_data = ecom_token
                    break
        print(cookies_data)

        with open(f'{cook_name}.pkl', 'wb') as f:
            pickle.dump(cookies_data, f)

        with open(f'{cook_name}.pkl', 'rb') as f:
            cookies = pickle.load(f)

        driver.add_cookie(cookies)
        os.remove(f'{cook_name}.pkl')

        print('Выгрузка закончилась')
    except Exception as ex:
        print(ex)


def move_cookies(driver, operation_type, way_to_dir):
    pass


def click_func(driver, path, time_wait):
    for by, selector in path:
        try:
            button = WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((by, selector)))
            button.click()
            break
        except:
            print(f'Ошибка в кнопке {path} {by}\nПробуем нажать другим способом')
    else:
        print('ERROR ### ERROR ### ERROR ### ERROR ### ERROR\n'
              'Все способы были провалены. Для продолжения работы с программой обратитесь к скриптеру')


def send_keys(driver, path, time_wait, data_send):
    pass


def bs4_checker(driver, path):
    pass


def generate_data():
    pass


def start_report_telegram(type_report):
    pass


def ex_report_telegram(user_n, ex):
    pass


def send_data_telegram(user_n, type_message, data_message):
    pass

take_protokol_socks_path = get_path('take_protokol_socks_path', 'stepLabLib_paths')
take_protokol_https_path = get_path('take_protokol_https_path', 'stepLabLib_paths')
take_protokol_path = get_path('take_protokol_path', 'stepLabLib_paths')
skip_guide_proxy_path = get_path('skip_guide_proxy_path', 'stepLabLib_paths')
active_proxy_path = get_path('active_proxy_path', 'stepLabLib_paths')
save_changes_path = get_path('save_changes_path', 'stepLabLib_paths')
open_inputs_data_auth_path = get_path('open_inputs_data_auth_path', 'stepLabLib_paths')
proxy_user_name_path = get_path('proxy_user_name_path', 'stepLabLib_paths')
proxy_password_path = get_path('proxy_password_path', 'stepLabLib_paths')
proxy_port_path = get_path('proxy_port_path', 'stepLabLib_paths')
proxy_host_path = get_path('proxy_host_path', 'stepLabLib_paths')
proxy_accept_btn_path = get_path('proxy_accept_btn_path', 'stepLabLib_paths')
google_btn = get_path('google_btn', 'stepLabLib_paths')












