#!$SHELL
## create database "jp_lr"
## create a table for word

if psql -lqt | cut -d \| -f 1 | grep -qw jp_lr ; then

else
    createdb jp_lr
fi

echo "\e[0;35mPlease enter the table name: \e[0m"
read table
python3 create_word_db.py $table
