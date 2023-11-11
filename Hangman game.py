import random
import time
import os

print('_____________________')
print('|           |')
print('|         [* *]')
print('|         [_=_]')
print('|     ______|______')
print('|          ||')
print('|          /\ ')
print('|         /  \ ')
print('|        /    \ ')

nrOfTries = 3
stop = False
za_sing = ''
cattetetogrorororeidesssss = ''
cheose = True
refresh = True
nochance = True
uncoprinto = True


animal_names = [
    "Lion", "Elephant", "Tiger", "Giraffe", "Penguin", "Kangaroo", "Dolphin", "Zebra",
    "Cheetah", "Gorilla", "Polar Bear", "Chimpanzee", "Koala", "Platypus", "Octopus", "Rhinoceros",
    "Hippopotamus", "Ostrich", "Sloth", "Puma", "Raccoon", "Flamingo", "Meerkat", "Komodo Dragon",
    "Lemur", "Tasmanian Devil", "Armadillo", "Chameleon", "Seahorse", "Narwhal", "Red Panda",
    "Warthog", "Eel", "Orangutan", "Albatross", "Woodpecker", "Vulture", "Gannet", "Otter", "Lynx",
    "Cheetah", "Antelope", "Walrus", "Python", "Cobra", "Jaguar", "Magpie", "Hummingbird", "Parrot",
    "Ocelot", "Dingo", "Mongoose", "Tapir", "Salamander", "Rattlesnake", "Marmoset", "Hammerhead Shark",
    "Walrus", "Grasshopper", "Starfish",
]
fruit_names = [
    "Apple", "Banana", "Cherry", "Orange", "Strawberry", "Watermelon", "Blueberry", "Grape",
    "Pineapple", "Mango", "Kiwi", "Peach", "Plum", "Lemon", "Lime", "Coconut",
    "Pear", "Grapefruit", "Cantaloupe", "Raspberry", "Blackberry", "Pomegranate", "Papaya", "Fig",
    "Guava", "Apricot", "Cranberry", "Passion Fruit", "Nectarine", "Lychee", "Dragon Fruit", "Starfruit",
    "Avocado", "Persimmon", "Honeydew", "Mandarin", "Tangerine", "Kumquat", "Clementine", "Durian",
    "Guava", "Cherimoya", "Mulberry", "Gooseberry", "Quince", "Currant", "Soursop", "Jackfruit",
    "Pawpaw", "Feijoa", "Salak", "Feijoa", "Kiwano", "Acai", "Bilberry", "Elderberry",
    "Rhubarb", "Carambola", "Miracle Fruit", "Blood Orange", "Plantain", "Date Palm", "Sapodilla", "Soursop",
]
country_names = [
    "United States", "Canada", "France", "Japan", "Australia", "Brazil", "Germany", "Italy",
    "Spain", "United Kingdom", "China", "India", "Russia", "South Korea", "Mexico", "Argentina",
    "Egypt", "Nigeria", "South Africa", "Kenya", "Greece", "Sweden", "Norway", "Turkey",
    "Thailand", "Indonesia", "Vietnam", "New Zealand", "Saudi Arabia", "Israel", "Pakistan", "Bangladesh",
    "Canada", "Mexico", "Argentina", "Peru", "Chile", "Colombia", "Venezuela", "Ecuador",
    "Moldova", "Algeria", "Tunisia", "Niger", "Senegal", "Mali", "Nepal", "Sri Lanka",
    "Iceland", "Switzerland", "Austria", "Poland", "Hungary", "Czech Republic", "Ukraine", "Romania",
    "Ireland", "Portugal", "Netherlands", "Belgium", "Denmark", "Finland", "Ireland", "Poland",
]
movie_names = [
    "Titanic", "Star Wars", "Avatar", "Jurassic Park", "The Matrix", "Inception", "Frozen", "Harry Potter",
    "The Shawshank Redemption", "Forrest Gump", "The Godfather", "Pulp Fiction", "Schindler's List", "The Dark Knight", "Fight Club", "Inglourious Basterds",
    "The Lord of the Rings", "The Lion King", "The Terminator", "Gladiator", "The Green Mile", "The Silence of the Lambs", "The Shining", "Goodfellas",
    "Braveheart", "American Beauty", "The Social Network", "Eternal Sunshine of the Spotless Mind", "The Grand Budapest Hotel", "La La Land", "Memento", "Casablanca",
    "Blade Runner", "The Sixth Sense", "Saving Private Ryan", "The Revenant", "Avatar", "The Avengers", "Iron Man", "Black Panther",
    "The Godfather: Part II", "One Flew Over the Cuckoo's Nest", "The Departed", "No Country for Old Men", "Shutter Island", "The Usual Suspects", "The Good, the Bad and the Ugly", "The Great Gatsby",
    "Interstellar", "The Matrix", "The Incredibles", "The Graduate", "Blazing Saddles", "Rocky", "The Exorcist", "A Clockwork Orange",
]
sports_names = [
    "Soccer", "Basketball", "Tennis", "Swimming", "Golf", "Cycling", "Volleyball", "Cricket",
    "Baseball", "Hockey", "Rugby", "Boxing", "Wrestling", "Badminton", "Table Tennis", "Fencing",
]
vegetable_names = [
    "Carrot", "Broccoli", "Potato", "Cucumber", "Spinach", "Pepper", "Lettuce", "Onion",
    "Tomato", "Zucchini", "Eggplant", "Cauliflower", "Cabbage", "Asparagus", "Mushroom", "Radish",
    "Pumpkin", "Sweet Potato", "Artichoke", "Green Bean", "Corn", "Celery", "Beet", "Kale",
    "Brussels Sprout", "Okra", "Squash", "Garlic", "Turnip", "Leek", "Pea", "Chard",
    "Rhubarb", "Bok Choy", "Watercress", "Endive", "Arugula", "Collard Greens", "Dill", "Parsley",
    "Thyme", "Basil", "Cilantro", "Rosemary", "Sage", "Oregano", "Mint", "Chives",
    "Ginger", "Scallion", "Fennel", "Horseradish", "Dandelion", "Parsnip", "Celeriac", "Jicama",
    "Kohlrabi", "Rutabaga", "Turnip", "Salsify", "Escarole", "Chicory", "Winter Melon", "Lotus Root",
]
color_names = [
    "Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Black"
]
instrument_names = [
    "Guitar", "Piano", "Violin", "Trumpet", "Drums", "Flute", "Saxophone", "Clarinet", "Harp", "Trombone",
    "Accordion", "Banjo", "Harmonica", "Xylophone", "Bagpipes", "Cello", "Oboe", "Ukulele", "Didgeridoo", "Theremin"
]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
languages = [
    "English", "Spanish", "French", "Chinese", "Arabic", "Russian", "German", "Japanese", "Portuguese", "Italian",
    "Dutch", "Swedish", "Korean", "Turkish", "Hindi", "Bengali", "Urdu", "Greek", "Polish", "Vietnamese",
    "Thai", "Hebrew", "Persian", "Swahili", "Finnish", "Hungarian", "Romanian", "Czech", "Danish", "Norwegian",
    "Indonesian", "Malay", "Filipino", "Dutch", "Swedish", "Korean", "Turkish", "Hindi", "Bengali", "Urdu", "Greek",
    "Polish", "Vietnamese", "Thai", "Hebrew", "Persian", "Swahili", "Finnish", "Hungarian", "Romanian", "Czech",
    "Danish", "Norwegian", "Indonesian", "Malay", "Filipino"
]
cars = [
    "Toyota", "Ford", "Honda", "Tesla", "BMW", "Mercedes", "Audi", "Chevrolet", "Lexus", "Subaru",
    "Volkswagen", "Hyundai", "Nissan", "Volvo", "Jeep", "Porsche", "Mazda", "Kia", "Jaguar", "Ferrari",
    "Land Rover", "Chrysler", "Mitsubishi", "Cadillac", "Dodge", "Acura", "Infiniti", "Bentley", "Rolls-Royce",
    "Maserati", "Mini Cooper", "Bugatti", "Lamborghini", "McLaren", "Aston Martin", "Lotus", "Alfa Romeo", "Fiat", "Buick",
    "Lincoln", "Maybach", "Ram", "Koenigsegg", "Pagani", "Genesis", "Karma", "Spyker", "Hennessey", "Scion",
    "Hummer", "Saturn", "Pontiac", "Saab", "Oldsmobile", "Geo", "Suzuki", "Isuzu", "Mercury"
]
professions = [
    "Doctor", "Teacher", "Firefighter", "Engineer", "Chef", "Artist", "Pilot", "Lawyer", "Nurse", "Accountant",
    "Police Officer", "Dentist", "Electrician", "Plumber", "Architect", "Mechanic", "Psychologist", "Journalist", "Pharmacist", "Scientist",
    "Veterinarian", "Farmer", "Librarian", "Paramedic", "Social Worker", "Banker", "Designer", "Barista", "Actor", "Musician",
    "Economist", "Geologist", "Photographer", "Biologist", "Astronomer", "Meteorologist", "Secretary", "Carpenter", "Fashion Designer", "Translator",
    "Surveyor", "Anthropologist", "Zoologist", "Linguist", "Historian", "Tour Guide", "Flight Attendant", "Landscaper", "Physicist", "Mathematician",
    "Dietitian", "Chiropractor", "Forester", "Park Ranger", "Air Traffic Controller", "Paramedic", "Orthodontist", "Speech Therapist", "Massage Therapist", "Radiologist"
]
books = [
    "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "The Lord of the Rings", "War and Peace", "Moby-Dick", "The Catcher in the Rye", "The Hobbit", "Brave New World",
    "The Grapes of Wrath", "Fahrenheit 451", "The Odyssey", "The Alchemist", "The Hitchhiker's Guide to the Galaxy", "The Chronicles of Narnia", "Wuthering Heights", "The Scarlet Letter", "A Tale of Two Cities", "The Picture of Dorian Gray",
    "One Hundred Years of Solitude", "Crime and Punishment", "Jane Eyre", "Frankenstein", "Dracula", "The Shining", "Lord of the Flies", "The Road", "The Name of the Wind", "The Giver",
    "The Hunger Games", "The Girl with the Dragon Tattoo", "The Help", "The Kite Runner", "The Secret Garden", "The Color Purple", "The Old Man and the Sea", "The Art of War", "The Stand", "The Time Traveler's Wife",
    "The Sun Also Rises", "The Bell Jar", "The Outsiders", "The Wind in the Willows", "The Jungle Book", "The Iliad", "The Odyssey", "Don Quixote", "The Canterbury Tales", "Les Misérables",
    "Walden", "The Divine Comedy", "The Republic", "The Prince", "Siddhartha", "Alice's Adventures in Wonderland", "The Little Prince", "Charlotte's Web", "The Call of the Wild", "Anne of Green Gables",
    "The Count of Monte Cristo", "Great Expectations", "A Christmas Carol", "Gulliver's Travels", "The Picture of Dorian Gray", "Treasure Island", "Around the World in Eighty Days", "The Three Musketeers", "Moby-Dick", "Pride and Prejudice"
]
holidays = [
    "Christmas", "Thanksgiving", "Halloween", "Easter", "Valentine's Day"
]
cities = [
    "Chisinau", "Paris", "Tokyo", "London", "Rome", "Sydney", "Beijing", "Moscow", "Cairo", "Dubai",
    "Los Angeles", "Chicago", "Toronto", "Madrid", "Berlin", "Rio de Janeiro", "Cape Town", "Amsterdam", "Bangkok", "Mumbai",
    "San Francisco", "Hong Kong", "Vienna", "Barcelona", "Lisbon", "Stockholm", "Buenos Aires", "Athens", "Prague", "Singapore",
    "San Francisco", "Seoul", "Kuala Lumpur", "Shanghai", "Riyadh", "Istanbul", "Dublin", "Oslo", "Warsaw", "Budapest",
    "Wellington", "Helsinki", "Lima", "Copenhagen", "Brussels", "Manila", "Nairobi", "Kiev", "Bucharest", "Zurich",
    "Vancouver", "Montreal", "Brisbane", "Perth", "Copenhagen", "Delhi", "Munich", "Marrakech", "Casablanca", "Jakarta",
]
food = [
    "Pizza", "Sushi", "Burger", "Pasta", "Ice Cream", "Taco", "Curry", "Sandwich", "Salad", "Steak",
    "Chicken", "Soup", "Rice", "Pancakes", "Omelette", "Cereal", "Bacon", "Donut", "Waffle", "Lasagna",
    "Burrito", "Fried Chicken", "Hot Dog", "Ramen", "Spaghetti", "Shrimp", "Lobster", "Sashimi", "Noodles", "Tofu",
    "Cheese", "Chocolate", "Cupcake", "Pretzel", "Popcorn", "Gyros", "Samosa", "Enchilada", "Sushi Roll", "Goulash",
    "Fish and Chips", "Peking Duck", "Calzone", "Clam Chowder", "Pumpkin Pie", "Peking Duck", "Baklava", "Dim Sum", "Beef Stroganoff", "Pad Thai",
    "Jambalaya", "Mango Sticky Rice", "Spare Ribs", "Ceviche", "Fajitas", "Chicken Alfredo", "Ratatouille", "Rack of Lamb", "Chow Mein", "Guacamole",
]
hobbies = [
    "Painting", "Gaming", "Reading", "Cooking", "Hiking", "Photography", "Swimming", "Dancing", "Singing", "Sculpting",
    "Fishing", "Gardening", "Meditation", "Biking", "Yoga", "Woodworking", "Knitting", "Camping", "Birdwatching", "Collecting",
    "Sudoku", "Crossword Puzzles", "Chess", "Pottery", "Golf", "Running", "Rock Climbing", "Surfing", "Traveling", "Billiards",
    "Astronomy", "Birdwatching", "Calligraphy", "Mountain Biking", "Kite Flying", "Wine Tasting", "Whale Watching", "Geocaching", "Metal Detecting", "Canoeing",
    "Kayaking", "Jigsaw Puzzles", "Cycling", "Paintball", "Scuba Diving", "Snorkeling", "Amateur Radio", "Beekeeping", "Skydiving", "Paragliding",
]
categories = [animal_names, fruit_names, hobbies, food, cities, holidays, books, professions, cars, languages,
               planets, instrument_names, color_names, vegetable_names, sports_names, movie_names]
