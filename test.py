import os
import time
import sys
import getpass
import hashlib
import passfile as logpass #не забываем, что хотели это все шифрануть еще
import configparser


#тянем из конфига
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
maxerr = int(config.get('Setup','maxerr')) #Количество неудачных попыток до блокировки
t2 = int(config.get('Setup','blocktime')) #время блокировки

exit =0
while exit == 0:

    #init
    login = 0
    err=0
    t1=0

    while login == 0:
        if err < maxerr:
            os.system('cls')
            print ('<----Вход в систему---->','\n')
            log = input ('Введите имя (прописные русские буквы)> ')
            pas = getpass.getpass ('Введите пароль (пароль не отображается)> ')
            
            try:
                if pas == logpass.logpas[log]:
                    print()
                    print('Вход разрешен')
                    time.sleep(1)
                    login = 1
                else:
                    print()
                    print('Неверный логин или пароль ')
                    time.sleep(1)
                    err+=1
            except KeyError:
                print()
                print('Неверный логин или пароль') 
                time.sleep(2)
                err+=1

        else:
            print()
            print('Вы превысили максимальное число неудачных попыток')
            print('Вход будет заблокирован на ',t2,' секунд')
            time.sleep(3)
            for t1 in range(t2):
                os.system('cls')
                print('Оставшееся время до разблокировки: ', t2 - t1)
                time.sleep(1)
                t1+=1
                if t1 >= t2:
                    err = 0

    selmenu = 0
    while login == 1:

        os.system('cls')
        print('<----Меню программы---->','\n')
        print('1.Запустить приложение')
        print('2.Настройки приложения')
        print('3.Выход из системы')
        print('4.Закрыть программу', sep='\n\n')
        selmenu = input('Ввыберите пункт меню> ')
        try:
            if   selmenu == '1': #основная программа
                pass
            elif selmenu == '2': #настройки
                pass
            elif selmenu == '3': #выход из системы
                os.system('cls')
                print('Осуществлен выход из системы')
                time.sleep(2)
                login = 0
                
            elif selmenu == '4': #закрыть программу
                os.system('cls')
                print('Осуществлен выход из программы')
                time.sleep(2)
                os.abort()
        except (selmenu < '1' ) and (selmenu > '4' ):
            pass






    
