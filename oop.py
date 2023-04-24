class kucing:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print("Meow, Aku", self.name, "and Aku", self.age, "tahun")

# membuat objek kucing
my_kucing = kucing("Oyen", 2)

# memanggil metode dari objek kucing
my_kucing.meow() 
