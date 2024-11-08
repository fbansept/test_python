class ComptaUtils :

    @staticmethod
    def moyenne(tuple) :

        cumul = 0

        for element in tuple :
            cumul += element

        return cumul / len(tuple)
    
class HelloUtils :

    @staticmethod
    def hello() :

        return "hello world"

