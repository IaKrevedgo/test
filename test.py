import os
import time
import sys
import getpass
import configparser
import passfile as logpass #тянем пароли из файла и не забываем, что хотели это все шифрануть еще
import mes as mes #подключаем фалй с сообщениями


#имена подключаемых файлов
cfile = 'config.ini'
lfile = 'my.log'
mfile = 'mes.py'

#работаем с дополнительными файлами
config = configparser.ConfigParser()

#глобальные переменные

def Log (mtype,id):
    logmesE = mes.logmesE   #алармы
    logmesI = mes.logmesI   #информационные
    datetime  = time.localtime()
    time_str = time.strftime("[%m/%d/%Y, %H:%M:%S]", datetime)

    if not os.path.exists(lfile):
        with open(lfile, 'w') as file:
            file.write('[MAIN LOG]')
            file.close()
    else:       
        try:
            emes = '\n[A]' + time_str + ' ' + str(logmesE[id])
            imes = '\n[I]' + time_str + ' ' + str(logmesI[id])
            wmes = '\n[W]' + time_str + ' ' + str(logmesI[id])
            if mtype == 'e':
                with open(lfile, 'a') as f:
                    f.write(emes)
            elif mtype == 'i':
                with open(lfile, 'a') as f:
                    f.write(imes)
            elif mtype == 'w':
                with open(lfile, 'a') as f:
                    f.write(wmes)
        except KeyError:
            pass
        

def useConfig (path):
    global maxerr 
    global t2
    if not os.path.exists(cfile): #если файла нет создаем новый
        Log ('e','100') 
        with open(path, "a") as f:
            config.write(f)
            Log ('0','100')
        config.add_section('block')
        config.set("block", "maxerr", "3")
        config.set("block", "blocktime", "10")
        
    elif os.path.exists(cfile):
        try:
            #тянем из конфига
            config.read(path, encoding='utf-8-sig')
            maxerr = int(config.get('block','maxerr')) #Количество неудачных попыток до блокировки
            t2 = int(config.get('block','blocktime')) #время блокировки
        except KeyError:
            pass

useConfig (cfile)
exit = 0
Log ('i','1')
while exit == 0:

    #init
    LogSys = 0
    err=0
    t1=0

    while LogSys == 0:
        if err < maxerr:
            os.system('cls')
            print ('<----Вход в систему---->','\n')
            login = input ('Введите имя (прописные русские буквы)> ')
            password = getpass.getpass ('Введите пароль (пароль не отображается)> ')
            
            try:
                if password == logpass.logpas[login]:
                    print()
                    print('Вход разрешен')
                    time.sleep(1)
                    LogSys = 1
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
    while LogSys == 1:

        os.system('cls')
        print('<----Меню программы---->','\n')
        print('1.Запустить приложение')
        print('2.Настройки приложения')
        print('3.Выход из системы')
        print('4.Закрыть программу', '\n\n')
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
                LogSys = 0
                
            elif selmenu == '4': #закрыть программу
                os.system('cls')
                print('Осуществлен выход из программы')
                time.sleep(2)
                os.abort()
        except (selmenu < '1' ) and (selmenu > '4' ):
            pass






    
