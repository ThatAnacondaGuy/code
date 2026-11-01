def simple_reflex_agent(location,status):

  if status == "Dirty":
    return "suck"
  elif location == "A":
    return "move right"
  else :
    return "move left"

def vacumm_cleaner():

  environment = {
    "A" : "Dirty",
    "B" : "Dirty"
  }
  location = "A"
  while True :
    if environment["A"] == clean and environment["B"] == clean :
      break;
    status = environment[location]
    action = simple_reflex_agent(location,status)
    
