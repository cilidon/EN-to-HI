import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtGui import *
import nltk
from englisttohindi.englisttohindi import EngtoHindi
from nltk.tokenize import TweetTokenizer
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import * 
import demoji
import re
import alias
import spacy
import itertools



class MainWindow(QDialog): 
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi('final.ui', self) 
		self.setWindowTitle("Automatic Grader")
		self.pushButton.clicked.connect(self.trans)

	def get_key(self,val,my_dict):
		for key, value in my_dict.items():
			if val == value:
				return key

	def trans(self):
		sen = self.textEdit.toPlainText()
		sen=''.join(i for i, _ in itertools.groupby(sen))
		nlp = spacy.load('en_core_web_md')
		sett=demoji.findall(sen)
		toeken=nltk.TweetTokenizer()
		token_Sent=toeken.tokenize(sen)
		for emoji in sett:
			i=token_Sent.index(emoji)
			#print(token_Sent[i-1])
			prior=token_Sent[i-1]
			emoji_text=sett[emoji]
			emoji_text=re.sub('\s','-',emoji_text)
			url=f'https://emojipedia.org/{emoji_text}/'
			alises=alias.getaliases(url)
			temp=[]
			dict={}
			alises.append(emoji_text)
			for alis in alises:
				#alis=re.sub('\s','-',alis)
				data=prior+" "+alis
				tokens= nlp(data)
				print(tokens)
				token1, token2 = tokens[0], tokens[1]
				sim=token1.similarity(token2)
				temp.append(sim)
				dict[alis]=sim
				print(alis,sim)
			max_sim=max(temp)
			alis_elect=self.get_key(max_sim,dict)
			alis_elect=re.sub('-',' ',alis_elect)
			toeken=TweetTokenizer()
			token_alis=toeken.tokenize(alis_elect)
			if(token_alis[-1].lower()=='face'):token_alis[-1]=''
			alis_elect=' '.join(token_alis)
			if(alis_elect.lower() not in token_Sent):token_Sent[i]=alis_elect
			else:token_Sent[i]=''
		sen=' '.join(token_Sent)
		print(sen)		
		result = EngtoHindi(sen)
		print(str(result.convert))
		self.textBrowser.setText(str(result.convert))
		
# main
app = QApplication(sys.argv)
mainwindow = MainWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMinimumHeight(750)
widget.setMinimumWidth(1120)
widget.setWindowTitle("Machine Translation")
widget.setWindowIcon(QIcon("icon.png"))
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")
