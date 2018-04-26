password = raw_input("Please enter a password: ")
UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
LC_LETTERS = UC_LETTERS.lower()
NUMS = "1234567890"
SYMBOLS = ".?!&#,;:-_*"

def pass_check(password):
	uppers = [1 if char in UC_LETTERS else 0 for char in password]
	lowers = [1 if char in LC_LETTERS else 0 for char in password]
	nums = [1 if char in NUMS else 0 for char in password]
	# print [1 if char in UC_LETTERS and 2 if char in LC_LETTERS else 0 for char in password]
	return 1 in uppers and 1 in lowers and 1 in nums

print "password validity:"
print "\t" + str(pass_check(password))

def pass_rating(password):
	ans = 0
	uppers = [1 if char in UC_LETTERS else 0 for char in password]
	lowers = [1 if char in LC_LETTERS else 0 for char in password]
	nums = [1 if char in NUMS else 0 for char in password]
	syms = [1 if char in SYMBOLS else 0 for char in password]
	if 1 in uppers and 1 in lowers:
		ans += 2
	if 1 in nums:
		ans += 2
	if 1 in syms:
		ans += 2
	ans += max(0, min(4, (len(password) - 8) / 2))
	return ans

print "password rating:"
print "\t" + str(pass_rating(password))