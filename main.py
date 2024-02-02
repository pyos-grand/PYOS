import hmcg
import os
with open('conf/shell.conf', 'r') as f:
    shell = f.readline()
    if shell == "ish":
        print("[INFO] Loading ish")
        import interactiveshell
        interactiveshell.console()
    if shell == "hmcg":
        print("[INFO] Loading hmcg")
        hmcg.run()
    else:
        hmcg.run()

