import sys
import random

status = random.choice(["OK", "FAIL"])

if status == "OK":
  print("Success")
  sys.exit(0)
else:
  print("Failed")
  sys.exit(1)
