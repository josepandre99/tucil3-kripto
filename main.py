from PyQt5 import QtWidgets, uic
from function import *
from rsa import *
from diffie_hellman import *
from elgamal import *
import re


# init GUI
app = QtWidgets.QApplication([])
call = uic.loadUi("GUI.ui")


# set default
# default value : encryption in rsa, encryption in elgamal
call.radioButton_enkripsi_rsa.setChecked(True)
call.radioButton_enkripsi_elgamal.setChecked(True)

# tab generate key rsa
def get_prima_ke_n():
    n = int(call.lineEdit_prima_ke_rsa.text())
    prima = bilangan_prima_ke(n)
    call.lineEdit_prima_rsa.setText(str(prima))
    
def generate_rsa_key():
    p = int(call.lineEdit_p_rsa.text())
    q = int(call.lineEdit_q_rsa.text())
    e = int(call.lineEdit_e_rsa.text())
    rsa = RSA(p, q, e)
    rsa.generate_key()
    d, n = rsa.private_key()
    call.lineEdit_d_rsa.setText(str(d))
    call.lineEdit_n_rsa.setText(str(n))
    
def save_public_key_rsa():
    e = int(call.lineEdit_e_rsa.text())
    n = int(call.lineEdit_n_rsa.text())
    data_public_key = str(e) + "," + str(n)
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', "Public key files (*.pub)")
    print(filename[0])
    try:
        writeFileText(filename[0], data_public_key)
    except:
        pass
    
def save_private_key_rsa():
    d = int(call.lineEdit_d_rsa.text())
    n = int(call.lineEdit_n_rsa.text())
    data_private_key = str(d) + "," + str(n)
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', "Private key files (*.pri)")
    try:
        writeFileText(filename[0], data_private_key)
    except:
        pass


# tab enkripsi/dekripsi rsa
def load_key_rsa():
    filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '')
    try:
        e_or_d, n = readPublicPrivateKey(filename[0])
        call.lineEdit_ed_rsa.setText(str(e_or_d))
        call.lineEdit_n_ende_rsa.setText(str(n))
    except:
        pass
    
def load_file_input_rsa():
    filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '')
    try:
        input_text = readFile(filename[0])
        call.textEdit_input_rsa.setText(input_text)
    except:
        pass
    
def save_file_output_rsa():
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '')
    output_text = call.textEdit_output_rsa.toPlainText()
    writeFile(filename[0], output_text)
    
def enkrip_dekrip_rsa():
    e_or_d = int(call.lineEdit_ed_rsa.text())
    n_ed = int(call.lineEdit_n_ende_rsa.text())
    input_text = call.textEdit_input_rsa.toPlainText()
    output_text = ''
    if call.radioButton_enkripsi_rsa.isChecked():   # enkripsi
        print("Enkripsi")
        rsa = RSA(e=e_or_d, n=n_ed)
        rsa.set_plain(input_text)
        output_text = rsa.encrypt()
    else:   # dekripsi
        print("Dekripsi")
        rsa = RSA(d=e_or_d, n=n_ed)
        rsa.set_cipher(input_text)
        output_text = rsa.decrypt()
    call.textEdit_output_rsa.setText(output_text)

# tab generate key elgamal
def generate_elgamal_key() :
    p = int(call.lineEdit_p_elgamal.text())
    g = int(call.lineEdit_g_elgamal.text())
    x = int(call.lineEdit_x_elgamal.text())
    elgamal = ElGamal(p, g, x)
    elgamal.generate_key()
    y, _, _ = elgamal.public_key()
    call.lineEdit_y_elgamal.setText(str(y))

def save_public_key_elgamal():
    y = int(call.lineEdit_y_elgamal.text())
    g = int(call.lineEdit_g_elgamal.text())
    p = int(call.lineEdit_p_elgamal.text())
    data_public_key = str(y) + "," + str(g) + "," + str(p)
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', "Public key files (*.pub)")
    print(filename[0])
    try:
        writeFileText(filename[0], data_public_key)
    except:
        pass
    
def save_private_key_elgamal():
    x = int(call.lineEdit_x_elgamal.text())
    p = int(call.lineEdit_p_elgamal.text())
    data_private_key = str(x) + "," + str(p)
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', "Private key files (*.pri)")
    try:
        writeFileText(filename[0], data_private_key)
    except:
        pass

