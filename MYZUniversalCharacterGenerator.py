# r/RedRuttinRabbit
# Mutant: Year Zero Character Generator!
import random
import string
import os
while 1 == 1:
    elyfirstnoblenames = ["Afton", "Agrona", "Aida", "Aiken", "Aislinn", "Alden",
                          "Aldrich", "Allard", "Allston", "Alvina", "Ariana",
                          "Arleigh", "Arlo", "Ashley", "Audrey", "Avon", "Bailey",
                          "Ballard", "Bancroft", "Beldon", "Beverly", "Blaine",
                          "Blossom", "Blythe", "Brea", "Brenda", "Brewster",
                          "Brinley", "Buckley", "Burne", "Cade", "Calhoun",
                          "Calvert", "Cameron", "Carleton", "Carlyle", "Carvell",
                          "Chilton", "Claiborne", "Clifford", "Colbert", "Colter",
                          "Corliss", "Creighton", "Dale", "Dayton", "Demelza",
                          "Digby", "Donald", "Douglas", "Doyle", "Duncan",
                          "Dustin", "Eartha", "Edda", "Edgar", "Edith", "Edmund",
                          "Edward", "Edwin", "Egerton", "Eldon", "Eldridge",
                          "Elmer", "Emerson", "Esmond", "Ethel", "Farley", "Farrah",
                          "Fern", "Fiona", "Gilford", "Godiva", "Golda", "Gordon",
                          "Hadley", "Haley", "Halsey", "Harlan", "Harmony",
                          "Hayden", "Haywood", "Hazel", "Hedwig", "Hendrick",
                          "Henley", "Herbert", "Hertha", "Hollace", "Holly", "Hope",
                          "Horton", "Humphrey", "Idina", "Isolda", "Ivy", "Jocelyn",
                          "Kenley", "Kenton", "Kimberley", "Kyla", "Layton", "Leigh",
                          "Leslie", "Lindsay", "Locke", "Luella", "Lyndon", "Maida",
                          "Manley", "Marsden", "Millard", "Milton", "Misty",
                          "Nara", "Nelson", "Nyle", "Ogden", "Osmond", "Oswin",
                          "Payton", "Penley", "Preston", "Radella", "Ransford",
                          "Ransley", "Reginald", "Remington", "Ridley"]
    elyfirstlowername = ["Abner", "Ada", "Aggie", "Aldus", "Aram", "Baltus",
                         "Barb", "Berton", "Bessie", "Birdie", "Burch", "Callie",
                         "Celia", "Clane", "Cleon", "Daisy", "Derris", "Dolly",
                         "Dottie", "Ebbon", "Elma", "Elos", "Enid", "Festus", "Flossie",
                         "Garnet", "Ginny", "Grizzie", "Haskel", "Hattie",
                         "Heran", "Ivey", "Jobe", "Josey", "Lent", "Lindy", "Lissie",
                         "Lulu", "Lyman", "Lynk", "Mallie", "Molly", "Morrie",
                         "Mott", "Nettie", "Odell", "Ona", "Peachie", "Pell",
                         "Pimm", "Quitman", "Rena", "Roxie", "Sadoc", "Suvia",
                         "Taron", "Trixie", "Willon", "Winnie"]
    labfirstnames = {
        "Dog": ["Gagarin", "Laika", "Aldrin", "Tereshkova", "Sputnik"],
        "Cat": ["Cassius", "Octavia", "Agrippa", "Lucilla", "Flavia"],
        "Rat": ["Vivaldi", "Mozart", "Mendelssohn", "Rachmaninov"],
        "Bear": ["Truffaut", "Bogart", "Garbo", "Bergman"],
        "Ape": ["Newton", "Curie", "Einstein", "Bohr", "Oppenheimer"],
        "Rabbit": ["Ronaldo", "Totti", "Zlatan"],
        "Badger": ["Krutov", "Salming", "Gretzky"],
        "Reptile": ["Piaf", "Elvis", "Dolly", "Pavarotti"],
        "Moose": ["Milton", "Shelly", "Yeats", "Poe"]
    }
    corefirstnames = ["Hugust", "Lenny", "Marl", "Pontis", "Otlak", "Ingrit", "Mubba", "Nelma", "Rebeth", "Quark", "Octane", "Plonk", "Zingo", "Zippo", "Delta", "Iridia", "Loranga", "Nafta", "Zanova", "Danko", "Endel", "Franton", "Hammed", "Max", "Felin", "Jena", "Katin", "Krin", "Tula", "Abed", "Denrik", "Fillix", "Jonar", "Leodor", "Jolisa", "Lula", "Marlian", "Monja", "Novia",
                      "Finn", "Jony", "Mohan", "Montiak", "Rasper", "Anny", "Brie", "Krinnel", "Linna", "Sofin", "Erister", "Olias", "Maxim", "Silas", "Victon", "Amara", "Danova", "Johalin", "Hanneth", "Miri", "Augustian", "Kristor", "Maximon", "Mohamin", "Oskartian", "Birktorla", "Elona", "Gunitt", "Natara", "Bristin", "Dink", "Fils", "Hent", "Mart", "Wilo", "Alia", "Eria", "Henny", "Kim", "Lin"]
    mechfirstnames = ["Lei", "Ran", "Nixon", "Dallas", "Nova", "Hunang", "Venus", "Cesar", "Shiva", "Delta", "Bonker", "Burl", "Skip", "Sully", "Duct", "Smeg", "Surya", "Nella", "Just", "Thump", "Parvati", "Jasper", "Meta", "Miranda", "Mariki", "Flora", "Julius", "Lussala", "Manola", "Anjali", "Donner", "Gisele", "Haddock", "Dhaval", "Elissa", "Sunita", "Edmond", "Sumana", "Sankar", "Samuel",
                      "Rani", "Jocelyn", "Eustacia", "Felicia", "Eloah", "Abha", "Farley", "Mandeep", "Vinay", "Arianne", "Rhea", "Lenora", "Etta", "Tisco", "Prabod", "Guadalupe", "Jia", "Burz", "Mahendra", "Tamika", "Ling", "Turbo", "Chanda", "Claxon", "Yeybox", "Tiny", "Sputnik", "Mekog", "Rajendra", "Klarice", "Yasmina", "Luna", "Pontiac", "Wall", "Shivali", "Vicente", "Penelope", "Yan", "Gabino"]
    houses = ["Morningstar", "Kilgore", "Fortescue", "Warburg"]
    lowerhouses = ["Abram", "Alton", "Badger", "Barlow", "Barton", "Benson",
                   "Bing", "Brady", "Budd", "Coombs", "Dudley",
                   "Hale", "Harlan", "Holton", "Merton", "Morley", "Norton",
                   "Ogden", "Reed", "Skelton", "Tenley", "Tickle",
                   "Tinley", "Vance", "Weld"]
    elygeneraltraits = ["Backstab", "Double Wielder", "Elusive", "Fast Healer", "Fencer",
                        "Machine At Heart", "Overseer", "Rapid Fire", "Reputable", "Robot Hunter", "Rot Resistant"]
    labgeneraltraits = ["Comfort Eater", "Defensive", "Mechanic", "Monster Whisperer", "Naturist",
                        "Nine Lives", "Quick Fire", "Slayer", "Slugger", "Tenacious", "Throwing Arm", "Scrounger", "Wanderer"]
    coregeneraltraits = ["Admirer", "Archeologist", "Assassin", "Bad Omens", "Bodyguard", "Butcher", "Combat Veteran", "Cool Head", "Counselor", "Coward", "Fast Draw", "Flyweight", "Gadgetter", "Good Footwork",
                         "Hard Hitter", "Workhorse", "Jack of All Trades", "Light Eater", "Loner", "Never Surrender", "Pack Mule", "Personal Arithmetic", "Sharpshooter", "Sleepless", "Stoic", "Therapist", "Weapon Specialist", "Zone Cook"]
    mechgeneraltraits = ["Analyzing Unit", "Backup Power", "Battery Charger", "Cargo Lift", "Combustion Engine", "Crank Generator", "Deep Data", "Extra Plating", "Firewall",
                         "Flotation Device", "Hydraulic Crane", "Overdrive", "Power Saver", "Psi-Alarm", "Robo-Alarm", "Robo-Chef", "Self-Destruct Mechanism", "Solar Panels", "Telescopic Eye", "Weapons Rig"]
    professiontraits = {
        "Investigator": ["Intuition", "Many Faces", "Well Connected"],
        "Officer": ["Commander", "Feared Enemy", "Icy Voice"],
        "Procurator": ["Defender", "Pettifogger", "Public Servant"],
        "Scholar": ["Bearer of Knowledge", "Crucial Insight", "Judge of Character"],
        "Soldier": ["Beefy", "Biomechatronic", "True Grit"],
        "Technician": ["Biomechatronic", "Field Surgeon", "Grease Monkey"],
        "Enforcer": ["Barge Through", "Mean Stream", "Sucker Punch"],
        "Gearhead": ["Inventor", "Motorhead", "Tinkerer"],
        "Stalker": ["Scavenger", "Monster Hunter", "Rot Finder"],
        "Fixer": ["Wheeler Dealer", "Vicious Creep", "Juicy Info"],
        "Dog Handler": ["Bloodhound", "Fight Dog", "Mutant's Best Friend"],
        "Chronicler": ["Bonesaw", "Agitator", "Performer"],
        "Boss": ["Commander", "Gunslingers", "Racketeer"],
        "Slave": ["Cynic", "Rebel", "Resilient"],
        "Healer": ["Moonshiner", "Surgeon", "Therapist"],
        "Hunter": ["Bowyer", "Skinner", "Trapper"],
        "Warrior": ["Stonewall", "Weapon Maker", "Weapon Master"],
        "Seer": ["Death Visions", "Sudden Visions", "Totem Maker"],
        "Scavenger": ["Hideout", "Scrounger", "Weapons Collector"],
        "Battle Robot": ["Command Override", "IR Camera", "Robot Anatomy"],
        "Cleaning Robot": ["Rubberized", "Trash Blower", "Waste Recycler"],
        "Companion Robot": ["Appearance Morph", "Human Features", "Infiltrator"],
        "Coordination Robot": ["Battle Commander", "Swat Tactics", "Top-Tier Unit"],
        "Industrial Robot": ["Mass Production", "Mounted Tools", "Resistant"],
        "Protocol Robot": ["Coordination Support", "Interpreter", "Ultimate Clerk"],
        "Scrap Robot": ["Chopping Tool", "Dummy Modules", "Scrap Companion"],
        "Security Robot": ["Armlock", "Command Override", "Sirens"]

    }
    professionskills = {
        "Investigator": "Investigate",
        "Officer": "Command",
        "Procurator": "Prosecute",
        "Scholar": "Enlighten",
        "Soldier": "Press On",
        "Technician": "Tinker",
        "Enforcer": "Intimidate",
        "Gearhead": "Jury-Rig",
        "Stalker": "Find the Path",
        "Fixer": "Make a Deal",
        "Dog Handler": "Sic a Dog",
        "Chronicler": "Inspire",
        "Boss": "Command",
        "Slave": "Shake it Off",
        "Healer": "Brew Potions",
        "Hunter": "Hunt",
        "Warrior": "Measure Enemy",
        "Seer": "Scry",
        "Scavenger": "Scavenge",
        "Battle Robot": "Target",
        "Cleaning Robot": "Clean",
        "Companion Robot": "Manipulate",
        "Coordination Robot": "Coordinate",
        "Industrial Robot": "Manufacture",
        "Protocol Robot": "Calculate",
        "Scrap Robot": "Recycle",
        "Security Robot": "Protect"
    }
    ages = ["Young", "Middleaged", "Old"]
    elyageattribute = {
        "Young": [3, 16, 8, 1],
        "Middleaged": [4, 15, 11, 2],
        "Old": [5,  14, 14, 3]
    }
    labageattribute = {
        "Young": [2, 15, 8, 2],
        "Middleaged": [4, 14, 10, 2],
        "Old": [6,  13, 12, 2]
    }
    coreageattribute = {
        "Young": [0, 14, 10, 1]
    }
    attributes = {
        "Strength": 2,
        "Agility": 2,
        "Wits": 2,
        "Empathy": 2,
    }
    skills = {
        "Endure": 0,
        "Force": 0,
        "Fight": 0,
        "Sneak": 0,
        "Move": 0,
        "Shoot": 0,
        "Scout": 0,
        "Comprehend": 0,
        "Know the Zone": 0,
        "Sense Emotion": 0,
        "Manipulate": 0,
        "Heal": 0
    }
    reputationstart = {
        "Investigator": 0,
        "Officer": 2,
        "Procurator": 1,
        "Scholar": 1,
        "Soldier": 0,
        "Technician": 0,
        "Seer": 3,
        "Warrior": 2,
        "Healer": 1,
        "Hunter": 0,
        "Scavenger": -1,
        "Battle Robot": 2,
        "Cleaning Robot": 1,
        "Coordination Robot": 5,
        "Escort Robot": 1,
        "Industrial Robot": 2,
        "Protocol Robot": 3,
        "Security Robot": 4,
        "Companion Robot": 1,
        "Scrap Robot": 0
    }
    charactertypes = ["mutant", "animal", "human", "robot"]
    traitchoices = []
    charactertraits = []
    firstname = ""
    lastname = ""
    present = "False"
    def clear(): return os.system('cls')

    def Generatefirst(charactertype):
        if charactertype == "animal":
            firstnamelist = random.choice(list(labfirstnames.values()))
            firstname = firstnamelist[random.randint(
                0, len(firstnamelist) - 1)]
        elif charactertype == "human":
            print("Bro, what the fuck?")
            quit()
        elif charactertype == "mutant":
            firstname = corefirstnames[random.randint(
                0, len(corefirstnames) - 1)]
        elif charactertype == "robot":
            firstname = mechfirstnames[random.randint(
                0, len(mechfirstnames) - 1)]

        return firstname

    def Generatelast(charactertype):
        if charactertype == "animal":
            lastname = random.randint(1, 99)
        if charactertype == "robot":
            randletters = ''.join(random.choice(string.ascii_uppercase)
                                  for x in range(3))
            randnumbers = str(random.randint(100, 999))
            lastname = randletters + "-" + randnumbers
        if charactertype == "mutant":
            lastname = ""
        return lastname

    def Genelysfirst(highorlow):
        if highorlow == 1:
            firstname = elyfirstlowername[random.randint(
                0, len(elyfirstlowername) - 1)]
        elif highorlow == 2:
            firstname = elyfirstnoblenames[random.randint(
                0, len(elyfirstnoblenames) - 1)]
        return firstname

    def Genelylast(highorlow):
        if highorlow == 1:
            lastname = lowerhouses[random.randint(0, len(lowerhouses) - 1)]
        if highorlow == 2:
            lastname = houses[random.randint(0, len(houses) - 1)]
        return lastname

    def Generateage():
        age = ages[random.randint(0, len(ages) - 1)]
        return age

    def Generateprofession(charactertype):
        profession = professions[random.randint(0, len(professions) - 1)]
        professions.remove(profession)
        skills[professionskills[profession]] = 1
        traitchoices.extend(professiontraits[profession])
        pickedtrait = random.randint(0, len(traitchoices) - 1)
        charactertraits.append(traitchoices[pickedtrait])
        del traitchoices[pickedtrait]

        return profession

    def Calculaterep(agevalues, profession):
        reputation = agevalues[0] + reputationstart[profession]
        return reputation

    def Appendtraitchoices(charactertype):
        bookchoices = ["Elysium", "Genlabalpha", "Core"]
        selectedbooks = []
        if charactertype == "robot":
            bookchoices.append("Mechatron")
        while len(bookchoices) > 0:
            clear()
            print("Current options are:")
            print("----")
            for x in bookchoices:
                print(x)
            # print(*bookchoices)
            if len(selectedbooks) > 0:
                print("----")
                print("Enabled books:")
                for x in selectedbooks:
                    print(x)
            print("----")
            bookchosen = input(
                "Please chose which book you'd like to pull traits from! (Press enter with no choice to stop adding books. Adding no books only allows for career traits.): ")
            bookchosen = bookchosen.lower()
            bookchosen = bookchosen.capitalize()
            if bookchosen == "":
                return
            else:
                for i in range(len(bookchoices)):
                    if bookchoices[i] == bookchosen:
                        present = "True"
                        break
                    else:
                        present = "False"
                        continue
                if present == "True":
                    if bookchosen == "Elysium":
                        traitchoices.extend(elygeneraltraits)
                    if bookchosen == "Genlabalpha":
                        traitchoices.extend(labgeneraltraits)
                    if bookchosen == "Core":
                        traitchoices.extend(coregeneraltraits)
                    if bookchosen == "Mechatron":
                        traitchoices.extend(mechgeneraltraits)
                    selectedbooks.append(bookchosen)
                    bookchoices.remove(bookchosen)
                elif present != "True":
                    print(
                        "Sorry! That book isn't present or you already chose that one. Please try again!")
                present = "False"
        if charactertype == "robot":
            traitchoices.extend(mechgeneraltraits)

    def GenAttributes(agevalues, charactertype):
        points = agevalues[1] - 8
        if charactertype == "animal":
            attributes["Instinct"] = attributes["Empathy"]
            del attributes["Empathy"]
        while(points > 0):
            tobeincremented = random.choice(list(attributes.keys()))
            if(attributes[tobeincremented] == 5):
                continue
            attributes[tobeincremented] = attributes[tobeincremented] + 1
            points = points - 1

    def GenSkills(agevalues, charactertype):
        skillpoints = agevalues[2] - 1
        if charactertype == "robot":
            skills["Overload"] = skills["Endure"]
            del skills["Endure"]
            skills["Force"] = skills["Force"]
            del skills["Force"]
            skills["Assault"] = skills["Fight"]
            del skills["Fight"]
            skills["Infiltrate"] = skills["Sneak"]
            del skills["Sneak"]
            skills["Move"] = skills["Move"]
            del skills["Move"]
            skills["Scan"] = skills["Scout"]
            del skills["Scout"]
            skills["Datamine"] = skills["Comprehend"]
            del skills["Comprehend"]
            skills["Analyze"] = skills["Know the Zone"]
            del skills["Know the Zone"]
            skills["Question"] = skills["Sense Emotion"]
            del skills["Sense Emotion"]
            skills["Interact"] = skills["Manipulate"]
            del skills["Manipulate"]
            skills["Repair"] = skills["Heal"]
            del skills["Heal"]
        if charactertype == "animal":
            skills["Dominate"] = skills["Manipulate"]
            del skills["Manipulate"]
        while(skillpoints > 0):
            tobeincremented = random.choice(list(skills.keys()))
            if(skills[tobeincremented] == 3):
                continue
            skills[tobeincremented] = skills[tobeincremented] + 1
            skillpoints = skillpoints - 1

    def Levelup(Levels):
        while Levels > 0:
            skillortrait = random.randint(1, 2)
            if skillortrait == 1:
                tobeincremented = random.choice(list(skills.keys()))
                if(skills[tobeincremented] == 5):
                    continue
                skills[tobeincremented] = skills[tobeincremented] + 1
            if skillortrait == 2:
                if len(traitchoices) > 0:
                    pickedtrait = random.randint(0, len(traitchoices) - 1)
                    charactertraits.append(traitchoices[pickedtrait])
                    if traitchoices[pickedtrait] == "Jack of All Trades":
                        if len(charactertraits) < 3:
                            continue
                        else:
                            profession = professions[random.randint(
                                0, len(professions) - 1)]
                            skills[professionskills[profession]] = 1
                            traitchoices.extend(professiontraits[profession])
                    del traitchoices[pickedtrait]
            Levels = Levels - 1

    def presentation(age, firstname, lastname, profession, charactertype, Levels, skills, attributes, charactertraits, agevalues, reputation):
        clear()
        print(
            f"My name is {firstname} {lastname} and I am a {charactertype}")
        print(f"I am a {profession} and I am level {Levels}")
        if charactertype != "robot":
            print(f"I am a {age.lower()} {charactertype}")
        if charactertype == "animal" or charactertype == "human":
            print(f"My reputation is {reputation}")
        if charactertype == "robot":
            print(f"My hierarchy is {reputation}")
        print("----")
        print("My attributes are:")
        for attribute in attributes:
            print(f"{attribute}: {attributes[attribute]}")
        print("----")
        print(f"{firstname} {lastname} has dice in:")
        for skill in skills:
            if skills[skill] > 0:
                print(f"{skill}: {skills[skill]}")
        print("----")
        print("My traits are:")
        for trait in charactertraits:
            print(f"{trait}")
        print("----")
        if charactertype == "animal":
            print("I start with 2 animal powers, or 1 animal power and 1 mutation!")
        if charactertype == "human":
            print(
                f"I start with {agevalues[3]} contacts, or 0 contacts and 1 mutation")
        if charactertype == "mutant":
            print(
                f"I start with {agevalues[3]} mutations, or 2 mutations at the cost of 1 attribute point!")
        if charactertype == "robot":
            print(
                "Please manage my armor pieces and modules seprately from my generation!")
        print("----")
        print("If you liked this generator, please give kudos, kind messages and upvotes to r/RedRuttinRabbit and r/MutantYearZero!")
        print("Me: https://www.reddit.com/user/RedRuttinRabbit")
        print("r/MutantYearZero: https://www.reddit.com/r/mutantyearzero/")

    def save(age, firstname, lastname, profession, charactertype, Levels, skills, attributes, charactertraits, agevalues, reputation):
        firstname = str(firstname)
        lastname = str(lastname)
        filename = firstname + lastname + ".txt"
        with open(filename, 'w') as f:
            f.write("My name is " + firstname + " " +
                    lastname + " and I am a " + charactertype)
            f.write('\n')
            f.write("I am a " + profession + " and I am level " + str(Levels))
            f.write('\n')
            if charactertype != "robot":
                f.write("I am a " + str(age.lower()) + " "+ charactertype)
                f.write('\n')
            if charactertype == "animal" or charactertype == "human":
                f.write("My reputation is " + str(reputation))
                f.write('\n')
            if charactertype == "robot":
                f.write("My hierarchy is " + str(reputation))
                f.write('\n')
            f.write("----")
            f.write('\n')
            f.write("My attributes are:")
            f.write('\n')
            for attribute in attributes:
                f.write(attribute + ": " + str(attributes[attribute]))
                f.write('\n')
            f.write("----")
            f.write('\n')
            f.write(firstname + " " + lastname + " has dice in:")
            f.write('\n')
            for skill in skills:
                if skills[skill] > 0:
                    f.write(skill + ": " + str(skills[skill]))
                    f.write('\n')
            f.write("----")
            f.write('\n')
            f.write("My traits are:")
            f.write('\n')
            for trait in charactertraits:
                f.write(trait)
                f.write('\n')
            f.write("----")
            f.write('\n')
            if charactertype == "animal":
                f.write(
                    "I start with 2 animal powers, or 1 animal power and 1 mutation!")
                f.write('\n')
            if charactertype == "human":
                f.write(
                    f"I start with " + str(agevalues[3]) + " contacts, or 0 contacts and 1 mutation")
                f.write('\n')
            if charactertype == "mutant":
                f.write(
                    f"I start with " + str(agevalues[3]) + " mutations, or 2 mutations at the cost of 1 attribute point!")
                f.write('\n')
            if charactertype == "robot":
                f.write(
                    "Please manage my armor pieces and modules seprately from my generation!")
                f.write('\n')
            f.write("----")
            f.write('\n')
            f.write("If you liked this generator, please give kudos, kind messages and upvotes to r/RedRuttinRabbit and r/MutantYearZero!")
            f.write('\n')
            f.write("Me: https://www.reddit.com/user/RedRuttinRabbit")
            f.write('\n')
            f.write("r/MutantYearZero: https://www.reddit.com/r/mutantyearzero/")

    print("Hello! Welcome to r/RedRuttinRabbit's MYZ NPC/PC Generator!")
    print("---")
    #print("Your options are:")
    #print("Random (or press enter) - Generate a random character")
    #print("Manual - Generate a character given manual attributes. You can press enter at any time for a random value.")
    #choice = input("Enter your choice: ")
    #choice = choice.lower()
    choice = "random"
    if choice == "random" or choice == "":
        while True:
            charactertype = input(
                "What kind of character are you making? A human, animal, robot, mutant or RANDOM? (Just press enter with nothing inputed for random!): ")
            charactertype = charactertype.lower()
            if charactertype == "":
                x = random.randint(0, len(charactertypes)-1)
                charactertype = charactertypes[x]
                break
            if charactertype == "human" or charactertype == "animal" or charactertype == "robot" or charactertype == "mutant":
                break
            else:
                print(
                    "Incorrect input. Please type 'human' 'animal' 'robot' 'mutant' or nothing at all")
                continue
        if charactertype == "mutant":
            professions = ["Enforcer", "Gearhead", "Stalker",
                           "Fixer", "Dog Handler", "Chronicler", "Boss", "Slave"]
        if charactertype == "animal":
            professions = ["Healer", "Hunter", "Warrior", "Seer", "Scavenger"]
        if charactertype == "human":
            professions = ["Investigator", "Officer",
                           "Procurator", "Scholar", "Soldier", "Technician"]
        if charactertype == "robot":
            professions = ["Battle Robot", "Cleaning Robot", "Companion Robot", "Coordination Robot",
                           "Industrial Robot", "Protocol Robot", "Scrap Robot", "Security Robot"]
        if charactertype == "human":
            highorlow = random.randint(1, 2)
            firstname = Genelysfirst(highorlow)
            lastname = Genelylast(highorlow)
        else:
            firstname = Generatefirst(charactertype)
            lastname = Generatelast(charactertype)
        if charactertype == "human" or charactertype == "animal":
            age = Generateage()
        else:
            age = "Young"
        if charactertype == "human":
            agevalues = elyageattribute[age]
        elif charactertype == "animal":
            agevalues = labageattribute[age]
        elif charactertype == "mutant":
            agevalues = coreageattribute[age]
        elif charactertype == "robot":
            agevalues = [0, 0, 10, 0, 0]
        profession = Generateprofession(charactertype)
        if charactertype == "animal" or charactertype == "robot" or charactertype == "human":
            reputation = Calculaterep(agevalues, profession)
        else:
            reputation = 0
        Appendtraitchoices(charactertype)
        if charactertype != "robot":
            GenAttributes(agevalues, charactertype)
        GenSkills(agevalues, charactertype)
        flag = "False"
        while flag == "False":
            clear()
            decision = input(
                "What level would you like your character? (0-20) Enter nothing for random: ")
            if decision == "":
                Levels = random.randint(0, 20)
                flag = "True"
                break
            try:
                decision = int(decision)
            except:
                print("You didn't enter a number!")
                continue
            if decision > -1 and decision < 21:
                Levels = decision
                flag = "True"
                break
            else:
                print("Please enter a number between 0-20")

        if Levels > 0:
            Levelup(Levels)
        presentation(age, firstname, lastname, profession, charactertype,
                     Levels, skills, attributes, charactertraits, agevalues, reputation)
        while True:
            saveyn = input("Would you like to save your character?(y/n): ")
            saveyn = saveyn.lower()
            if saveyn == "n" or saveyn == "no":
                break
            elif saveyn == "y" or saveyn == "yes":
                save(age, firstname, lastname, profession, charactertype,
                     Levels, skills, attributes, charactertraits, agevalues, reputation)
                break
            else:
                print("Please try that again.")

        while True:
            exit = input("Would you like to run again? (y/n): ")
            exit = exit.lower()
            if exit == "y" or exit == "yes":
                clear()
                break
            elif exit == "n" or exit == "no":
                quit()
            else:
                print("Please try again.")

    # elif choice == "manual":
        # while True:
        # charactertype = input(
        #      "What kind of character are you making? A human, animal, robot, mutant or RANDOM? (Just press enter with nothing inputed for random!): ")
        #  charactertype = charactertype.lower()
        #  if charactertype == "":
        #     x = random.randint(0, len(charactertypes)-1)
        #      charactertype = charactertypes[x]
        #      break
        #  if charactertype == "human" or charactertype == "animal" or charactertype == "robot" or charactertype == "mutant":
        #        break
        #   else:
        #       print(
        #            "Incorrect input. Please type 'human' 'animal' 'robot' 'mutant' or nothing at all")
        #       continue
        #print("In manual mode, you can just press 'enter' at any point and make a random values instead!")
    # decision = input("First name?: ")
        # if decision == "":
        #    if charactertype == "human":
        #        highorlow = random.randint(1, 2)
        #        firstname = Genelysfirst(highorlow)
        #    else:
        #        firstname = Generatefirst(charactertype)
        # else:
        #    firstname = decision
        # if charactertype != "mutant":
        #decision = input("Last name?: ")
        # if decision == "":
        #   if charactertype == "human":
        #        lastname = Genelylast(highorlow)
        #     else:
        #          lastname = Generatelast(charactertype)
        #   else:
        #        lastname = decision
        # if charactertype != "robot" or charactertype != "mutant":
        # flag = "False"
        # while flag == "False":
        #  decision = input(
        #       "How old is your character? Young, Middleaged or Old: ")
        #    decision = decision.lower()
        #     decision = decision.capitalize()
        #          age = decision
        #          flag = "True"
        #          break
        #       print("Please try again")
        #       continue
        # if charactertype == "mutant":
    #     professions = ["Enforcer", "Gearhead", "Stalker",
        #                   "Fixer", "Dog Handler", "Chronicler", "Boss", "Slave"]
        # if charactertype == "animal":
        #    professions = ["Healer", "Hunter", "Warrior", "Seer", "Scavenger"]
        # if charactertype == "human":
        #    professions = ["Investigator", "Officer",
        #                   "Procurator", "Scholar", "Soldier", "Technician"]
        # if charactertype == "robot":
        #    professions = ["Battle Robot", "Cleaning Robot", "Companion Robot", "Coordination Robot",
    #                    "Industrial Robot", "Protocol Robot", "Scrap Robot", "Security Robot"]
        #print(f"Your {charactertype}'s class options are:")
        # for x in professions:
        #   print(x)
        #flag = "False"
        # while flag == "False":
        #  decision = input(f"What class is your {charactertype}?: ")
        #   for x in professions:
        #        if decision == x:
    #             flag = "True"
    #      print("That's not a recognized class, please try again.")
    #   if charactertype == "human":
    #       agevalues = elyageattribute[age]
    #   elif charactertype == "animal":
    #       agevalues = labageattribute[age]
    #   elif charactertype == "mutant":
    #       agevalues = coreageattribute[age]
    #   elif charactertype == "robot":
    #       agevalues = [0, 0, 10, 0, 0]
