import urllib2
import datetime
import logging
import argparse

log = 'error.log'
logging.basicConfig(filename=log, level=logging.ERROR)
logger1 = logging.getLogger('IS211_Assignment2')


def downloadData(urlm):
    file = urllib2.urlopen(urlm)
    read_file = file.read()
    return read_file


def processData(fp):
    mdict = {}
    file_break = fp.split('\n')
    f = open(log, 'rt')
    for x in file_break[1:-1]:
        rec = x.split(',')
        try:
            mdict[rec[0]] = (rec[1], datetime.datetime.strptime(rec[2], "%d/%m/%Y"))
        except ValueError:
            msg = 'Error processing line {} for ID {}'.format(x[0], rec[0])
            logger1.error(msg)
            pass
        else:
            pass
    return mdict


def displayPerson(id, personData):
    try:
        pid = 'Person #{} '.format(id)
        name = 'is {} '.format(personData[id][0])
        bday = 'with a birthday of {}'.format(datetime.datetime.strftime(personData[id][1], '%d/%m/%Y'))
        record = pid + name + bday
        print record
    except:
        print 'No user found with that id'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='enter the data url')
    parser.add_argument('id', help='enter a positive number for id')
    args = parser.parse_args()
    if args.url and args.id:
        if args.id is not 0:
            csvdata = downloadData(args.url)
            result = processData(csvdata)
            records = displayPerson(args.id, result)
        else:
            exit()
    else:
        print 'error'


