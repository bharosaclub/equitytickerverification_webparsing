from levensten_algorithm import *
def similarity_checker(original, new):
  """
  compares every word in original with every word in new using levenshtein similarity, 
  and if passing a certain threshold decided by length of word/constant n it takes words as the same
  """
  original = original.split(' ')
  new = new.split(' ')
  matches = 0
  for og_w in original:
    for new_w in new:
      similarity_word = levenshtein_distance(og_w, new_w)
      print(f"original: {og_w}, new: {new_w}, threshold: {(len(og_w)/1.2)}, score: {similarity_word}")
      if similarity_word < (len(og_w)/1.2):
        matches += 1

  return [matches, len(original), matches/len(original)]

print(similarity_checker("Domino's pizza incorporated", "DominoS Pizza"))