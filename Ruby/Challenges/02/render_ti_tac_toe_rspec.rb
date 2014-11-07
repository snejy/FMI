describe 'render_tic_tac_toe_board_to_ascii' do
  it 'renders boards with x and o markers' do
    expect(render_tic_tac_toe_board_to_ascii([
      :x,  nil, nil,
      :o,  :x,  nil,
      :x,  :o,  :o,
    ])).to eq(<<BOARD.chomp)
| x |   |   |
| o | x |   |
| x | o | o |
BOARD
  end
end

describe 'render_tic_tac_toe_board_to_ascii' do
  it 'renders boards with x and o markers 2' do
    expect(render_tic_tac_toe_board_to_ascii([
      nil,  nil, nil,
      :o,   :x,  nil,
      :x,   :o,  :o,
    ])).to eq(<<BOARD.chomp)
|   |   |   |
| o | x |   |
| x | o | o |
BOARD
  end
end

describe 'render_tic_tac_toe_board_to_ascii' do
  it 'renders boards with x and o markers' do
    expect(render_tic_tac_toe_board_to_ascii([
      nil,  nil, nil,
      nil,  nil, nil,
      nil,  nil, nil,
    ])).to eq(<<BOARD.chomp)
|   |   |   |
|   |   |   |
|   |   |   |
BOARD
  end
end