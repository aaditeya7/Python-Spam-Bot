import pyautogui, time

# 5 second delay so you have time to go and open up whats app or insta
time.sleep(5)

# Opening file in read mode
f = open("msg.txt", 'r')

# For line in file type in the statement and hit enter to send
for line in f:
	pyautogui.typewrite(line)
	pyautogui.press("enter")

# And that's my Python Spam Bot
