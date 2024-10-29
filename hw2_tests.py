import data
import hw2
import unittest

from hw2 import validate_route


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input = data.Point(2,2)
        input2 = data.Point(10,10)
        result = hw2.create_rectangle(input,input2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        input = data.Point(-50,21)
        input2 = data.Point(-120,50)
        result = hw2.create_rectangle(input,input2)
        expected = data.Rectangle(data.Point(-120, 50),data.Point(-50,21))
        self.assertEqual(expected, result)


    # Part 2
    def test_shorter_duration_than_1(self):
        input1 = data.Duration(3,15)
        input2 = data.Duration(4,18)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertEqual(result,expected)

    def test_shorter_duration_than_2(self):
        input1 = data.Duration(5,34)
        input2 = data.Duration(5,57)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertEqual(result,expected)

    def test_shorter_duration_than_3(self):
        input1 = data.Duration(3,43)
        input2 = data.Duration(2,25)
        result = hw2.shorter_duration_than(input1,input2)
        expected = False
        self.assertEqual(result,expected)

    def test_shorter_duration_than_4(self):
        input1 = data.Duration(3,16)
        input2 = data.Duration(3,16)
        result = hw2.shorter_duration_than(input1,input2)
        expected = False
        self.assertEqual(result,expected)

    def test_shorter_duration_than_5(self):
        input1 = data.Duration(3,16)
        input2 = data.Duration(3,14)
        result = hw2.shorter_duration_than(input1,input2)
        expected = False
        self.assertEqual(result,expected)



    # Part 3
    def test_songs_shorter_than_1(self):
        input1 = [data.Song("Bruno Mars", "Grenade", data.Duration(3,42)),
                  data.Song("JVKE","golden hour", data.Duration(3,29)),
                  data.Song("Bruno Mars", "Nothin' on You", data.Duration(4,28)),
                  data.Song("Tyler, the Creator", "See You Again", data.Duration(3,0))]
        input2 = data.Duration(3,30)
        result = hw2.songs_shorter_than(input1,input2)
        expected = [data.Song("JVKE","golden hour", data.Duration(3,29)),
                    data.Song("Tyler, the Creator", "See You Again", data.Duration(3,0))]
        self.assertEqual(expected,result)

    def test_songs_shorter_than_2(self):
        input1 = [data.Song("Bruno Mars", "Die With A Smile", data.Duration(4,11)),
                  data.Song("JVKE","this is what falling in love feels like", data.Duration(2,0)),
                  data.Song("Bruno Mars", "When I Was Your Man", data.Duration(3,33)),
                  data.Song("Tyler, the Creator", "EARFQUAKE", data.Duration(3,10))]
        input2 = data.Duration(3,33)
        result = hw2.songs_shorter_than(input1,input2)
        expected = [data.Song("JVKE","this is what falling in love feels like", data.Duration(2,0)),
                    data.Song("Tyler, the Creator", "EARFQUAKE", data.Duration(3,10))]
        self.assertEqual(expected,result)


    # Part 4
    def test_running_time_1(self):
        input1 = [data.Song("Bruno Mars", "Die With A Smile", data.Duration(4,11)),
                  data.Song("JVKE","this is what falling in love feels like", data.Duration(2,0)),
                  data.Song("Bruno Mars", "When I Was Your Man", data.Duration(3,33)),
                  data.Song("Tyler, the Creator", "EARFQUAKE", data.Duration(3,10))]
        input2 = [2,3,0,2,1]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(16,27)
        self.assertEqual(expected,result)

    def test_running_time_2(self):
        input1 = [data.Song("Decemberists", "June Hymn", data.Duration(4,30)),
                  data.Song("Broken Bells","October", data.Duration(3,40)),
                  data.Song("Kansas", "Dust in the Wind", data.Duration(3,29)),
                  data.Song("Local Natives", "Airplanes", data.Duration(3,58))]
        input2 = [0, 2, 1, 3, 0]
        result = hw2.running_time(input1,input2)
        expected = data.Duration(20, 7)
        self.assertEqual(expected,result)


    # Part 5
    def test_validate_route(self):
        input1 = [['san luis obispo', 'santa margarita'],
                  ['san luis obispo', 'pismo beach'],
                  ['atascadero', 'santa margarita'],
                  ['atascadero', 'creston']]
        input2 = ['san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected,result)

    def test_validate_route_2(self):
        input1 = [['san luis obispo', 'santa margarita'],
                  ['san luis obispo', 'pismo beach'],
                  ['atascadero', 'santa margarita'],
                  ['atascadero', 'creston']]
        input2 = ['pismo beach', 'san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected,result)

    def test_validate_route_3(self):
        input1 = [['san luis obispo', 'santa margarita'],
                  ['san luis obispo', 'pismo beach'],
                  ['atascadero', 'santa margarita'],
                  ['atascadero', 'creston']]
        input2 = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(input1,input2)
        expected = False
        self.assertEqual(expected,result)

    def test_validate_route_4(self):
        input1 = [['san luis obispo', 'santa margarita'],
                  ['san luis obispo', 'pismo beach'],
                  ['atascadero', 'santa margarita'],
                  ['atascadero', 'creston']]
        input2 = []
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected,result)

    def test_validate_route_5(self):
        input1 = [['san luis obispo', 'santa margarita'],
                  ['san luis obispo', 'pismo beach'],
                  ['atascadero', 'santa margarita'],
                  ['atascadero', 'creston']]
        input2 = ['san luis obispo']
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected,result)


    # Part 6
    def test_longest_repetition(self):
        input = [2, 3, 5, 5, 5, 1, 2, 3, 7, 1, 1, 1, 1, 8, 4, 6, 6, 2]
        result = hw2.longest_repetition(input)
        expected = 9
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        input = [4,4,4,4,4,4,7,2,1,2,6,6,6,6,6,8,1,3,3,3,3]
        result = hw2.longest_repetition(input)
        expected = 0
        self.assertEqual(expected, result)

    def test_longest_repetition_3(self):
        input = [2, 3, 5, 5, 5, 1, 2, 3, 7, 1, 1, 1, 1, 8, 4, 6, 6, 2, 7, 7, 7, 7, 7]
        result = hw2.longest_repetition(input)
        expected = 18
        self.assertEqual(expected, result)

    def test_longest_repetition_4(self):
        input = [2, 3, 5, 5, 5, 5, 5, 1, 2, 3, 7, 1, 1, 1, 1, 8, 4, 6, 6, 2, 7, 7, 7, 7, 7]
        result = hw2.longest_repetition(input)
        expected = 2
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
