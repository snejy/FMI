def fibonacci(n)
  if n <= 1 then n 
  else fibonacci(n-1) + fibonacci(n-2)
  end
end

def lucas(n)
  if n <= 1 then 2
  elsif n == 2 then 1
  else then lucas(n-1) + lucas(n-2)
  end
end

def series(row, n)
  if row == "fibonacci" then fibonacci(n)
  elsif row == "lucas" then lucas(n)
  else fibonacci(n) + lucas(n)
  end
end
