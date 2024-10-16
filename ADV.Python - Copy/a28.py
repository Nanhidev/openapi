class Too_old(Exception):
    def __init__(self,arg):
        self.msg = arg

class Too_young(Exception):
    def __init__(self,arg):
        self.msg = arg


age = int(input("Enter your age :"))
if age > 60 :
        raise Too_old('Age should not exceed 60 !')

elif age < 20 :
         raise Too_young("Age should not be under 20 !")

else :
        print('you are eligible to take policy')


print()


class Too_Old(Exception):
      def __init__(self,arg):
            self.msg = arg

class Too_Young(Exception):
      def __init__(self,arg):
            self.msg = arg
try :
      age = int(input("Enter the your age :"))
      if age > 60 :
            raise Too_Old('Age should not exceed 60 !')
      
      elif age < 20 :
            raise Too_Young('Age should not be under 20 !')
      
      else:
            print("you are eligible to take policy !")

except Exception as msg :
      print(msg)