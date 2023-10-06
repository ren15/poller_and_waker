# poller_and_waker

Suppose you have a.py and b.py. 

1. You start a.py and b.py, supervise them, and restart them if they crash.

2. b.py depends on a.py's output. a.py takes some time to start up.

3. a.py write some data to a sqlite database. b.py reads from the database.

4. b either polls the database, or long polls a.py's output via nats, or any http endpoint.


## solution

1. hivesmind/overmind
2. nats pubsub
3. pid.file
