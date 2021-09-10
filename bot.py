import tweepy
import time

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

key = 'KEY'
secret = 'SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# Actualiza el estado de tu twitter añadiendo el tweet con las palabras que se encuentran entre paréntesis
#   api.update_status('Prueba')

#Imprime el último tweet escrito

#   tweets = api.mentions_timeline()
#   print(tweets[0].text)

#Recorre los tweets de la cuenta e imprime sus tweets así como el ID del tweet

#   for tweet in tweets:
#   print(str(tweet.id) + ' - ' + tweet.text)

#Recorre los tweets de la cuenta e imprime sus tweets así como el ID del tweet si contiene la palabra prueba

#   for tweet in tweets:
#       if 'prueba' in tweet.text.lower():
#           print(str(tweet.id) + ' - ' + tweet.text)

#Obtener el ID de su screen name
    
    # El @ del usuario
    #   screen_name = "fernirepullo"

    # Encontrar al usuario
    #   user = api.get_user(screen_name)

    # Encontrar el ID
    #   ID = user.id_str

    # Mostrar el ID
    #   print("El ID es: " + ID)

screen_name = 'USER'

user = api.get_user(screen_name)

print(user)



# Recuperar los MD's

#   md = api.list_direct_messages
#   print (md)

# Para saber el lenguaje de un tweet se usa lo siguiente:

# ID del tweet
#   id = 
# Devolver el tweet
#   status = api.get_status(id)
# Devolver el lenguaje
#   lang = status.lang

# Para saber la localización de un usuario

# #ID del usuario
# id = USERID

# #Devolver el usuario
# user = api.get_user(id)

# #Devolver la localización
# location = user.location

# print("La localización del usuario es: " + location)

# Para que el bot responda a tuits nuevos o que no ha respondido, hay que separar los tuits vistos de los tuits nuevos
# Para ello, debemos de guardar el ID del último tuit contestado
# Se guardarán en un documento de texto de nombre "last_seen.txt"

# Crear métodos para escribir en el fichero de texto -- NO FUNCIONA --

# FILE_NAME = 'last_seen.txt'

# def read_last_seen(FILE_NAME):
#     file_read = open(FILE_NAME, 'r')
#     last_seen_id = int(file_read.read().strip())
#     file_read.close()
#     return last_seen_id

# def store_last_seen(FILE_NAME, last_seen_id):
#     file_write = open(FILE_NAME, 'w')
#     file_write.write(str(last_seen_id))
#     file_write.close()
#     return

# # Cargar timeline después de pasarle el ID del último tuit
# tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')

# #bucle que permitirá leer el contenido total del tuit, al tener tweet_mode = 'extended'
# for tweet in reversed(tweets):
#     if '#prueba' in tweet.full_text.lower():
#         print(str(tweet.id) + ' - ' + tweet.full_text)