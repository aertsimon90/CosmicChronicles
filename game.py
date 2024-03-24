import json, os, sys, random, time

class Universe:
	def __init__(self, seed):
		self.data = {"peoples": {}, "seed": seed, "chc": seed**2}
		self.chcLevel = seed**2+962846
		self.seed = seed
		list = []
		for h in range(30, 100):
			list.append(h)
		charnum = self.choice(list)
		list = []
		for h in range(2, 50):
			list += [h]
		for _ in range(charnum):
			name = self.createName()
			power = self.choice(list)
			self.data["peoples"][name] = power
		self.user(self.createName())
		self.data["peoples"]["God"] = 999999999
	def choice(self, list):
		index = self.seed+self.chcLevel
		index = (index**2)%len(list)
		self.chcLevel += index*len(list)+8729
		self.data["chc"] = self.chcLevel
		return list[index]
	def createName(self):
		while True:
			list = []
			for h in range(2, 6):
				list.append(h)
			length = self.choice(list)
			name = ""
			for _ in range(length):
				name += self.choice("q r t y p s d f g h j k l z c v b n m".split())
				name += self.choice("e u i o a".split())
			name = (name[0].upper())+name[1:]
			if name in self.data["peoples"]:
				pass
			else:
				return name
	def user(self, name):
		self.data["user"] = (name, self.choice([2, 3, 4, 5]))
	def PowerUp(self, power):
		try:
			power += int(int(power*50)/100)
		except:
			pass
		if power >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
			power = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
		return power
	def userPowerUp(self):
		power = self.data["user"][1]
		power = self.PowerUp(power)
		self.data["user"] = (self.data["user"][0], power)
	def wait(self):
		print("Some guys got new powers...")
		time.sleep(1)
		for item, value in self.data["peoples"].items():
			if item == "God":
				pass
			else:
				value = self.PowerUp(value)
				self.data["peoples"][item] = value
		list = []
		for h in range(2, 50):
			list += [h]
		name = self.createName()
		self.data["peoples"][name] = self.choice(list)
		time.sleep(1)
		print(f"Somebody coming to universe! Name: {name}")
		time.sleep(1)
	def save(self, file):
		try:
			os.chdir("saves")
		except:
			os.mkdir("saves")
			os.chdir("saves")
		with open(file, "w") as f:
			f.write(json.dumps(self.data, indent=4))
		os.chdir("..")
	def load(self, file):
		try:
			os.chdir("saves")
		except:
			os.mkdir("saves")
			os.chdir("saves")
		with open(file, "r") as f:
			self.data = json.loads(f.read())
		os.chdir("..")

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def startmenu():
	while True:
		clear()
		print(f"Welcome to Cosmic Chronicles! (v1.0.0)\n\n[ 1 ] New Game\n[ 2 ] Load Game\n[ 3 ] Exit\n")
		chc = input("Select Option: ")
		if chc == "1":
			try:
				seed = int(float(input("\nEnter Seed (A Number): ")))
			except:
				seed = random.randint(1, 10000000000)
				print(f"You entered unknow seed,created for you: {seed}")
			name = input("Use a username? (If you enter no, game will create name for you.) (Y/n): ")
			print("Generating Universe...")
			root = Universe(seed)
			if name.lower() == "n":
				pass
			else:
				name = input("Enter username: ")
				if name in ["", " "]:
					print("Name is not a name, im creating for you.")
				else:
					root.user(name)
			print(f"Sucessfuly!")
			root.save("auto-save.json")
			menu(root)
		elif chc == "2":
			clear()
			print("Select a save file:\nFile list:\n")
			try:
				os.chdir("saves")
			except:
				os.mkdir("saves")
				os.chdir("saves")
			for h in os.listdir():
				print(h)
			os.chdir("..")
			print()
			chc = input("Filename: ")
			root = Universe(0)
			try:
				root.load(chc)
			except:
				pass
			menu(root)
		elif chc == "3":
			clear()
			sys.exit()
		else:
			print(f"Please select a option")
			time.sleep(1)

