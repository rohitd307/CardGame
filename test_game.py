import unittest
import card_game

class TestCardGame(unittest.TestCase):
    
    # Test size of deck is 40
    def test_createDeck(self):
        result = card_game.createDeck()
        self.assertEqual(len(result),40)

    # Test is deck is shuffled or not
    def test_shuffle(self):
        arr = card_game.createDeck()
        tempArr = arr[:]
        shuffledArr = card_game.shuffleDeck(tempArr, len(arr))
        self.assertNotEqual(arr, shuffledArr)

    # Test to check discard pile is shuffled into empty draw pile
    def test_drawPile(self):
        drawPile = []
        discardPile = [4, 7, 9, 3, 7, 7]
        self.assertEqual(card_game.changePile(discardPile, drawPile), [4, 7, 9, 3, 7, 7])

    def test_checkDraw(self):
        self.assertEqual(card_game.decideDraw(6, 9), 9)
        self.assertEqual(card_game.decideDraw(4, 2), 4)


if __name__ == '__main__':
    unittest.main()