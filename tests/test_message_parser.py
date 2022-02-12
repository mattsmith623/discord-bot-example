from mock_classes import Client, Message, User

from bot.message_parser import is_bot_message, is_command, parse_command


def test_is_bot_message():
    client = Client('mockbotid')
    bot_message = Message(user_id='mockbotid')
    user_message = Message(user_id='mockuserid')

    assert is_bot_message(client, bot_message) is True
    assert is_bot_message(client, user_message) is False


def test_is_command():
    assert is_command(Message('test')) is False
    assert is_command(Message('! test')) is False
    assert is_command(Message('!test')) is True
    assert is_command(Message('!test argument')) is True
    assert is_command(Message('!test some arguments')) is True


def test_parse_command_without_arguments():
    assert parse_command(Message('!test')) == ['!test']


def test_parse_command_with_single_word_argument():
    assert parse_command(Message('!test argument')) == ['!test', 'argument']
    assert parse_command(Message('!test  argument')) == ['!test', 'argument']


def test_parse_command_with_multi_word_argument():
    assert parse_command(Message('!test some arguments')) == ['!test', 'some arguments']
