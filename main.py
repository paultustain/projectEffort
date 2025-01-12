from visuals import Visualiser
import argparse 

parser = argparse.ArgumentParser(description="A CLI Project tracking tool")
parser.add_argument(
    "-p", 
    "--project", 
    help="Project name", 
    default=None
)

parser.add_argument(
    "-a", 
    "--aims", 
    help="Aims for the session", 
    action='store_true'
)

args = parser.parse_args()
print(args.project, args.aims)
vis = Visualiser(args.project, args.aims)

# print(timer)

# for _ in range(60 * 30):
#     timer.count_down()

#     print(timer)

# timer.count_down()

# print(timer)
