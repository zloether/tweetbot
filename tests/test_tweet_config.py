#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from tweetbot import tweet_config
from argparse import ArgumentParser


def test_tweet_config_init():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    assert isinstance(tc, tweet_config.tweet_config)



def test_get_api_creds():
    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    # get api creds
    creds = tc.get_api_creds()
    
    assert creds[0] == 'test_oauth_consumer_key'
    assert creds[1] == 'test_oauth_consumer_secret'
    assert creds[2] == 'test_oauth_token'
    assert creds[3] == 'test_oauth_token_secret'



def test_get_list_file():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    # test list file to check against
    default_list_file = 'config/things_to_tweet.txt'

    # test default list file
    assert tc.get_list_file() == default_list_file

    # test list file to use
    test_list_file = 'test/test_files/test_list.txt'

    # try --list argument
    tc.args = tc.parser.parse_args(['--list', test_list_file])

    assert tc.get_list_file() == test_list_file



def test_get_status_check():
    # create tweet_config object
    tc = tweet_config.tweet_config()
    assert tc.get_status_check() == True

    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)
    assert tc.get_status_check() == False

    # try --status-enable argument
    tc.args = tc.parser.parse_args(['--status-enable'])
    assert tc.get_status_check() == True

    # try --status-disable argument
    tc.args = tc.parser.parse_args(['--status-disable'])
    assert tc.get_status_check() == False



def test_get_tweet_things():
    # create tweet_config object
    tc = tweet_config.tweet_config()
    assert tc.get_tweet_things() == False

    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)
    assert tc.get_tweet_things() == True

    # try --tweet-disable argument
    tc.args = tc.parser.parse_args(['--tweet-disable'])
    assert tc.get_tweet_things() == False

    # try --tweet-enable argument
    tc.args = tc.parser.parse_args(['--tweet-enable'])
    assert tc.get_tweet_things() == True



def test_get_verbose():
    # create tweet_config object
    tc = tweet_config.tweet_config()
    assert tc.get_verbose() == False

    # try --verbose argument
    tc.args = tc.parser.parse_args(['--verbose'])
    assert tc.get_verbose() == True

    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)
    assert tc.get_verbose() == False



def test_get_delay():
    # create tweet_config object
    tc = tweet_config.tweet_config()
    assert tc.get_delay() == 60

    # try --delay argument
    tc.args = tc.parser.parse_args(['--delay', '25'])
    assert tc.get_delay() == 25

