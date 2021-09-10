import tweepy
import time

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

key = 'KEY'
secret = 'SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# Se almacena el ID de un tweet
# Cuando se menciona a la cuenta, responde en un nuevo tweet a parte.

FILE_NAME = 'last_seen.txt'


def devolver_last_seen_id(file_name):
    leerFichero = open(file_name, 'r')
    last_seen_id = int(leerFichero.read().strip())
    leerFichero.close()
    return last_seen_id


def guardar_last_seen_id(last_seen_id, file_name):
    escribirFichero = open(file_name, 'w')
    escribirFichero.write(str(last_seen_id))
    escribirFichero.close()
    return


def respuesta():
    last_seen_id = devolver_last_seen_id(FILE_NAME)
    mention = api.mentions_timeline(since_id=last_seen_id)

    for mention in reversed(mention):
        print(str(mention.id) + ' - ' + mention.text)
        last_seen_id = mention.id
        guardar_last_seen_id(last_seen_id, FILE_NAME)
        print('Respondiendo al tweet -> ' + str(mention.id) + 'escrito por: @' + mention.user.screen_name)
        api.update_status('@' + mention.user.screen_name + ' ' + 'Tuit de respuesta ',
                          in_reply_to_status_str=devolver_last_seen_id(FILE_NAME), auto_populate_reply_metadata=True)
        print('Mensaje respondido a -> @ ' + mention.user.screen_name)


print('Bot Started')

while True:
    print('Esperando a tuits')
    respuesta()
    time.sleep(10)
