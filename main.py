import cmd
import subprocess


class mainInterface(cmd.Cmd):

    def do_add(self, s):
        l = s.split()
        if len(l) != 2:
            print("*** invalid number of arguments")
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print("*** arguments should be numbers")
            return
        print(l[0] + l[1])

    def do_open(self, arg):
        if len(arg.split()) == 1:
            file = arg
            try:
                if file == "excel.exe":
                    file = "c:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
                subprocess.run([file])
            except (FileNotFoundError, FileExistsError):
                print("*** file not found or not exist")
                return
        elif len(arg.split()) == 2:
            file, path = arg.split()
            if file == "excel.exe":
                file = "c:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
            try:
                subprocess.run([file, path])
            except FileNotFoundError:
                print("*** file not found")
                return
        else:
            print("*** invalid number of arguments")
            return

    def do_exit(self):
        print("Exit the cmd...")
        return True


if __name__ == "__main__":
    interface = mainInterface()
    interface.cmdloop()
