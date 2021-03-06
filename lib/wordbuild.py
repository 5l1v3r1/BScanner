# coding=utf-8
import Queue
from lib.config import conf
from lib.log import logger
from tqdm  import tqdm

__author__ = "LoRexxar"
# 设置标志位为字典有多少行
raw_words = 0


def build_wordlist(wordlist_file):
    # 读入字典文件
    fd = open(wordlist_file, "rb")
    logger.info("start wordlist build...")
    global raw_words
    raw_words = fd.readlines()
    logger.info("This dictionary contains %s rows" % len(raw_words))
    print "This dictionary contains %s rows..." % len(raw_words)
    if len(raw_words) == 0:
        logger.error("This dictionary is empty...")
    fd.close()

    found_resume = False
    words = Queue.Queue()

    for word in raw_words:
        word = word.rstrip()

        # 这功能暂时没开

        if conf['resume'] is not None:
            if found_resume:
                words.put(word)
            else:
                if word == conf['resume']:
                    found_resume = True
                    print "Resuming wordlist from : %s" % conf['resume']

        else:
            words.put(word)

    logger.info("wordlist build is complete...")
    return words
