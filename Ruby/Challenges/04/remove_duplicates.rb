def remove_duplicates(array)
  array.reduce({}){ |hash, n| hash.update(n => hash.fetch(n, 0) + 1) }.keys()
end