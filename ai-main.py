from gen import logic
from control-handler import control
#Configuration
aps = 100
safe = True

def main():
	while True:
		#Get AI's selected action
		action = logic(1)
		#Control the client
		control(action)
		print(action)
if __name__ == __main__:
	main()
		
