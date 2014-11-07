def prime?(number)
    number.abs == 1 ? false :
    2.upto(number.abs / 2).all?{|digit| number.abs % digit == 0 ? false : true}
end