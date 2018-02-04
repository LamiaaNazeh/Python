import webbrowser
import random

ran = ['http://gmail.com' , 'http://google.com' , 'http://yahoo.com']
ran_web = random.SystemRandom()

webbrowser.open(ran_web.choice(ran))


