class Dad :
    baskeball = 1
class Son(Dad) :
    dance = 1
    def is_dance (self) :
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def is_dance (self) :
        return f"Jackson yahe!" \
               f"Yes i dance very awsemally {self.dance} no of times"


darry = Dad()
larry = Son()
harry = Grandson()
print(harry.is_dance())