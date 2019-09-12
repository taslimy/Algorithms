#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # initialize batches made
  batches = 0
  # set it true so we got ingredients
  got_ingredients = True
  # we make with the recipies we have
  while got_ingredients:
    # subtract from the recipies
    for ing in recipe:
      if ingredients.get(ing) == None or ingredients[ing]-recipe[ing] < 0:
        got_ingredients = False
      else:
        ingredients[ing] = ingredients[ing]-recipe[ing]
    # increment batches
    if got_ingredients:
      batches += 1

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))