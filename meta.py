import json, os, importlib.util

class Main:
    def __init__(self):
        self.attacks = {}
        self.load_attacks()

    def load_attacks(self):
        module_dir = "core/modules/"
        for file in os.listdir(module_dir):
            if file.endswith(".py"):
                file_path = module_dir + file
                spec = importlib.util.spec_from_file_location(file, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "arguments"):
                    self.attacks[file.split(".py")[0]] = module.arguments
        print("Loaded attacks")


    def main(self):
        def interpreter(entry):
            commands = {
                "help"   : {"desc" : "Shows all commands", "args" : [{"name" : "module", "required" : False}]},
                "list"   : {"desc" : "Lists current attacks", "args" : []},
                "search" : {"desc" : "Searches for an attack", "args" : [{"name" : "module", "required" : True}]},
                "select" : {"desc" : "Loads an attack", "args" : [{"name" : "attack", "required": True}]} ,
                "set"    : {"desc" : "Sets the variable for the attack", "args" : [{"name" : "variable", "required" : True}]}
            }
            if not entry in commands:
                return {"status" : "Failed", "message" : "No proper command provided"}
            return {"status" : "Success", "message" : commands[entry]}

        while True:
            entry = input("> ")
            data = interpreter(entry)
            if data["status"] == "Failed":
                print(data["message"])
                continue
            print(data)
            


if __name__ == "__main__":
    main = Main()
    main.main()