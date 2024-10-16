import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

print()

import time

class Test:
    def __init__(self):
        print('Constructor execution')

    def __del__(self):
        print('Destructor execution')


T = Test()
time.sleep(5)
print("End of the program")

