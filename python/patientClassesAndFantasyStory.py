# Problem 1
print("\n\nProblem 1 \n\n")

# Part 1


class Patient:
    
    def __init__(self,lastName,social):
        self.name = lastName
        self.SSN = social
        
    def __str__(self):
        return (self.name + ',' + str(self.SSN))

# Part 2
    
class PatientQueue:
    
    def __init__(self):
        self.p1 = []
        self.p2 = []
        self.p3 = []
        
# Part 3
    
    def add(self, patient, priority):
        if priority == 1 : 
            self.p1.append(patient)
        elif priority == 2 : 
            self.p2.append(patient)
        else:
            self.p3.append(patient)

# Part 4

    def nextPatient(self):
        patientNow = 'No Patient'
        if self.p1 != [] :
            patientNow = self.p1[0]
            self.p1.pop(0)
        elif self.p2 != []:
            patientNow = self.p2[0]
            self.p2.pop(0)
        elif self.p3 != []:
            patientNow = self.p3[0]
            self.p3.pop(0)
        return patientNow
   
# Part 5
    
    def __str__(self):
        s  = ''
        s1 = ''
        s2 = ''
        s3 = ''
        s1list=[]
        s2list=[]
        s3list=[]
        for e in self.p1:
            # s1 += e.__str__() + '; '
            s1list.append(e.__str__())
        s1 = '; '.join(s1list) 
        # s1 = s1[:-2]
        s1 = 'p1: [' + s1 + ']'
        for e in self.p2:
            s2list.append(e.__str__())
            # s2 += e.__str__() + '; '
        # s2 = s2[:-2]
        s2 = '; '.join(s2list) 
        s2 = 'p2: [' + s2 + ']'
        for e in self.p3:
            s3list.append(e.__str__())
            # s3 += e.__str__() + '; '
        # s3 = s3[:-2]
        s3 = '; '.join(s3list) 
        s3 = 'p3: [' + s3 + ']'
        s = '\n'+ s1 + '\n' + s2 + '\n' + s3 
        return s
    
    
Paul = Patient("Allen",753265)
Marion = Patient("Raffi",435654)
Kalima = Patient("Aribi",873451)
Ann = Patient("Chang",771124)
Lee = Patient("Strong",113246)
p = PatientQueue()
print(p)
p.add(Paul,3)
p.add(Marion,2)
p.add(Kalima,1)
p.add(Ann,3)
p.add(Lee,1)
print(p)
for i in range(5):
    print("\nNext patient:", p.nextPatient())
    print("\nPatient list:", p)
    
# Problem 2
print("\n\nProblem 2 \n\n")

# Part 1
import random

class childsStory:
    
    def __init__(self):        
        self.hero = input('\nName the hero of the story.\n')
        self.location = input('\nName the location of the story.\n')
        self.allDescriptions = {'listLocations'            : ['caves', 'forests', 'hills', 'mountains', 'lakes'],
                                'listGoodObjects'          : ['lost treasure', 'mystical doll', 'dragon ball', 'magic flute', 'enchanted cape'],
                                'listbadGuys'              : ['dragon', 'troll', 'Wendigo','Bigfoot' ,  'gangsters', 'raiders'],
                                'listBadGuyObjectActions'  : ['take','steal','escape with','hide','destroy'],
                                'listGoodGuyObjectActions' : ['save','find','rescue','search for','recover'],
                                'listActionOnBadGuys'      : ['battle', 'attack','face','confront','deal with'],
                                'listWeaponsHero'          : ['sword', 'axe','wand','katana','nunchuks'],
                                'listWeaponsBadGuy'        : [], # Potential future story improvement
                                'listWeaponAdject'         : ['powerful','giant', 'golden','sharp','devastating'],
                                'listDefeatVerbs'          : ['destroy','decimate','obliterate','annihilate'],
                                'listGoodPeople'           : ['King', 'princess','towns people','villagers','students','forest creatures'],
                                'listGoodEndingVerbs'      : ['hailed','lauded','cheered','raised in victory','rewarded'],
                                'listBadEndingVerbs'       : ['leave','run away','escape','split'] ,
                                'listOfEndings'            : ['good', 'bad'] # Can add different endings to list, requires more list of descriptive words
                                }

    def randomise(self,l):
        lenList = len(l)
        r = random.randrange(0,lenList)
        return r
        
    def getAllDescriptions(self):
        print(self.allDescriptions)
        
    def setAllDescriptions(self, newKey, newValue):
        self.allDescriptions[newKey] = newValue
        
    def makeStory(self):
        self.locationType         = self.allDescriptions['listLocations'][self.randomise(self.allDescriptions['listLocations'])]
        self.goodObject           = self.allDescriptions['listGoodObjects'][self.randomise(self.allDescriptions['listGoodObjects'])]
        self.badGuy               = self.allDescriptions['listbadGuys'][self.randomise(self.allDescriptions['listbadGuys'])]
        self.badGuyObjectActions  = self.allDescriptions['listBadGuyObjectActions'][self.randomise(self.allDescriptions['listBadGuyObjectActions'])]
        self.actionOnBadGuys      = self.allDescriptions['listActionOnBadGuys'][self.randomise(self.allDescriptions['listActionOnBadGuys'])]
        self.weaponAdject         = self.allDescriptions['listWeaponAdject'][self.randomise(self.allDescriptions['listWeaponAdject'])]
        self.weaponsHero          = self.allDescriptions['listWeaponsHero'][self.randomise(self.allDescriptions['listWeaponsHero'])]
        self.defeatVerbs          = self.allDescriptions['listDefeatVerbs'][self.randomise(self.allDescriptions['listDefeatVerbs'])]
        self.goodEndingVerbs      = self.allDescriptions['listGoodEndingVerbs'][self.randomise(self.allDescriptions['listGoodEndingVerbs'])]
        self.goodPeople           = self.allDescriptions['listGoodPeople'][self.randomise(self.allDescriptions['listGoodPeople'])]
        self.badEndingVerbs       = self.allDescriptions['listBadEndingVerbs'][self.randomise(self.allDescriptions['listBadEndingVerbs'])]
        self.goodGuyObjectActions = self.allDescriptions['listGoodGuyObjectActions'][self.randomise(self.allDescriptions['listGoodGuyObjectActions'])]
        self.ending               = self.allDescriptions['listOfEndings'][self.randomise(self.allDescriptions['listOfEndings'])]
         
    def __str__(self):       
        self.makeStory()
        s = ('\nIn the ' + self.locationType + ' of ' + self.location + ', there was a ' + self.goodObject + ' that belonged to the ' + self.goodPeople + '.')
        s += ('\nThe ' + self.badGuy + ' wanted to ' + self.badGuyObjectActions + ' the ' + self.goodObject + '.')
        s += ('\n' + self.hero + ' decided to ' + self.goodGuyObjectActions + ' the ' + self.goodObject + ' and ' + self.actionOnBadGuys + ' the ' + self.badGuy + '.')
        s += ('\n' + self.hero + ' used his ' + self.weaponAdject + ' ' + self.weaponsHero + ' to ' + self.defeatVerbs + ' the ' + self.badGuy + '.')
        if self.ending == 'good' : # Add more endings with elif statements
            s += ('\n' + self.hero + ' saved the ' + self.goodObject + ' and was ' + self.goodEndingVerbs + ' by the ' + self.goodPeople + '.')
        else:
            s += ('\nBut ' + self.hero + ' was defeated by the ' + self.badGuy + ', and decided to ' + self.badEndingVerbs + ' and improve his skills to try again another day.')
        return s

story1 = childsStory()

print(story1)