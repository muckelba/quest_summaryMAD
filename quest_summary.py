import json
import requests
import time
import locale

def readConfig(type):
    arr = []
    parse = False
    with open('quest_config.txt') as f:
        arr = f.readlines()
    arr = [x.strip() for x in arr]
    resp = []
    for x in arr:
        if '#' in x:
            if type in x:
                parse = True
                continue
            else:
                parse = False
        if parse and x != '':
            resp.append(x)
    return resp

token = readConfig('TOKEN')
chat_id = readConfig('CHATID')
mapurl = readConfig('MAPURL')
madminurl = readConfig('MADMINURL')
localeSetting = readConfig('LOCALE')
pokemonIds = readConfig('POKEMON')
rarecandy = readConfig('RARECANDY')
stardust = readConfig('STARDUST')
user = readConfig('USER')
passw = readConfig('PASS')

text_file = open('text.txt', 'r', encoding='utf-8')
text = text_file.read()

candyList = []
starList = []
pokeList = []

for k in rarecandy:
    candyList.append([])
for k in stardust:
    starList.append([])
for k in pokemonIds:
    pokeList.append(False)

if user != "":
    json_input = requests.get(madminurl[0] + '/get_quests', auth=(user[0], passw[0]))
else:
    json_input = requests.get(madminurl[0] + '/get_quests')

data = json_input.json()

link = ''
for d in data:
    if d['quest_reward_type'] == "Item":
        if d['item_type'] == "Rare Candy":
            if str(d['item_amount']) in rarecandy:
                link = '[' + d['name'] + '](' + mapurl[0] + '/?lat=' + str(d['latitude']) + str('%26lon=') + str(d['longitude']) + '%26zoom=16)\n'
                candyList[rarecandy.index(d['item_amount'])].append(link)
    elif d['quest_reward_type'] == 'Stardust':
        if str(d['item_amount']) in stardust:
            link = '[' + d['name'] + '](' + mapurl[0] + '/?lat=' + str(d['latitude']) + str('%26lon=') + str(d['longitude']) + '%26zoom=16)\n'
            starList[stardust.index(d['item_amount'])].append(link)
    elif d['quest_reward_type'] == 'Pokemon':
        if str(d['pokemon_id']) in pokemonIds:
            link = '[' + d['name'] + '](' + mapurl[0] + '/?lat=' + str(d['latitude']) + str('%26lon=') + str(d['longitude']) + '%26zoom=16)\n' + '$' + d['pokemon_id'] + '$'
            text = text.replace('$' + d['pokemon_id'] + '$', link)
            pokeList[pokemonIds.index(d['pokemon_id'])] = True

starstring = ''
candystring = ''

for i in range(0, len(stardust)):
    if len(starList[i]) == 0:
        continue
    starstring += '\n🌟 ' + stardust[i] + ' *Stardust:*\n'
    for k in starList[i]:
        starstring += k
for i in range(0, len(rarecandy)):
    if len(candyList[i]) == 0:
        continue
    candystring += '\n🍬 ' + rarecandy[i] + ' *Rare Candies:*\n'
    for k in candyList[i]:
        candystring += k
for i in range(0, len(pokemonIds)):

    if pokeList[i]:
        text = text.replace('$' + pokemonIds[i] + '$', '')
        continue
    text = text.replace('$' + pokemonIds[i] + '$', '_Was not found today._\n')

text = text.replace('$rarecandy$', candystring)
text = text.replace('$stardust$', starstring)
text = text.replace('$amount$', str(len(data)))
locale.setlocale(locale.LC_TIME, localeSetting[0])
text = text.replace('$date', time.strftime("%A, the %e.%m.%Y"))

def bot_sendtext(bot_message):
    ### Send text message
    send_text = 'https://api.telegram.org/bot' + token[0] + '/sendMessage?chat_id=' + chat_id[0] + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)

bot_sendtext(text)