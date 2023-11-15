#!/usr/bin/python3
"""https://pymotw.com/2/cmd/"""
import cmd


class MyCmd(cmd.Cmd):
    """doc"""
    def emptyline(self):
        pass
    
    def do_hi(self, line):
        """print a greeting"""
        print("Hello")
    
    def do_EOF(self, line):
        """doc"""
        return True


if __name__ == '__main__':
    MyCmd().cmdloop()
