import unittest
from unittest.mock import patch, MagicMock, ANY
import main as bot
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    @freeze_time("2021-12-20 14:00")
    @patch("main.bot")
    def test_something(self, mock_bot):
        chat = MagicMock(id=123)
        user = MagicMock(first_name='a', last_name='b')
        message = MagicMock(chat=chat, from_user=user)
        bot.welcome(message)
        mock_bot.send_message.assert_called_with(chat.id,
                                                 'Добрый день, a b\nВы желаете записаться на одну из наших секций?',
                                                 parse_mode='html', reply_markup=ANY)


if __name__ == '__main__':
    unittest.main()
