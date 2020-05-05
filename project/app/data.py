"""
Mocking data for testing
"""

from pathlib import Path
from flask import current_app

class Item:
    def __init__(self, name,price,desc,image):
        self.name = name
        self.price=price,
        self.desc=desc,
        self.image = str(image)

items_data = [
    Item(**dict(
        name='Jojoba Oil',
        price=9.32,
        desc="""Nutrient dense antioxidants heal blemishes, chapped dry skin, rashes, beard care, stretch marks, sun spot damage, plus is a makeup remover, acne infection treatment & more.
Made in the USA - Absorbs into the skin with no additives or parabens and non-GMO for maximum healing anti-inflammatory benefits. Fragrance free and Kosher friendly.
Great for Hair, Skin & Nails - Use to help treat acne, cysts, blisters, psoriasis, rosacea, eczema, candidiasis, rashes, keratosis, keloid dermatitis, calluses, corns, shingles, sunburn and more.
Nothing Added Or Taken Away - Dark amber bottle with glass dropper extends shelf life as oils are light sensitive & must be stored in dark amber bottles to protect organics from oxidation.
Apply externally to ankles, arms, backs, chests, stretched earlobes, elbows, knees, cuticles, heels, hands, head and scalp, hair follicles, fingernails, toenails, eyelashes, eyebrows, face, pores, forehead, cheek, chin, lips, forearms, shoulders, knuckles, shins, wrinkles & more.""",
        image='oil.jpg'
    )),
    Item(**dict(
        name='First Alert',
        price=28.00,
        desc="""Keep your family safe with this hardwired smoke and carbon monoxide alarm; The battery backup means constant monitoring, even if there's a power failure
Features an electrochemical Carbon Monoxide sensing technology as well as an ionization sensor for smoke detection.
Indicator lights on the face of the unit display the presence of smoke or carbon monoxide, while an 85 decibel siren provides a clear, loud warning upon detection
Can connect to other compatible BRK or First Alert detectors, to ensure all alarms will sound when threat is detected
Simple to use, with a single test/silence button, and side load battery compartment; tamper resistant locking brackets and universal mounting brackets make installation easy
Rigorously tested to meet UL standards
Faster turnarounds on job sites with the easy-to-install, most-trusted alarms in home safety
First Alert has been the most trusted brand in home safety since launching the first residential smoke alarm in 1958 (Based on a First Alert Brand Trust Survey in February 2018)""",
        image='alert.jpg'
    )),
    Item(**dict(
        name="Outdoor Security Camera Wireless",
        price=50.99,
        desc="""100% Wireless and Cordless : This outdoor security camera built-in 6400mAh rechargeable battery and Wi-Fi connected, the installation and the connection of security camera are 100% wireless, which gives you the added convenience of not having to deal with any outlets or tangled mess of wires.
Easy to Install and Use : This battery powered security camera takes less than 5 minutes to set up without having to use any complicated tools. You can install anywhere using an adjustable mounting bracket. Download Vicoo App on Google Play/App Store, friendly App operation can help you use it quickly.
1080P Full HD and Night Vision : Wireless security camera can be used both outdoors and indoors, it monitors your home in 1080HD video with infrared night vision and Live View. It maintains a 122 Degree Wide View Angle and offers two-way audio talk to let you easily hold conversations.
Advanced AI Events Detection : XTU home security camera system featuring motion detection, sound detection and face detection that captures video when it detects any type of activity and send instant alerts to your phone via app. You also can customize motion zone to reduce false alarms. Know your home situation anytime and anywhere.
Secure Cloud Storage and Local Storage : Security camera adopt financial encryption, support up to 128G Micro SD(NOT included) storage and Cloud storage. You’ll never miss out on a moment with remote and playback video with the encrypted Cloud service wherever you are.""",
        image='camera.jpg'
    )),
    Item(**dict(
        name="Juicer Machines",
        price=106.99,
        desc="""First, it turns a high volume of whole fruits and veggies into a glass of juice,You get the nutrients you need without having to eat a big bunches of leaves, roots, and fruits.

Second, since the juice is highly concentrated in vitamins and nutrients and is deprived of most of the fiber, the digestion happens with much more ease and at a much faster speed.

Top benefits of a juice:
Vitamin Supplementation
Promote Digestion
Improve Appetite
Strengthen Immunity
Bodybuilding and Weight-reducing""",
        image='machine.jpg'
    )),
    Item(**dict(
        name="Lavemi Men's Real Leather Ratchet Dress Belt",
        price=15.29,
        desc="""TRIM TO FIT - You can trim the strap length by yourself to fit your size if the belt strap is too long for you.
NO MORE HOLES - Lavemi's Fashion Ratchet Belt provides 38 unique adjustments for a superb comfortable fit. Easy removable buckle allows you to cut the belt to your ideal size to give a primmer and custom tailored appearance!
EASY USE - Just slide the belt into the buckle and pull the belt through, the buckle simply auto locks the belt, to release the belt, gently push the lever on the side of the buckle and lock will snap. Simple, smooth and sleek!
MAXIMUM DURABILITY - Leather strap is a bit wider than 1 2/5" presenting the perfect look of a fine, genuine leather quality belt, complemented with an HIGHLY FASHIONABLE stylish, buckle that is elegantly designed with class. Scratch resistant buckles made to last.
GIFT BOX - Make a big impression! Enclosed in a lovely, attractive gift box.""",
        image='belt.jpg'
    ))
]
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
users_data = [
    User(**dict(
        username='test',
        password='test'
    ))
]