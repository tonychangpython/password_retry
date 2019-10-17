# 密碼重複程式
# password = 'a123'
# 最多輸入三次
# 如果正確印出 "登入成功"
# 如果不正確 印出"密碼錯誤! 還有_次機會!"
password = 'a123'
i = 3
while i > 0:
	i = i -1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print(' 還有', i,'次機會!')
		else:	
			print('沒機會了 要鎖帳號了!')