#!$SHELL
## create database "jp_lr"
## create a table for word

if psql -lqt | cut -d \| -f 1 | grep -qw jp_lr ; then
    echo "db: jp_lr exist"
else
    createdb jp_lr
fi

echo "Please enter the table name: "
read table
python3 create_word_db.py $table
