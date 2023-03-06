from pyrogram import Client

api_id = 28518143
api_hash = 'ad381fd66d11c000b1cc5b984237e059'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message(384749611, 'Привет, это я!')
app.stop()
