def parse_expression(self):
  node = self.parse_term()

  while self.pos < len(self.tokens) and self.tokens[self.pos] in ("+","-"):
    op = self.token[self.pos]
    self.pos += 1
    right = self.parse_term()
    node = Node(op, left, right)
  return node
