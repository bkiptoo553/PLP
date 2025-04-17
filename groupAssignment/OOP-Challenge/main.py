from pet import Pet

def main():
    my_pet = Pet("simba")

    my_pet.get_status()

    my_pet.eat()
    my_pet.get_status()

    my_pet.play()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    
    my_pet.train("sit")
    my_pet.train("fetch")
    my_pet.train("sit")  

    my_pet.show_tricks()

main()
