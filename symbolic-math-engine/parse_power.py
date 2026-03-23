def parse_power(self):
  left = self.parse_factor()

  if self.pos < len(self.tokens) and self.tokens[self.pos] == "^":
    self.pos += 1
    right = self.parse_power()
    return Node("^", left, right)

  return left
