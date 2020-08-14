




import gc

class Singer:
    def sing(self):
        print("lalalal!")
        return "LALALAL!"
    
    
    
taeji = Singer()
taeji.sing()

print(id(taeji))
                
taeji = Singer()
taeji.sing()

print(id(taeji))

taeji = Singer()
taeji.sing()

print(id(taeji))

taeji = Singer()
taeji.sing()

print(id(taeji))

taeji = Singer()
taeji.sing()

print(id(taeji))

yuna = Singer()
yuna.sing()

print(id(taeji))



print( globals() )


