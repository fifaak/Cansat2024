import datetime

def get_current_time():
  """Prints the current date and time in a readable format."""
  now = datetime.datetime.now()
  print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Format the output for better readability

if __name__ == "__main__":
  get_current_time()
