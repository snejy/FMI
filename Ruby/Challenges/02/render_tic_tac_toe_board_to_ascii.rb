def render_tic_tac_toe_board_to_ascii(board)
    board.map{ |element| element.nil? ? " " : element.to_s}.each_slice(3).to_a.
    map{ |element| element.join(" | ").insert(0,"| ") + " |\n"}.join.strip
end
