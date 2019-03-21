## News.py

**news.py** is a command line program that answers some useful queries related to the news database. It is useful for getting information on top articles, top authors, and to find the days on which a large number of requests to the news website led to an error.

It uses the `psycopg2` library to run SQL queries against the news database.

## Setting up

To run the program, you will need to install the provided virtual machine. It comes with PostgreSQL set up with the news database (without the actual data, you will need to import it separately). Steps for getting set up on **Ubuntu** are explained below, but you can adapt them for whichever machine you're on.

### Install Vagrant

`$ sudo apt update`  
`$ sudo apt install vagrant`

### Download the VM configuration
Download this file: [news-virtual-machine.zip](https://drive.google.com/open?id=1UdCcLO3-A9WEk6AjOhcIbUwUrv1D5m0U) and unzip it. This will give you a directory called **news-virtual-machine**.

Open up a terminal and cd into the **vagrant** directory inside. Then run this command: `vagrant up`.

This will download an entire Ubuntu based virtual machine from the network. This may take some time depending on your connection speed.

### Connect to the virtual machine

Your virtual machine should be running now. To connect to it, run `vagrant ssh`

### Logging out and in

To log out of your virtual machine, run type `CTRL+D`. To stop the running vm, run
`vagrant halt`.

If you reboot your computer, or you have stopped down your virtual machine, start it again by running `vagrant up` the same way as you did before. Note: This will not download the virtual machine again from the network.

## Download the program

While you're connected to your virtual machine, cd into the **vagrant** directory.

`$ cd /vagrant`

Then clone the repository into this directory by running
`$ git clone https://github.com/davidaik/udacity-logs-analysis.git`

If **git** is not install, install it by running  
`$ sudo apt install git`

This will give you a directory called **udacity-logs-analysis** which will contain the **news.py** file along with others.

## Setting up the database

To get any useful output form the program, we will need some database with proper data to work with. Download this file: [newsdata.zip](https://drive.google.com/open?id=1KhSrlmZZ0_tRb-kQjBctSo82hfWfDdZ-). Extract it and you will get a file called **newsdata.sql**. Copy this file into your **udacity-logs-analysis** directory.

### Import the data into your database.

Now, we need to import the data from the **newsdata.sql** file into your PostgreSQL database which comes with the given VM.

To do this, on your virtual machine, cd into the **udacity-logs-analysis** directory and run
`psql -d news -f newsdata.sql`

Now we're ready to use the program.


## Dependencies

**psycopg2**:  
`$ pip3 install psycopg2`

**psycopg2-binary**: To avoid **The psycopg2 wheel package will be renamed** warning.  
`$ pip3 install psycopg2-binary`

If you're still getting the warning, uninstall both `psycopg2` and `psycopg2-binary` and run the following in order.

`$ pip3 install psycopg2`  
`$ pip3 install psycopg2-binary`


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
