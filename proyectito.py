import subprocess

from telegram.ext import Updater, CommandHandler
# from piled import LED


def hello(update, context):
    update.message.reply_text("Bienvenido a Proyectito")


def echo(update, context):
    if len(context.args) > 0:
        mensaje = " ".join(context.args)
        update.message.reply_text(mensaje + "🤔")
        print(mensaje)
    else:
        update.message.reply_text("Escribe algo")


def led(update, context):
    pass


def check(update, context):
    salida = subprocess.check_output(["/home/pi/scripts/takepicture"])
    ruta_photo = salida.decode().strip()
    photo = open(ruta_photo, 'rb')
    update.message.reply_photo(photo)


with open("/home/pi/mechi/clave_token.txt") as token_file:
    TOKEN_TL = token_file.read().strip()
    print(TOKEN_TL)

updater = Updater(TOKEN_TL)

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('echo', echo))
updater.dispatcher.add_handler(CommandHandler('led', led))
updater.dispatcher.add_handler(CommandHandler('check', check))

print("Iniciando bot")
updater.start_polling()
updater.idle()
print("terminando el proceso")
