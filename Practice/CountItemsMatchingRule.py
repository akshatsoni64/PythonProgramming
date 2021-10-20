def countMatches(self, items, ruleKey, ruleValue):
    d = {'type': 0, 'color': 1, 'name': 2}
    count = 0
    for i in range(len(items)):
        if items[i][d[ruleKey]] == ruleValue:
            count += 1
    return count

  
print(
  countMatches(
      [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
      "color",
      "silver"
  )
)
