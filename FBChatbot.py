from flask import  Flask, request
import requests
from pymessenger import Bot

app = Flask(__name__)

VERIFY_TOKEN = "SS"
PAGE_ACCESS_TOKEN = "EAACqRrvnuoABAJI6aDZBp6DfEVgeKGZC8ASCIDIu0VyKZC86fduKaRUmHOgDAKMnSE8JUmDkZBJehQZBjUIr8IbFkZASxAVszrBlmjvZB3tZBCg4D6s0qkd77WZAAX4pmD1oOoRkamA9n4RCWSVtNuCx2XXZCYuUkeCRvGWLs4AlWs7YSMMK1NZCxH2"
bot = Bot(PAGE_ACCESS_TOKEN)

def handling_message(text):
	adjusted_msges = text
	if adjusted_msges == "hi" or adjusted_msges == "Hi" or adjusted_msges == "Hello" or adjusted_msges == "hello" :
		response = "Hello"

	elif adjusted_msges == "What's up" or adjusted_msges == "what's up" or adjusted_msges == "wassup" or adjusted_msges == "Whatsup" :
		response = "Nothing much, wt abt u??"

	else : 
		response = "Can you give me ten mins i have important stuff to do"

	return response


@app.route('/', methods =["POST","GET"])

def web_hook():
	if request.method == 'GET' :
		if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if request.args.get('hub.verify_token') == VERIFY_TOKEN :
			return request.args.get('hub.challenge')

		else :
			return "Cant connect"

	elif request.method == 'POST' :
		data = request.json
		process = data['entry'][0]['messaging']
		for msg in process:
			text = msg['message']['text']
			sender_id = msg['sender']['id']
			response = handling_message(text)
			bot.send_text_message(sender_id, response)

		return 'message_posted'
	else:
		return ok

if __name__ == '__main__' :
	app.run()
