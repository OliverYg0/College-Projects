import random


class Game:
    running = False
    score = 0
    lives = 3

    @classmethod
    def check_if_player_won(cls, player_choice, computer_choice):
        if player_choice == 'r' and computer_choice == 's' or player_choice == 's' and computer_choice == 'p' or player_choice == 'p' and computer_choice == 'r':
            return True

    @classmethod
    def start(cls):
        cls.running = True

        print(f'You have {cls.lives} lives remaining')

        while cls.running:
            if cls.lives > 0:
                player_choice = input('\nR for Rock, P for paper and S for Scissors: ').strip().lower()
                computer_choice = random.choice(('r', 'p', 's'))

                print(f'\nYou choose {player_choice}')
                print(f'The computer choose {computer_choice}')

                if player_choice == computer_choice:
                    print('\nIt was a draw')
                elif (cls.check_if_player_won(player_choice, computer_choice)):
                    cls.score += 1
                    print(f'\nYou won, your score is {cls.score}')
                    print(f'You have {cls.lives} lives remaining')
                else:
                    cls.lives -= 1
                    print(f'\nYou lose, you have {cls.lives} remaining')
                    print(f'Your score is still {cls.score}')
            else:
                print('Game Over')
                print(f'Score {cls.score}')
                cls.running = False


def main():
    Game.start()


if __name__ == '__main__':
    main()