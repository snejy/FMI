import unittest
import solution

class TestFiveFunctions(unittest.TestCase):

    def test_is_pangram(self):
        self.assertFalse(
            solution.is_pangram('Малката пухкава панда яде бамбук.'))

        self.assertTrue(
            solution.is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'))

    def test_char_histogram(self):
        self.assertEqual(
            {' ': 3, 'i': 2, 'a': 2, 'e': 2, 's': 2, 'h': 1, 'l': 1, 'm': 1,
             'n': 1, 'x': 1, '!': 1, 'p': 1, 'T': 1},
            solution.char_histogram('This is an example!'))

    def test_sort_by(self):
        self.assertEqual(['a', 'ab', 'abc'],solution.sort_by(lambda x, y: len(x) - len(y), ['abc', 'a', 'ab']))

    def test_group_by_type(self):
        self.assertEqual({str: {'b': 1, 'a': 12}, int: {1: 'foo'}}, solution.group_by_type({'a': 12, 'b': 1, 1: 'foo'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b'},
             tuple: {(1, 2): 12, ('a', 1): 1}},
            solution.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b', 'c': 15}))
        
    def test_anagrams(self):
        words = ['army', 'mary', 'ramy', 'astronomer', 'moonstarer',
                 'debit card', 'bad credit', 'bau']
        anagrams = [['army', 'mary', 'ramy'],
                    ['bad credit', 'debit card'],
                    ['astronomer', 'moonstarer'], ['bau']]
        self.assertEqual(set(map(frozenset, anagrams)),set(map(frozenset, solution.anagrams(words))))
    
    def test_sort_by_2(self):
        words = ['hey', 'hi', 'hello', 'buy', 'io', 'a']
        self.assertEqual(['a', 'hi', 'io', 'hey', 'buy', 'hello'],solution.sort_by(lambda x, y: len(x) - len(y), words))
        self.assertEqual([3, 3, 5, 10, 15, 30, 100],solution.sort_by(lambda x, y: x - y,[15, 3, 10, 100, 5, 3, 30]))
        self.assertEqual([33, 32, 15, 9, 7, 2, 1],solution.sort_by(lambda x, y: y - x,[7, 2, 9, 1, 15, 33, 32]))
        self.assertEqual([0, 4, 4, 5, 11, 12, 16],solution.sort_by(lambda x, y: x - y,[12, 5, 4, 16, 0, 4, 11]))
        self.assertEqual([2,1],solution.sort_by(lambda x, y: y - x,[1,2]))
    
    def test_group_by_type_2(self):
        self.assertEqual({str: {'val': 5, 'var': 7}, int: {1: 2},tuple: {(3, 4): 'c'}},solution.group_by_type({'val': 5, 'var': 7, 1: 2,(3, 4): 'c'}))
 
        self.assertEqual({str: {'c': 15}, int: {1: 'b', 12: 202},tuple: {(1, 2): 12, ('a', 1): 1, (3, 4, 5, 6): 7}},solution.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b',(3, 4, 5, 6): 7, 'c': 15, 12: 202}))
 
    
    def test_anagrams_2(self):
        words = ['wamаn hitler', 'the eyes', 'dormitory', 'mаther-in-law','dirty room', 'they see']
        anagrams = [['wamаn hitler', 'mаther-in-law'],['the eyes', 'they see'],['dormitory', 'dirty room']]

 
        self.assertEqual(set(map(frozenset, anagrams)),set(map(frozenset, solution.anagrams(words))))
    
    def test_anagrams_0(self):
        words = ["To be or not to be: that is the question; whether"
            " \'tis nobler in the mind to suffer the slings and arrows"
            " of outrageous fortune...",
            "In one of the Bard\'s best-thought-of tragedies our"
            " insistent hero, Hamlet, queries on two fronts about"
            " how life turns rotten.", "wow"]
        anagrams = [["To be or not to be: that is the question; whether"
            " \'tis nobler in the mind to suffer the slings and"
            " arrows of outrageous fortune...",
            "In one of the Bard\'s best-thought-of tragedies our"
            " insistent hero, Hamlet, queries on two fronts about"
            " how life turns rotten."], ["wow"]]
        self.assertEqual(set(map(frozenset, anagrams)),set(map(frozenset, solution.anagrams(words))))
 
    def test_anagrams_1(self):
        words = [("To be or not to be: that is the question; whether \'tis"
        " nobler in the mind to suffer the slings and arrows of"
        " outrageous fortune, or to take arms against a sea of"
        " troubles and by opposing, end them?"),
        ("Is a befitting quote from one of Shakespeare\'s greatest"
        " tragedies. But why won\'t Hamlet\'s inspiring motto toss"
        " our stubborn hero\'s tortuous battle for life, on one"
        " hand, and death, on another?"), "such string"]
        anagrams = [[("To be or not to be: that is the question; whether \'"
        "tis nobler in the mind to suffer the slings and arrows"
        " of outrageous fortune, or to take arms against a sea"
        " of troubles and by opposing, end them?"),
        ("Is a befitting quote from one of Shakespeare\'s"
        " greatest tragedies. But why won\'t Hamlet\'s inspiring"
        " motto toss our stubborn hero\'s tortuous battle for"
        " life, on one hand, and death, on another?")],
        ["such string"]]
        self.assertEqual(
        set(map(frozenset, anagrams)),
        set(map(frozenset, solution.anagrams(words))))
         
    def test_anagrams_3(self):
        words = ["Election results", "Stolen cruelties.",
        "Lies – let\'s recount", "Halley\'s Comet",
        "Shall yet come", "Conversation",
        "Voices rant on", "Fir cones", "Conifers"]
        anagrams = [["Election results", "Stolen cruelties.",
        "Lies – let\'s recount"],
        ["Halley\'s Comet", "Shall yet come"],
        ["Conversation", "Voices rant on"],
        ["Fir cones", "Conifers"]]
        self.assertEqual(
        set(map(frozenset, anagrams)),
        set(map(frozenset, solution.anagrams(words))))
         
 

if __name__ == '__main__':
    unittest.main()