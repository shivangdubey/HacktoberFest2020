import binascii
n=9516311845790656153499716760847001433441357
e=65537
d=5617843187844953170308463622230283376298685
msg="python"
print("Message:",msg)
hex_data=binascii.hexlify(msg.encode())
print("Hex data:",hex_data)
pt=int(hex_data,16)
print("PT:",pt)
if pt>n:
    raise Exception("PT is large")
enc_text=pow(pt,e,n)
print("Encrypted text:",enc_text)
dec_text=pow(enc_text,d,n)
print("Decrypted text:",dec_text)
print("Message:",binascii.unhexlify(hex(dec_text)[2:]).decode())
