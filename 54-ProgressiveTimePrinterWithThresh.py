import time

counter = 1
while True:
    print("Hello")
    if counter >= 4:
        print("End of loop.")
        break
    time.sleep(counter)
    counter += 1

