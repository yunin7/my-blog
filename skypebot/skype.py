#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
import Skype4Py
from http import Http
from datetime import datetime

# Две строки, которые избавляют от ошибки декодирования кириллицы
# ASCII decoding error: ordinal not in range(128)
# Хотя локаль по-умолчанию в системе стоит en_US.UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

skype = Skype4Py.Skype()

# Ключевое слово
string_key = unicode('enru','utf-8')
string_key2 = unicode('ruen','utf-8')  

def translate(msg, langpair):
    print msg
    #import pdb; pdb.set_trace()
    http = Http('ajax.googleapis.com', 443)
    params = {'v': '1.0', 'q': msg, 'langpair': langpair}
    #if http.request('/ajax/services/language/translate?v=1.0&q=%s&langpair=%s' % (msg, langpair)):
    if http.request('/ajax/services/language/translate', 'GET', params):
        response = http.parse()
	print response
        if response.get('responseStatus', None) == 200:
	    result = response['responseData']['translatedText']
            print 'TRANSLATION:', result
	    return result

# Callback на аттач к скайпу
def OnAttach(status):
    print "API Attachment status: %s" % skype.Convert.AttachmentStatusToText(status)
    attached = False
    # Пытаемся подключиться
    if status == Skype4Py.apiAttachAvailable:
        while not attached:
            try:
                # Если скрипт внесен в Public API allowed programs - коннектимся
                skype.Attach()
                attached = True
            # Если нет - ждем, пока внесут, а пока идем лесом
            except:
                pass

# Callback на смену статуса
#def OnUserStatus(status):
#    print "Current status: %s" % status

# При нотисе
#def OnNotify(var):
#    print "OnNotify: %s" % var

def OnMessageStatus(chat, status):
# Получили? Получили!
# есть ещё статус 'READ' - может быть понадобится потом.
    if status in ('SENT',):
        token = chat.Body[:4]
	msg = chat.Body[4:]
        msg='hello'
        langpair = 'en|ru'
        if token == 'enru':
	  langpair = 'en|ru'
        if token == 'ruen':
	  langpair = 'ru|en'
	result = translate(msg, langpair)
        chat.Chat.SendMessage(result)
    else:
        print status


# Регистрируем слушателей
skype.OnAttachmentStatus = OnAttach
#skype.OnUserStatus = OnUserStatus
#skype.OnNotify = OnNotify
skype.OnMessageStatus = OnMessageStatus

print 'Connecting to skype..'
# Подключаемся
skype.Attach(Wait=False)
profile = skype.CurrentUserProfile

while True:
    # Каждые 5 секунд проверяем, не изменился ли трек
    time.sleep(5)
    pass
