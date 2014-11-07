def ordinal(n)
    {1 => "st", 2 => "nd", 3 => "rd"}.select { |key, value| key == n.to_s[-1]
        .to_i }.map{|key, value| key.to_s + value }[0] or n.to_s + "th"
end
