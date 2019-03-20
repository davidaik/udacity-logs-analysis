## News.py

**news.py** is a command line program that answers some useful queries related to the news database. It is useful for getting information on top articles, top authors, and to find the days on which a large number of requests to the news website led to an error.

It uses the `psycopg2` library to run SQL queries against the news database.

## Dependencies

**psycopg2**:  
`$ pip3 install psycopg2`

## Usage

The program is written for Python 3, but it runs with no problems under Python 2.

To use the program, cd into the directory containing the news.py file and execute it with the available query types.

The basic structure of commands for running the program is shown below.

`$ python3 news.py QUERY_TYPE -n NUMBER_OF_ROWS`

`QUERY_TYPE` is a required argument that can be replaced with any of the following:

`top-articles` : Print top articles  
`top-authors` : Print top authors  
`one-percent-error-days` : Print days on which >1% of requests led to an error

`-n NUMBER_OF_ROWS` is an optional argument, where `NUMBER_OF_ROWS` is a numerical value. Use it to set the number of rows returned by the query.

### 1. Print top articles in the database
`$ python3 news.py top-articles -n 3`

Example output:

    $ python3 news.py top-articles -n 3
    Candidate is jerk, alleges rival - 338647 views
    Bears love berries, alleges bear - 253801 views
    Bad things gone, say good people - 170098 views

### 2. Print top authors

`$ python3 news.py top-articles -n 3`

Example output:

    $ python3 news.py top-articles -n 3
    Ursula La Multa - 507594 views
    Rudolf von Treppenwitz - 423457 views
    Anonymous Contributor - 170098 views

### 3. Print days on which >1% of page requests led to an error

`$ python3 news.py one-percent-error-days -n 3`

Example output:

    $ python3 news.py one-percent-error-days -n 3
    July 17, 2016 - 2.262686% errors
    July 1, 2016 - 1.001734% errors
    July 25, 2016 - 3.953257% errors

## License
> MIT License

> Copyright (c) 2019 David Heisnam

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