def wizard(root):
	while True:
		clear()
		print(f"Home of Wizard - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print()
		print("[ 1 ] Ask how to power up")
		print("[ 2 ] Ask where is the president")
		print("[ 3 ] Ask what's God")
		print("[ 4 ] Exit from house")
		print()
		chc = input("Select question option: ")
		if chc == "1":
			print()
			sys.stdout.write("Wizard: ")
			sys.stdout.flush()
			text = "You are asking questions to get stronger, you may need to find a teacher and take a course or train yourself to get stronger. If you are looking for a more fun way, you can play games with your enemies... :)"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			print()
			input("[ Enter to next ]")
		elif chc == "2":
			print()
			sys.stdout.write("Wizard: ")
			sys.stdout.flush()
			text = "They ask this a lot these days, there are people who say the president went on vacation...... But in reality he was actually killed by a predator we don't know what happened, whatever the globe tells us"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			print()
			input("[ Enter to next ]")
		elif chc == "3":
			print()
			sys.stdout.write("Wizard: ")
			sys.stdout.flush()
			text = "The power he has is so great that he cannot understand what he is or what he looks like. Maybe one day you can see it"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			print()
			input("[ Enter to next ]")
		elif chc == "4":
			break

def president(root):
	while True:
		clear()
		print(f"President Hall - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print()
		print("It's so quiet and deserted, the lights are forgotten on and there's only a trace of blood on the carpet...")
		print()
		input("[ Enter to exit from hall ]")
		break

def unknowguy(root):
	while True:
		clear()
		print("\033[91m")
		clear()
		print(f"? (Unknow Guy) {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print()
		time.sleep(1)
		text = "It's like there's nothing here..."
		for h in text:
			sys.stdout.write(h)
			sys.stdout.flush()
			time.sleep(0.05)
		print()
		time.sleep(2)
		text = "It's like I came here but I didn't have any purpose, why did I come here?"
		for h in text:
			sys.stdout.write(h)
			sys.stdout.flush()
			time.sleep(0.05)
		print()
		time.sleep(2)
		chc = input("Answer: ")
		if chc == "got god powers":
			for _ in range(100):
				root.userPowerUp()
			text = "What the f**k is going on!"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			time.sleep(2)
			clear()
			print("\033[0m")
			clear()
			break
		elif chc == "nothing":
			text = "Im feeling nothing..."
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			time.sleep(2)
			clear()
			print("\033[0m")
			clear()
			break
		elif chc == "?":
			text = "?: You came here for me"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			time.sleep(2)
			text = "?: Let me tell you"
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			time.sleep(2)
			text = """aertsimon90: My name is aertsimon90 (Simon Scap), I am the producer of this game :D
I'm glad you came this far, I appreciate you playing this game, I'll tell you something; If you come to this place again and write "got god powers" as an answer, you will have god powers."""
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.05)
			print()
			time.sleep(2)
			clear()
			print("\033[0m")
			clear()
			break
		else:
			clear()
			print("\033[0m")
			clear()
			break
		
def actionmenu(root):
	while True:
		clear()
		print(f"Action Menu - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print()
		print("[ 1 ] Go to Wizard")
		print("[ 2 ] Go to President")
		print("[ 3 ] Go to ?")
		print("[ 4 ] Kill yourself")
		print("[ 5 ] Take the soul reset pill (Reset the game)")
		print("[ 6 ] Read the universe book")
		print("[ 7 ] Random Adventure")
		print("[ 8 ] Find yourself a teacher")
		print("[ 9 ] Exit from Action Menu")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			wizard(root)
		elif chc == "2":
			president(root)
		elif chc == "3":
			unknowguy(root)
			root.save("auto-save.json")
		elif chc == "4":
			sys.exit()
		elif chc == "5":
			print("Soul are reset...")
			root.data["user"] = (root.data["user"][0], 2)
			time.sleep(1)
		elif chc == "6":
			print()
			text = f"""What was the universe created from?
The universe is created entirely from light, everyone is possessed with its own soul, and every particle is possessed with its own cell.
Each of these universes is infinite, and this universe notebook is written exactly for the universe numbered {root.seed}"""
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.02)
			print()
			time.sleep(1)
			if root.seed == 0:
				text = f"""The story in the universe number 0, which is the middle region and the most just region of everything, is this:
God created his most helpless servant who could become as powerful as himself, and gave him intelligence and a real environment, and he has the name {root.data['user'][0]}
One day, {root.data['user'][0]} wanted to get away from the environment that was full of chaos but not a single sound was heard, and then he found the solution in the book of the universe. He was impatient to understand every word he read in the book of the universe, whether it was in his own language or not, and he wanted to get lost in real peace. He was so helpless that it was as if he was only writing on a keyboard. He was not surprised when he learned that everything was made up of cells. Because there could be so many universes, he wanted to discover each of them, because the seed of each universe is different. differ from each other in the universe
The number of universes is infinite, but the helpless servant is but a particle.
But remember that God, who loves him because he is in his own universe, has worked as much as possible for him..."""
			else:
				text = """In this universe, where everything is more complex and corrupt, there is no story or element. Everything and everyone was created for its own order..."""
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.02)
			print()
			time.sleep(1)
			print()
			input("[ Enter to exit from universe book ]")
		elif chc == "7":
			adv = [random.choice(["While sitting around the campfire under the stars, I heard a distant wolf howling.", "I found an old map and decided to research the location of a mysterious temple.", "I went for a night hike and a beam of mysterious light appeared in the sky.", "Walking along the riverbank, I found a clue to solve the mystery of a snake emerging from the water.", "I entered an old mansion at night and heard a mysterious sound inside.", "I dived into the deep seas to search for the wreckage of a lost ship and encountered a mysterious creature.", "While wandering in the forest, I stopped in front of the ruins of an ancient temple and decided to enter.", "I climbed to the top of the mountain and discovered an entrance at the edge of a cliff.", "I went diving into an ancient cave and found a clue indicating a valuable treasure inside.", "I sailed to a distant island and embarked on a quest for a lost pirate treasure."])]
			list = ["After that, I saw a man and he stared at me, unable to understand what was happening. He seemed to be frightened as if he had seen something. I wanted to greet him, but he didn't respond.", "Later, I noticed smoke in the distance and thought to myself that it seemed like a fire had broken out. However, no matter how strong I was, I couldn't bring myself to walk due to laziness.", "Following that, I stumbled upon a hidden cave entrance and felt a sense of curiosity overwhelming me. I cautiously entered, not knowing what awaited me inside.", "Subsequently, I encountered a group of travelers who seemed lost and confused. I offered them assistance, but they seemed wary of me and hurriedly moved on.", "Afterward, I stumbled upon an ancient relic buried in the ground. As I touched it, I was overcome with a sense of foreboding, as if disturbing something sacred.", "Then, I heard a mysterious whisper in the wind, urging me to follow it. Intrigued, I followed the sound, unaware of where it would lead me.", "Soon after, I encountered a wounded animal on the forest path. Despite my initial hesitation, I decided to help it and nursed it back to health.", "Later on, I stumbled upon a hidden treasure chest buried beneath the sand. As I opened it, I was filled with excitement and anticipation.", "Following that, I witnessed a rare celestial event in the night sky. It filled me with awe and wonder, reminding me of the vastness of the universe.", "After that, I came across a group of mysterious figures performing a ritual in the moonlight. I observed from a distance, unsure of their intentions.", "Subsequently, I found myself caught in a sudden thunderstorm. Despite my best efforts, I struggled to find shelter and protect myself from the elements.", "Later, I stumbled upon a forgotten ancient ruin hidden deep in the jungle. Exploring its depths, I uncovered secrets long lost to time.", "Then, I encountered a wise old sage who offered me cryptic advice and guidance. Though unsure of its meaning, I thanked him and continued on my journey.", "Soon after, I witnessed a breathtaking sunset over the horizon, filling me with a sense of peace and tranquility.", "Afterward, I found myself trapped in a maze of twisting tunnels beneath the earth's surface. Lost and disoriented, I struggled to find my way out.", "Then, I stumbled upon a hidden oasis in the desert, a welcome respite from the harsh surroundings. I rested there, replenishing my strength.", "Following that, I encountered a mysterious stranger who offered me a cryptic riddle to solve. Intrigued, I accepted the challenge and set out to unravel its secrets.", "Later on, I found myself ensnared in a deadly trap set by unknown assailants. With quick thinking and ingenuity, I managed to escape unscathed.", "After that, I witnessed a rare phenomenon in the sky, leaving me in awe of the wonders of the universe.", "Subsequently, I stumbled upon a hidden underground cavern filled with shimmering crystals. Mesmerized by their beauty, I collected a few as souvenirs.", "Then, I encountered a lost traveler in need of assistance. Despite my own reservations, I offered to guide them to safety.", "Soon after, I stumbled upon a forgotten temple hidden deep in the jungle. Exploring its ancient halls, I uncovered relics of a bygone era.", "Following that, I witnessed a fierce battle between two mythical creatures. Though tempted to intervene, I chose to observe from a safe distance.", "Later, I found myself caught in the midst of a raging storm at sea. With skill and determination, I navigated through the treacherous waters to safety.", "Afterward, I stumbled upon a hidden village nestled in the mountains. Intrigued by its inhabitants, I sought to learn more about their way of life.", "Then, I encountered a mysterious portal leading to another realm. Curiosity piqued, I stepped through, unsure of what awaited me on the other side.", "Subsequently, I found myself face to face with a legendary creature of myth and legend. Despite my fear, I approached it with caution, seeking to learn its secrets.", "Following that, I witnessed a spectacular meteor shower illuminating the night sky. It filled me with a sense of wonder and awe.", "Later on, I stumbled upon an ancient tome filled with arcane knowledge. Intrigued, I pored over its pages, hoping to unlock its secrets.", "After that, I found myself in the midst of a bustling marketplace, surrounded by merchants and traders from far and wide. Curious, I explored the myriad goods on offer."]
			for _ in range(random.randint(5, 15)):
				adv.append(random.choice(list))
			print()
			text = " ".join(adv)
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.02)
			print()
			time.sleep(2)
			print()
			input("[ Enter to next ]")
		elif chc == "8":
			name = root.createName()
			name2 = root.createName()
			text = [f"""I went on a search and found {name2} Martial Arts Club. When I entered, a person named {name} said, "If you want to learn, I can teach you" and started explaining."""]
			list = ["Martial arts are not just about physical strength, they are also about mental strength. You must learn to control yourself and maintain inner balance.", "Keep your breath regulated during fights. Proper breathing can increase your endurance and help you maintain controlled movements.", "Try to predict your opponent's movements in advance. Watch carefully and identify their weak points.", "Be aggressive in defending yourself. Being passive can make you vulnerable. Take action and take control.", "Never lose focus during fights. Block out anything that distracts you and observe your opponent closely.", "Fighting is not just a physical activity, it's also a mental game. Think strategically and plan your moves ahead.", "Have confidence in yourself, but never be arrogant. Confidence is the key to success, but overconfidence can be harmful.", "Don't lose control during fights. Anger or excitement can lead to irrational actions. Stay calm and focused.", "Observe your opponent and try to predict their movements. Consider possibilities and analyze to make the best decision.", "Patience is important in martial arts. Don't expect quick results, strive to constantly improve yourself."]
			for _ in range(random.randint(1, 3)):
				text.append(random.choice(list))
			print()
			text = " ".join(text)
			for h in text:
				sys.stdout.write(h)
				sys.stdout.flush()
				time.sleep(0.02)
			print()
			time.sleep(2)
			print()
			root.userPowerUp()
			input("[ Enter to next ]")
		elif chc == "9":
			break

