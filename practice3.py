def describe_person(name, **kwargs):
  new = list(kwargs.items())
  print(f"Characteristic of {name}")
  for key, value in new:
    print(f"{key}: {value}")