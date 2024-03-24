import json, os, sys, random, time

class Universe:
	def __init__(self, seed):
		self.data = {"peoples": {}, "seed": seed, "chc": seed**2, "all_seeds": [seed], "user": ("", 0), "year": 0, "age": 1, "names": []}
		self.chcLevel = seed**2+962846
		self.seed = seed
		list = []
		for h in range(20, 70):
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
		self.data["peoples"]["God"] = 999999999999999999
	def newUniverse(self, seed):
		self.data["peoples"] = {}
		self.data["all_seeds"] = self.data["all_seeds"]+[seed]
		self.chcLevel = seed**2+962846
		self.data["chc"] = self.chcLevel
		self.data["seed"] = seed
		self.data["year"] = 0
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
		self.data["peoples"]["God"] = 999999999999999999
	def summonBoss(self):
		name = self.createName()
		power = self.data["user"][1]*100
		power = self.PowerUp(power)
		print(f"God Boss coming to this universe! (Name: {name} Power: {power})")
		self.data["peoples"][name] = power
	def summonVorathar(self):
		print(f"Boss of the all Universes coming to this Universe! (Vorathar)")
		self.data["peoples"]["Vorathar"] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
	def choice(self, list):
		index = self.seed+self.chcLevel
		index = (index**2)%len(list)
		self.chcLevel += index+self.seed+self.chcLevel+len(self.data["peoples"])+len(self.data["all_seeds"])+len(self.data)+len(self.data["names"])+len(str(self.data["names"]))
		self.data["chc"] = self.chcLevel
		return list[index]
	def createName(self):
		n = 1
		while True:
			list = [2, 3, 4, 5]
			length = self.choice(list)
			name = ""
			for _ in range(length):
				name += self.choice("r t y p s d f g h j k l z c v b n m".split())
				name += self.choice("e u i o a".split())
			name = (name[0].upper())+name[1:]
			length = self.choice(list)
			name2 = ""
			for _ in range(length):
				name2 += self.choice("r t y p s d f g h j k l z c v b n m".split())
				name2 += self.choice("e u i o a".split())
			name2 = (name2[0].upper())+name2[1:]
			if n == 1:
				name = name+" "+name2
			else:
				name = name+" "+name2+" "+str(n)
			if name in self.data["names"]:
				n += 1
			else:
				self.data["names"] = self.data["names"]+[name]
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
	def wait(self, q=True):
		self.data["age"] = self.data["age"]+1
		self.data["year"] = self.data["year"]+1
		if q:
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
		if q:
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
	h = ["\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m"]
	h2 = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]
	h3 = ["\033[1m", "\033[2m", "\033[0m"]
	h4 = []
	for hh in range(33, 129):
		h4.append(chr(hh))
	for _ in range(4000):
		hh = random.choice(h)+random.choice(h2)+random.choice(h3)+random.choice(h4)
		sys.stdout.write(hh)
		sys.stdout.flush()
	print("\033[0m")
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def talkscreen(texts):
	clear()
	for text in texts:
		for h in text:
			sys.stdout.write(h)
			sys.stdout.flush()
			time.sleep(0.035)
		time.sleep(1)
		print()
	time.sleep(3)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	print("\033[0m "*5000)
	time.sleep(0.15)
	print("\033[47m "*5000)
	time.sleep(0.15)
	clear()

def talkscreen2(texts):
	clear()
	for text in texts:
		for h in text:
			sys.stdout.write(h)
			sys.stdout.flush()
			time.sleep(0.035)
		time.sleep(1)
		print()
	time.sleep(3)
	clear()

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
				name = root.data["users"][0]
			else:
				name = input("Enter username: ")
				if name in ["", " "]:
					print("Name is not a name, im creating for you.")
					name = root.data["user"][0]
				else:
					root.user(name)
			print(f"Sucessfuly!")
			root.save("auto-save.json")
			talkscreen(["V?: Do you think he is strong enough to achieve this?", "A?: Man, this man is smarter than you think. If he doesn't succeed, who will?", f"V?: Well then, I gift him a soul like the others. welcome {name}"])
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
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
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
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
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
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
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
			talkscreen(["A?: Yeah I'll give it that one", "V?: Okay then"])
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

