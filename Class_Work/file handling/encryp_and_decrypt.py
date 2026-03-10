# dumps(): Encryption
# loads(): Decryption
'''
1. JSON
2. Pickle
'''
import json
file = open('temp.txt','a+')
data = {
    'fullname' : 'Kartik Raj',
    'userid' : '1234',
    'password': '*****',
}

enc_data = json.dumps(data)
file.write(enc_data)

file.seek(0)

encReadData = file.read()
print(encReadData, type(enc_data))

ori_data = json.loads(enc_data)
print(ori_data,type(ori_data))

# print(f'Original data : {data}')
# print(f'Type of original data : {type (data)}')
# print()

# enc_data = json.dumps(data)
# print(f'Encrypted data : {enc_data}')
# print(f'Type of encrypted data : {type (enc_data)}')
# print()

# dec_data = json.loads(enc_data)
# print(f'Decrypted data : {dec_data}')
# print(f'Type of Decrypted data : {type (dec_data)}')

file.close()