categories2 = [
    "animal_names",  
    "fruit_names", 
    "hobbies",  
    "food", 
    "cities",  
    "holidays", 
    "books", 
    "professions",  
    "cars", 
    "languages",  
    "planets",  
    "instrument_names", 
    "color_names",  
    "vegetable_names",  
    "sports_names", 
    "movie_names"  
]
insults = ['asswipe', 'Fuck you', 'STUPID', 'Fucka', 'motherfucka', 'shitface', 'BITCH!', 'Stupid ahh' , 'dumb ass', 'Wan... nah, my bad meant to say you buffoon skallywag', 'poopyhead', 'Pussy', 'dickhead', 'hoe']


def EenyMeenyMinyMoeTheWord():
    intobinto = random.randint(0, len(categories) - 1)
    global za_sing
    global cattetetogrorororeidesssss
    worooreoerorerrroed = categories[intobinto]
    cattetetogrorororeidesssss = categories2[intobinto]
    za_sing = worooreoerorerrroed[random.randint(0, len(worooreoerorerrroed) - 1)]
    
EenyMeenyMinyMoeTheWord()
    
    
     

while not stop:
    
    if(refresh == True):
     os.system('cls') 
     print('_____________________')
     print('|           |')
     print('|         [* *]')
     print('|         [_=_]')
     print('|     ______|______')
     print('|          ||')
     print('|          /\ ')
     print('|         /  \ ')
     print('|        /    \ ')
    
    if(uncoprinto == True):
       somtang = '_' * len(za_sing)
       uncoprinto = False
       
    if(cheose == True):
       print(f'category is {cattetetogrorororeidesssss}')
       print(f'{somtang}   number of tries: {nrOfTries}')
       
       x = input()

    if(nrOfTries > 0):
     if(x.lower() == za_sing.lower()): 
        print('correct')
        EenyMeenyMinyMoeTheWord()
        uncoprinto = True
     elif(x.lower() != za_sing.lower()):
        print('nuh uh')
        lettatbereveal = random.randint(0, len(somtang) - 1)
        somtang = somtang[:lettatbereveal] + za_sing[lettatbereveal] +somtang[lettatbereveal + 1:]
        nrOfTries = nrOfTries - 1
    

    elif(nrOfTries == 0 or nrOfTries < 0):
       if(nochance == True):
        print(f'the word was {za_sing}')
        print('game over')
        print('wanna try again... PUSSY!? Y/N')
        again = input()
       if(again == 'Y'):
          nrOfTries = 3
          cheose = True
          EenyMeenyMinyMoeTheWord()
          uncoprinto = True
       elif(again == 'N'):
          print('HAHAHAHAHAHA!PUSSY! fack ouf meit!')
          cheose = False

    if(cheose == False):
       refresh = False
       nochance = False
       print(insults[random.randint(0, len(insults) - 1)])
    time.sleep(1)


    

