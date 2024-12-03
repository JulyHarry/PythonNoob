class WillDelete:
    def __del__(self):
        print("WillDelete Delete")


print("start")
x = WillDelete()
x = 3
print("end")
