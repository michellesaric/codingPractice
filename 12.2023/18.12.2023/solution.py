def solution():
  k = input("Enter any number: ")

  if not k.isdigit():
    print("Your input was not a number.")
    return

  k = int(k)
  lst = [10, 15, 3, 7]

  for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
      if lst[i] + lst[j] == k:
        print(f"The sum of {lst[i]} and {lst[j]} is {k}")


solution()