def menu(root):
	while True:
		clear()
		print(f"Cosmic Chronicles - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print()
		print("[ 1 ] Display Peoples")
		print("[ 2 ] Enter Fight")
		print("[ 3 ] Wait the next year")
		print("[ 4 ] Train the character")
		print("[ 5 ] Action")
		print("[ 6 ] Save Game")
		print("[ 7 ] Go Back to Start Menu")
		print("[ 8 ] Exit Game")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			clear()
			for item, value in root.data["peoples"].items():
				print(f"{item} - Power: {value}")
			print()
			input("[ Enter to exit displaying ]")
		elif chc == "2":
			clear()
			for item, value in root.data["peoples"].items():
				print(f"{item} - Power: {value}")
			print()
			while True:
				target = input("Enter Target: ")
				if target in root.data["peoples"]:
					print(f"Selected: {target}")
					break
				else:
					print("Target people not found.")
			targetp = root.data["peoples"][target]
			userp = root.data["user"][1]
			usern = root.data["user"][0]
			while True:
				clear()
				print(f"Target enemy:\nName: {target}\nAvaible Power: {targetp}\n\nYou:\nName: {usern}\nAvaible Power: {userp}\n")
				print("[ 1 ] Attack (with your %50 Power)")
				print("[ 2 ] Heal (power up %20)")
				print("[ 3 ] Use Shield (disable attack of %50)")
				print("[ 4 ] Run!")
				print()
				chc = input("Enter option: ")
				targetchc = root.choice(["1", "2", "3"])
				print(f"Enemy choice: {targetchc}")
				if targetchc == "1":
					eattack = targetp*50/100
				elif targetchc == "2":
					targetp += targetp*20/100
				if chc == "1":
					attack = userp*50/100
					if targetchc == "3":
						attack = attack*50/100
					targetp -= attack
					if targetchc == "1":
						userp -= eattack
				elif chc == "2":
					userp += userp*20/100
					if targetchc == "1":
						userp -= eattack
				elif chc == "3":
					if targetchc == "1":
						eattack = eattack*50/100
						userp -= eattack
				elif chc == "4":
					print("You will runned!")
					input("[ Enter to next ]")
					break
				else:
					print("Your dont make anything.")
					if targetchc == "1":
						userp -= eattack
				input("[ Enter to next ]")
				if targetp <= 0:
					if userp <= 0:
						print("Fight are draw!")
						input("[ Enter to next ]")
						break
					else:
						print(f"Enemy power: {targetp}")
						print("You win!")
						print("Powered up!")
						chc = input(f"Will kill target ({target}) ? (Y/n): ").lower()
						if chc == "y":
							print(f"Target ({target}) is dead :(")
							if target == "God":
								print("GAME IS OVER!")
								print("You so professional in the terminal games! :D")
								print("User get the God is Powers (100 Trainings)")
								for _ in range(100):
									root.userPowerUp()
							del root.data["peoples"][target]
						input("[ Enter to next ]")
						root.userPowerUp()
						root.save("auto-save.json")
						break
				elif userp <= 0:
					if targetp <= 0:
						print("Fight are draw!")
						input("[ Enter to next ]")
						break
					else:
						print(f"User power: {userp}")
						print(f"Enemy ({target}) win :(")
						input("[ Enter to next ]")
						break
		elif chc == "3":
			print("Waiting ...")
			root.wait()
			root.save("auto-save.json")
			input("[ Enter to next ]")
		elif chc == "4":
			print("Training ...")
			time.sleep(3)
			root.userPowerUp()
			root.save("auto-save.json")
		elif chc == "5":
			actionmenu(root)
		elif chc == "6":
			file = input('Filename: ')
			root.save(file)
		elif chc == "7":
			break
		elif chc == "8":
			sys.exit()

startmenu()