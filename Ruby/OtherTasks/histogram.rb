def histogram(string)
    string.scan(/\w/).reduce({}) { |h, w| h.update(w => h.fetch(w, 0) + 1) }
end