# tab enkripsi/dekripsi elgamal
def load_pubkey_elgamal():
    filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '')
    try:
        y,g,p = readPublicPrivateKey(filename[0])
        call.lineEdit_ygp_elgamal.setText(str(y)+","+str(g)+","+str(p))
    except:
        pass

def load_prikey_elgamal():
    filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '')
    try:
        x,p = readPublicPrivateKey(filename[0])
        call.lineEdit_xp_elgamal.setText(str(x)+","+str(p))
    except:
        pass

def load_file_input_elgamal():
    filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '')
    try:
        input_text = readFile(filename[0])
        call.textEdit_input_elgamal.setText(input_text)
    except:
        pass
    
def save_file_output_elgamal():
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '')
    output_text = call.textEdit_output_elgamal.toPlainText()
    writeFile(filename[0], output_text)

def enkrip_dekrip_elgamal():
    ygp = re.findall(r'\d+', call.lineEdit_ygp_elgamal.text())
    y = int(ygp[0])
    g = int(ygp[1])
    p = int(ygp[2])
    xp = re.findall(r'\d+', call.lineEdit_xp_elgamal.text())
    x = int(xp[0])
    k = int(call.lineEdit_k_elgamal.text())
    input_text = call.textEdit_input_elgamal.toPlainText()
    output_text = ''
    if call.radioButton_enkripsi_elgamal.isChecked():   # enkripsi
        print("Enkripsi")
        elgamal = ElGamal(p,g,x,y=y)
        elgamal.set_plain(input_text)
        output_text = elgamal.encrypt(k)
    else:   # dekripsi
        print("Dekripsi")
        elgamal = ElGamal(p,g,x,y=y)
        elgamal.set_cipher(input_text)
        output_text = elgamal.decrypt()
    call.textEdit_output_elgamal.setText(output_text)

# generate key diffie-hellman
def generate_dh_key():
    n = int(call.lineEdit_n_dh.text())
    g = int(call.lineEdit_g_dh.text())
    x = int(call.lineEdit_x_dh.text())
    y = int(call.lineEdit_y_dh.text())

    dh = Diffie_Hellman(n, g, x, y)
    _, _, K, K_dash = dh.generate_key()
    
    call.lineEdit_K_dh.setText(str(K))
    call.lineEdit_Kdash_dh.setText(str(K_dash))




# click button rsa
# generate prime
call.pushButton_get_prima_rsa.clicked.connect(get_prima_ke_n)
# generate rsa key
call.pushButton_generate_rsa.clicked.connect(generate_rsa_key)
# save rsa public key
call.pushButton_save_public_key_rsa.clicked.connect(save_public_key_rsa)
# save rsa private key
call.pushButton_save_private_key_rsa.clicked.connect(save_private_key_rsa)
# load key rsa
call.pushButton_load_key_rsa.clicked.connect(load_key_rsa)
# load file input rsa
call.pushButton_load_file_rsa.clicked.connect(load_file_input_rsa)
# save file output rsa
call.pushButton_save_file_rsa.clicked.connect(save_file_output_rsa)
# enkrip/dekrip rsa
call.pushButton_enkrip_dekrip_rsa.clicked.connect(enkrip_dekrip_rsa)

# generate elgamal key
call.pushButton_generate_elgamal.clicked.connect(generate_elgamal_key)
# save elgamal public key
call.pushButton_save_public_key_elgamal.clicked.connect(save_public_key_elgamal)
# save elgamal private key
call.pushButton_save_private_key_elgamal.clicked.connect(save_private_key_elgamal)
# load public key elgamal
call.pushButton_load_pubkey_elgamal.clicked.connect(load_pubkey_elgamal)
# load private key elgamal
call.pushButton_load_prikey_elgamal.clicked.connect(load_prikey_elgamal)
# load file input elgamal
call.pushButton_load_file_elgamal.clicked.connect(load_file_input_elgamal)
# save file output elgamal
call.pushButton_save_file_elgamal.clicked.connect(save_file_output_elgamal)
# enkrip/dekrip elgamal
call.pushButton_enkrip_dekrip_elgamal.clicked.connect(enkrip_dekrip_elgamal)


# click button diffie-hellman
# generate key diffie-hellman
call.pushButton_generate_dh.clicked.connect(generate_dh_key)




call.show()
app.exec()

