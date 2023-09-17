mkdir -p data

python src/a.py &
python src/b.py &

wait

sqlite3 \
    data/db.sqlite3 \
    "select * from deployment_meta"