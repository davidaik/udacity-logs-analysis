#!/usr/bin/env python3

import argparse
import psycopg2
import calendar
DBNAME = "news"


def get_top_articles(num_articles):
    limit = ''
    if(int(num_articles) > 0):
        limit = ' limit ' + str(num_articles)
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select articles.title, num
                from
                    (select articles.slug as slug, count(*) as num
                            from articles, log
                            where concat('/article/', articles.slug) = log.path
                            and log.status = '200 OK'
                            group by articles.slug
                            order by num) as toparticles,
                    articles
                where articles.slug = toparticles.slug
                group by articles.title, num
                order by num desc%s''' % (limit))
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors(num_authors):
    limit = ''
    if(int(num_authors) > 0):
        limit = ' limit ' + str(num_authors)

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute('''select authors.name, sum(num) as authorsum
                from
                    (select articles.slug as slug, count(*) as num
                            from articles, log
                            where concat('/article/', articles.slug) = log.path
                            and log.status = '200 OK'
                            group by articles.slug
                            order by num) as toparticles,
                    articles, authors
                where authors.id = articles.author
                and articles.slug = toparticles.slug
                group by authors.name
                order by authorsum desc%s''' % (limit))
    authors = c.fetchall()
    db.close()
    return authors


def get_one_percent_error_days(num_days):
    limit = ''
    if(int(num_days) > 0):
        limit = ' limit ' + str(num_days)

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute('''select * from
                    (select allreqsquery.day,
                            (errorsquery.errorsnum * 100.0
                            / allreqsquery.reqsnum) as percent
                        from
                            (select date(time) as day, count(*) as reqsnum
                                from log
                                group by day)
                                as allreqsquery,
                            (select date(time) as day, count(*) as errorsnum
                                from log
                                where status != '200 OK'
                                group by day)
                                as errorsquery
                        where allreqsquery.day = errorsquery.day
                        order by errorsquery.errorsnum desc%s) as subquery
                    where subquery.percent > 1''' % (limit))
    errordays = c.fetchall()
    db.close()
    return errordays


# Parse command line arguments
parser = argparse.ArgumentParser(
            description='Get information from news database'
        )
parser.add_argument(
                    "querytype",
                    choices=[
                        'top-articles',
                        'top-authors',
                        'one-percent-error-days'
                    ],
                    help="Query to run"
                )
parser.add_argument(
                    '-n',
                    '--numrows',
                    help='number of rows to return',
                    type=int
                )
args = parser.parse_args()

if(args.querytype == 'top-articles'):
    articles_count = 0
    if args.numrows:
        articles_count = args.numrows
    for article in get_top_articles(articles_count):
        print('%s - %d views' % (article[0], article[1]))

elif(args.querytype == 'top-authors'):
    authors_count = 0
    if args.numrows:
        authors_count = args.numrows
    for authors in get_top_authors(authors_count):
        print('%s - %d views' % (authors[0], authors[1]))

elif(args.querytype == 'one-percent-error-days'):
    days_count = 0
    if args.numrows:
        days_count = args.numrows
    for day in get_one_percent_error_days(days_count):
        print('%s %s, %s - %f%% errors' %
              (calendar.month_name[day[0].month],
               day[0].day,
               day[0].year,
               day[1]))
