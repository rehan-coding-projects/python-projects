def parse_term(self):
  node = self.parse_power()

  while self.pos < len(self.tokens) and self.tokens[self.pos] in ("*","/"):
    op = self.tokens[self.pos]
    self.pos += 1

    right = self.parse_power()
    node = Node(op, left, right)
  return node
