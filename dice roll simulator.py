x="y"
while (x=="y"):
    import random
    print("this is dice rolling game:")
    print("press enter to roll dice")
    input()
    num=random.randint(1,6)
    if num==1:
        print("[----------------------------]")
        print("[                            ]")
        print("[             o              ]")
        print("[                            ]")
        print("[----------------------------]")
    if num==2:
        print("[-----------------------------]")
        print("[                             ]")
        print("[            o   o            ]")
        print("[                             ]")
        print("[-----------------------------]")
    if num==3:
        print("[-----------------------------]")
        print("[              o              ]")
        print("[                             ]")
        print("[          o       o          ]")
        print("[-----------------------------]")
    if num==4:
        print("[-----------------------------]")
        print("[           o     o           ]")
        print("[                             ]")
        print("[           o     o           ]")
        print("[-----------------------------]")
    if num==5:
        print("[-----------------------------]")
        print("[           o     o           ]")
        print("[              o              ]")
        print("[           o     o           ]")
        print("[-----------------------------]")
    if num==6:
        print("[-----------------------------]")
        print("[           o     o           ]")
        print("[           o     o           ]")
        print("[           o     o           ]")
        print("[-----------------------------]")
    
