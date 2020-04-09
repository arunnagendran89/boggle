from boggle.utils.utils import get_random_character, get_unique_id
import enchant

ongoingBoggleGame = None

class BoggleGame:

    def __init__(self):
        self.id = get_unique_id()
        self.board = []
        self.valid_words_in_board = []

    def create_new_game(self):
        for i in range(4):
            row = []
            for j in range(4):
                row.append((get_random_character()))
            self.board.append(row)

    def get_word_score(self, word) -> int:
        """
        The score for a valid word is as follows:

        Fewer than 3 Letters: no score
        3 Letters: 1 point
        4 Letters: 1 point
        5 Letters: 2 points
        6 Letters: 3 points
        7 Letters: 4 points
        8 or More Letters: 11 points
        """
        def is_word_in_dictionary(word):
            dictionary = enchant.Dict("en-us")
            return dictionary.check(word)

        if not self._is_word_in_board(word):
            return 0
        if not is_word_in_dictionary(word):
            return 0
        score_for_length = [0, 0, 0, 1, 1, 2, 3, 4, 11, 11, 11, 11, 11, 11, 11, 11, 11]

        return score_for_length[len(word)]

    def _is_word_in_board(self, word) -> bool:
        def search(board, row, col, word):
            dirs = ([-1, 0], [1, 0], [1, 1],
               [1, -1], [-1, -1], [-1, 1],
               [0, 1], [0, -1])
            if board[row][col] != word[0]:
                return False

            for x, y in dirs:
                i, j = row + x, col + y
                found = True
                for k in range(1, len(word)):
                    if (0 <= i < 4 and
                            0 <= j < 4 and
                            word[k] == board[i][j]):
                        i += x
                        j += y
                    else:
                        found = False
                        break
                if found:
                    return True
            return False

        for row in range(4):
            for col in range(4):
                if search(self.board, row, col, word):
                    return True
        return False


class BogglePlayerGame:
    def __init__(self):
        self.id = get_unique_id()
        self.game_session = None
        self.player_total_score = 0
        self.player_word_history = set()

    def submit_guess(self, word) -> int:
        if word in self.player_word_history:
            return 0
        score = self.game_session.game.get_word_score(word)
        if score > 0:
            self.player_total_score += score
            self.player_word_history.add(word)
        return score

    def start_game(self):
        self.game_session = create_or_join_boggle_session(True)

    def join_game(self):
        self.game_session = create_or_join_boggle_session()

    def leave_game(self):
        self.game_session = None
        self.player_total_score = 0
        self.player_word_history = set()


def create_or_join_boggle_session(force_create = False) -> BoggleGame:
    global ongoingBoggleGame
    if not ongoingBoggleGame or force_create:
        ongoingBoggleGame = BoggleGame()
    return ongoingBoggleGame

