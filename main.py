import time
print('')
for i in range(10):
    print('--in--', end="\r")
    time.sleep(4)
    print('-hold-', end="\r")
    time.sleep(4)
    print('--out-', end="\r")
    time.sleep(4)
    print('-hold-', end="\r")
    time.sleep(4)
