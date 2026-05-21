import importlib
import filechanges


def changes():
    try:
        importlib.reload(filechanges)
    except:
        pass


user = input("Press Enter to continue")
for i in range(5):
    changes()