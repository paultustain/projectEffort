from visuals import Visualiser
import argparse 

parser = argparse.ArgumentParser(description="A CLI Project tracking tool")
parser.add_argument(
    "-p", 
    "--project", 
    help="Project name", 
    default=None
)

args = parser.parse_args()
print(args.project)
vis = Visualiser()

# print(timer)

# for _ in range(60 * 30):
#     timer.count_down()

#     print(timer)

# timer.count_down()

# print(timer)
