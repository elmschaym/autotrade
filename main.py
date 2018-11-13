import sys
import threading
import pickle
from autotradeviper import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
#from PyQt5.uic import loadUi
from gui import *

import re
tp_value=""
sl_value=""
trade_amount = ""
class Autobot(QDialog,Ui_Dialog):
	def __init__(self):
		super(Autobot, self).__init__()
		#loadUi('autobot.ui', self)
		#self.setupui = Ui_Dialog()
		self.setupUi(self)
		self.setWindowTitle('Autobot Powered by Rasmer')
		self.start.clicked.connect(self.on_push_clicked_start)
		self.end.clicked.connect(self.on_push_clicked_end)

		try:
			pickle_in = open("config_def.pickle","rb")
			config_dict_look = pickle.load(pickle_in)
			print(config_dict_look,'sadasd')
			self.tplineedit.setText(config_dict_look[1])
			self.sllineedit.setText(config_dict_look[2])
			self.tradeamountlineedit.setText(config_dict_look[3])
			self.file_path_field.setText(config_dict_look[4])
		except :
			pass

	@pyqtSlot()
	def on_push_clicked_start(self):
		print("GO GO GO GO GO POWER RANGER!!!!")    


		tp_value=self.tplineedit.text()
		sl_value=self.sllineedit.text()
		trade_amount=self.tradeamountlineedit.text()
		file_path=self.file_path_field.text()
		config_dict = {1:tp_value,2:sl_value,3:trade_amount,4:file_path}
		pickle_out = open("config_def.pickle","wb")
		pickle.dump(config_dict, pickle_out)
		pickle_out.close()
		
		self.thread = ThreadingExample(tp_value,sl_value,trade_amount,file_path)

		
		def printit():
			#print( self.thread.get_iq_balance(),'printit') 
			if self.thread.get_iq_balance() == "not_found":
				self.labelbalance.setText("BALANCE UNAVAILABLE")
			elif self.thread.get_iq_balance() == "less_than":
				self.labelbalance.setText("NOT ENOUGH BALANCE")
			elif float(self.thread.get_iq_balance()) >= 1:
						self.labelbalance.setText(str(self.thread.get_iq_balance()))
			else:
				self.labelbalance.setText("Opps!! Error")
			
			threading.Timer(10.0, printit).start()
		printit()
		self.start.setEnabled(False)
		self.tplineedit.setEnabled(False)
		self.sllineedit.setEnabled(False)
		self.tradeamountlineedit.setEnabled(False)
		self.file_path_field.setEnabled(False)
		#print (thread.tp_value,thread.sl_value,thread.trade_amount,"Button")
	@pyqtSlot()
	def on_push_clicked_end(self):
		
		self.thread.end()
		sys.exit()
		# stops = StoppableThread(threading)
		# stops.stop()
	
if __name__ == '__main__':
    
	app=QApplication(sys.argv)
	widget=Autobot()
	widget.show()
	sys.exit(app.exec_())
