#~!~#
#python 3.7.X
#if you are new run this program run this command
#python -m pip install gtts playsound wikipedia

from gtts import gTTS
from playsound import playsound
import os,wikipedia,argparse

class Run:
	def lang(self,lg):
		if lg == None:
			self.langue='en'
		else:
			self.langue=lg

	def wiki(self,query):
		wikipedia.set_lang(self.langue)
		if type(query) == list:
			kalimat=wikipedia.summary(" ".join(str(x) for x in query))
		else:
			kalimat=wikipedia.summary(query)
		print(kalimat)
		if args['say'] == True:
			self.say=gTTS(text=kalimat,lang=self.langue)
			print("\n[!] Making audio...")
			self.say.save('say.mp3')
			print("[OK] Audio started.")
			playsound('say.mp3')

def _help():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('-s','--say', help='To read out the search results', action='store_true')
	parser.add_argument('-l',dest='lang', help='for change language (default:english)')
	parser.add_argument('-q',dest='query', help='for search something to wikipedia', required=True, nargs='*')
	args = vars(parser.parse_args())
#	print(args)

os.system('clear')
print("WIKIPEDIA-CLI")
_help()
try:
	wik=Run()
	wik.lang(args['lang'])
	wik.wiki(args['query'])
except Exception as Err:
	print("ERR: %s"%(Err))