def zarathorn(root):
	while True:
		clear()
		print(f"Home of Zarathorn Wizard - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		print("[ 1 ] Summon Vorathar")
		print("[ 2 ] Time Machine")
		print("[ 3 ] Exit from House")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			print("A ritual is held to summon Vorathar")
			time.sleep(3)
			print("Vorathar, creator of all universes, is summoned")
			time.sleep(3)
			root.summonVorathar()
			print("Summon √")
			time.sleep(1)
		elif chc == "2":
			while True:
				clear()
				print("Welcome to Zarathorn's Time Machine")
				print(f"Your age: {root.data['age']}")
				print(f"Current year: {root.data['year']}")
				print()
				print("[ 1 ] Wait 10 year times")
				print("[ 2 ] Wait 100 year times")
				print("[ 3 ] Go to first time")
				print("[ 4 ] Exit from Time Machine")
				print()
				chc = input("Select a option: ")
				if chc == "1":
					for h in range(10):
						print(f"Year: +{h}")
						root.wait(q=False)
				elif chc == "2":
					for h in range(100):
						print(f"Year: +{h}")
						root.wait(q=False)
				elif chc == "3":
					print("Wait 3 seconds...")
					time.sleep(3)
					root.newUniverse(root.seed)
				elif chc == "4":
					break
		elif chc == "3":
			break

def gamemenu(root):
	while True:
		clear()
		print(f"Game Menu - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		print("[ 1 ] Open Your Info")
		print("[ 2 ] Edit Your Info")
		print("[ 3 ] Add/Set People")
		print("[ 4 ] Delete People")
		print("[ 5 ] Exit from Game Menu")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			clear()
			print("Your Info:")
			print()
			name = root.data["user"][0]
			power = root.data["user"][1]
			pc = 0
			g_ava = False
			v_ava = False
			for item, value in root.data["peoples"].items():
				if item == "God":
					g_ava = True
				elif item == "Vorathar":
					v_ava = True
				else:
					pc += 1
			u_seed = root.data["all_seeds"]
			print(f"Name: {name}")
			print(f"Power: {power}")
			print(f"People Count: {pc}")
			print(f"God Avaible?: {g_ava}")
			print(f"Vorathar Avaible?: {v_ava}")
			print(f"Using Seeds: {u_seed}")
			print(f"Your age: {root.data['age']}")
			print(f"Current year: {root.data['year']}")
			print()
			input("[ Enter to next ]")
		elif chc == "2":
			while True:
				clear()
				print("Your Info:")
				print()
				name = root.data["user"][0]
				power = root.data["user"][1]
				print(f"[ 1 ] Name: {name}")
				print(f"[ 2 ] Power: {power}")
				print("[ 3 ] Exit from info")
				print()
				chc = input("Select a option: ")
				if chc == "1":
					name = input("Name: ")
					root.data["user"] = (name, power)
				elif chc == "2":
					power = input("Power: ")
					root.data["user"] = (name, power)
				elif chc == "3":
					break
		elif chc == "3":
			name = input("Name: ")
			power = input("Power: ")
			root.data["peoples"][name] = power
		elif chc == "4":
			name = input("Name: ")
			try:
				del root.data["peoples"][name]
			except:
				pass
		elif chc == "5":
			break

def actionmenu(root):
	while True:
		clear()
		print(f"Action Menu - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		print("[ 1 ] Go to Wizard")
		print("[ 2 ] Go to President")
		print("[ 3 ] Go to ?")
		print("[ 4 ] Kill yourself")
		print("[ 5 ] Take the soul reset pill (Reset the game)")
		print("[ 6 ] Read the universe book")
		print("[ 7 ] Random Adventure")
		print("[ 8 ] Find yourself a teacher")
		print("[ 9 ] Go to new Universe")
		print("[ 10 ] Summon new Boss")
		print("[ 11 ] Go to Zarathorn Wizard")
		print("[ 12 ] Open Game Menu")
		print("[ 13 ] Navigation and Social")
		print("[ 14 ] Exit from Action Menu")
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
			try:
				seed = int(float(input("\nEnter Seed (A Number): ")))
			except:
				seed = random.randint(1, 10000000000)
				print(f"You entered unknow seed,created for you: {seed}")
			print("Going to new universe...")
			time.sleep(3)
			root.newUniverse(seed)
		elif chc == "10":
			root.summonBoss()
			time.sleep(3)
		elif chc == "11":
			zarathorn(root)
		elif chc == "12":
			gamemenu(root)
		elif chc == "13":
			navigation(root)
		elif chc == "14":
			break

def navigation(root):
	while True:
		clear()
		print(f"Navigation and Social - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		print("[ 1 ] Go to village")
		print("[ 2 ] Go to castle")
		print("[ 3 ] Go to plane")
		print("[ 4 ] Exit from this menu")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			n_villagemenu(root)
		elif chc == "2":
			n_castlemenu(root)
		elif chc == "3":
			n_planetmenu(root)
		elif chc == "4":
			break

def landmenu(name, root):
	peoples = []
	for people, power in root.data["peoples"].items():
		if people in ["God", "Vorathar"]:
			pass
		else:
			n = random.randint(1, 3)
			if n == 1:
				peoples.append(people)
	while True:
		clear()
		print(f"Lands / {name} - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		print(f"People from {name} list:")
		print()
		for people in peoples:
			print(people)
		print()
		print(f"[ 1 ] Exit from {name}")
		print()
		chc = input("Select a people or option: ")
		if chc == "1":
			break
		elif chc in peoples:
			talkwith(chc)

def talkwith(chc):
	name = chc
	while True:
		clear()
		print(f"Talking with {name}")
		print()
		print("[ 1 ] Ask villages")
		print("[ 2 ] Ask castles")
		print("[ 3 ] Ask planets")
		print("[ 4 ] Ask universes")
		print("[ 5 ] Ask about God")
		print("[ 6 ] Ask about Vorathar")
		print(f"[ 7 ] Ask about {name}")
		print("[ 8 ] Exit from chat")
		print()
		chc = input("Select a option: ")
		if chc == "1":
			recv = random.choice(["Village life offers serenity and connection to nature, yet demands caution and adjustment to rural isolation.", "The tranquility of villages appeals to those seeking a simpler lifestyle, although adjusting to rural living may pose challenges.", "Living in villages provides a peaceful retreat from urban hustle, yet requires vigilance and acceptance of rural solitude.", "Village living embodies a harmonious relationship with nature, necessitating awareness of safety and readiness for seclusion.", "Villages offer a tranquil haven amidst nature's beauty, but necessitate caution and acclimatization to rural solitude.", "The simplicity of village life attracts those weary of city bustle, yet demands caution and adjustment to isolation.", "Choosing village life means embracing nature's tranquility while being mindful of safety and adapting to rural seclusion.", "Village living promises peace and connection to nature, tempered by the need for caution and acceptance of rural isolation.", "The allure of village life lies in its serene environment, though caution and readiness for solitude are essential.", "Embracing village living entails embracing nature's calm, but requires caution and adjustment to rural seclusion."])
			talkscreen2(["You: How about villages?", f"{name}: {recv}"])
		elif chc == "2":
			recv = random.choice(["Exploring castles evokes a sense of history and wonder, but requires attention to safety and preservation.", "Castles stand as majestic relics of the past, offering glimpses into bygone eras while necessitating preservation efforts.", "Visiting castles transports one to a bygone era of knights and royalty, highlighting the importance of historical preservation.", "Castles symbolize strength and history, yet their preservation demands careful attention and resources.", "Exploring castles ignites the imagination with tales of chivalry and intrigue, emphasizing the need for preservation.", "Castles captivate with their grandeur and history, underscoring the importance of preservation and restoration efforts.", "Wandering through castles offers a glimpse into medieval life, emphasizing the importance of historical conservation.", "Castles embody tales of valor and conquest, but their preservation requires ongoing care and attention.", "Visiting castles provides a window into the past, underscoring the importance of preservation for future generations.", "Castles serve as living monuments to history, demanding ongoing preservation efforts to maintain their legacy."])
			talkscreen2(["You: How about castles?", name+": "+recv])
		elif chc == "3":
			recv = random.choice(["Exploring planets offers insights into the vastness of the universe, prompting curiosity about potential extraterrestrial life.", "Studying planets reveals the diversity of celestial bodies, sparking interest in planetary formation and evolution.", "Learning about planets fuels curiosity about the possibility of human colonization beyond Earth, highlighting the importance of space exploration.", "Understanding planets enhances our knowledge of the solar system's dynamics, fostering appreciation for Earth's unique characteristics.", "Exploring planets deepens our understanding of planetary geology and atmospheres, shedding light on the conditions necessary for life.", "Studying planets allows us to unravel mysteries about the origins of the solar system, inspiring wonder about the cosmos.", "Learning about planets prompts questions about their potential habitability and the search for life beyond Earth.", "Understanding planets informs discussions about climate change and environmental sustainability on Earth, emphasizing the importance of protecting our planet.", "Exploring planets offers insights into the potential for future space exploration and colonization efforts, sparking discussions about humanity's future beyond Earth.", "Studying planets encourages interdisciplinary research across astronomy, geology, and biology, fostering collaboration in the pursuit of scientific knowledge."])
			talkscreen2(["You: How about planets?", name+": "+recv])
		elif chc == "4":
			random.choice(["Contemplating the multiverse theory sparks curiosity about the possibility of alternate realities and dimensions.", "Exploring the concept of parallel universes ignites discussions about the nature of existence and reality.", "Studying the cosmos reveals the vastness of the universe and the potential for diverse forms of life beyond our own.", "Learning about different universes within the multiverse framework prompts philosophical reflections on the nature of existence.", "Understanding the theory of multiple universes fosters discussions about the interconnectedness of all things and the concept of cosmic consciousness.", "Contemplating the existence of parallel universes encourages speculation about the nature of time, space, and consciousness.", "Exploring theories of parallel dimensions offers insights into the potential for alternate realities and parallel versions of ourselves.", "Studying the multiverse hypothesis invites contemplation of the infinite possibilities and outcomes that may exist beyond our observable universe.", "Learning about the multiverse theory challenges conventional notions of reality and opens up new avenues for scientific inquiry and exploration.", "Understanding the concept of parallel universes encourages a broader perspective on life and the universe, inviting wonder and awe at the mysteries that lie beyond our comprehension."])
			talkscreen2(["You: How about universes?", name+": "+recv])
		elif chc == "5":
			recv = random.choice(["Contemplating the concept of God invites reflections on the nature of existence, purpose, and morality.",
"Exploring beliefs about God across different cultures and religions offers insights into the diversity of human spirituality.",
"Studying philosophical arguments for and against the existence of God prompts critical thinking about faith, reason, and skepticism.",
"Learning about religious texts and teachings about God provides understanding of the role of faith in shaping individual and collective worldviews.",
"Understanding the attributes ascribed to God in various religious traditions fosters appreciation for the complexities of divine concepts.",
"Contemplating theodicy and the problem of evil raises profound questions about the nature of God's benevolence and omnipotence.",
"Exploring personal experiences of God and spiritual awakenings offers glimpses into the depths of human consciousness and transcendent experiences.",
"Studying the historical development of religious concepts of God reveals the evolution of human understanding and interpretation of the divine.",
"Learning about different theological perspectives on God encourages dialogue and mutual respect among people of diverse faith traditions.",
"Understanding the mystery and ineffability of God inspires humility and reverence in the face of the divine."])
			talkscreen2(["You: How about God?", name+": "+recv])
		elif chc == "6":
			recv = random.choice(["Vorathar is a mysterious entity often mentioned in folklore, but concrete details about it are scarce.",
"The legend of Vorathar has been passed down through generations, yet its true nature remains elusive.",
"Vorathar is shrouded in mystery, with tales describing it as both a benevolent protector and a malevolent force.",
"Little is known about Vorathar beyond the stories and myths surrounding its existence.",
"The origin of Vorathar is veiled in mystery, leaving scholars and enthusiasts to speculate about its true origins.",
"Vorathar is a subject of fascination and intrigue, with some considering it a mere myth and others believing in its tangible presence.",
"Explorers and researchers have attempted to uncover the truth behind Vorathar, but conclusive evidence remains elusive.",
"Vorathar is often depicted as a figure of awe and fear, embodying the unknown and the enigmatic.",
"Legends of Vorathar vary among cultures, reflecting the diverse interpretations and beliefs surrounding this mysterious entity.",
"Despite the lack of concrete evidence, Vorathar continues to capture the imagination of storytellers and curious minds alike."])
			talkscreen2(["You: How about Vorathar?", name+": "+recv])
		elif chc == "7":
			recv = random.choice(["I'm feeling fantastic, like I'm on top of the world.", "I'm doing great, thanks for asking! Full of energy.", "I'm wonderful, like a ray of sunshine on a beautiful day.", "I'm fantastic, feeling empowered and ready to seize the day.", "I'm fabulous, thank you! Full of positivity and joy.", "I'm excellent, like a well-oiled machine, ready for action.", "I'm splendid, thanks for checking in. Feeling fantastic!", "I'm awesome, like a superhero with a cape. How about you?", "I'm terrific, thanks! Overflowing with enthusiasm.", "I'm doing amazing, like I just won the lottery."])
			talkscreen2(["You: How about You?", name+": "+recv])
		elif chc == "8":
			break
def n_villagemenu(root):
	villages = []
	for _ in range(random.randint(5, 10)):
		villages.append(root.createName()+" Village")
	while True:
		clear()
		print(f"Navigation and Social / Villages - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		for village, n, in zip(villages, range(len(villages))):
			print(f"[ {n+1} ] {village}")
		print(f"[ {len(villages)+1} ] Exit from villages")
		print()
		chc = input("Select a option: ")
		if chc == str(len(villages)+1):
			break
		else:
			try:
				landmenu(villages[int(chc)-1], root)
			except:
				pass

def n_castlemenu(root):
	villages = []
	for _ in range(random.randint(5, 10)):
		villages.append(root.createName()+" Castle")
	while True:
		clear()
		print(f"Navigation and Social / Castles - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		for village, n, in zip(villages, range(len(villages))):
			print(f"[ {n+1} ] {village}")
		print(f"[ {len(villages)+1} ] Exit from castles")
		print()
		chc = input("Select a option: ")
		if chc == str(len(villages)+1):
			break
		else:
			try:
				landmenu(villages[int(chc)-1], root)
			except:
				pass

def n_planetmenu(root):
	villages = []
	for _ in range(random.randint(5, 10)):
		villages.append(root.createName()+" Planet")
	while True:
		clear()
		print(f"Navigation and Social / Planets - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
		print()
		for village, n, in zip(villages, range(len(villages))):
			print(f"[ {n+1} ] {village}")
		print(f"[ {len(villages)+1} ] Exit from planets")
		print()
		chc = input("Select a option: ")
		if chc == str(len(villages)+1):
			break
		else:
			try:
				landmenu(villages[int(chc)-1], root)
			except:
				pass

def menu(root):
	while True:
		clear()
		print(f"Cosmic Chronicles - {root.data['user'][0]}")
		print(f"Your power: {root.data['user'][1]}")
		print(f"Your age: {root.data['age']}")
		print(f"Current year: {root.data['year']}")
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
