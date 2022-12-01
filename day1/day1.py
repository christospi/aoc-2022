import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

input_file = os.path.join(ROOT_DIR, 'day1', 'data', 'input.txt')

def part_one():
  maxi = 0
  curr = 0

  with open(input_file) as file:
    for line in file:
      curr = curr + int(line) if line.strip() else 0
      if curr > maxi:
        maxi = curr

  print(maxi)

def part_two():
  curr = 0
  per_elf = []

  with open(input_file) as file:
    for line in file:
      if line.strip():
        curr += int(line)
      else:
        per_elf.append(curr)
        curr = 0

  print(sum(sorted(per_elf, reverse=True)[:3]))

if __name__ == '__main__':
  part_one()
  part_two()
