aa = 'a b'
bb = '你,，'

aa_bytes = aa.encode('utf-8')
print(list(aa_bytes))

bb_bytes = bb.encode('utf-8')
print(list(bb_bytes))