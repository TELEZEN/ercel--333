if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/ercel--333.git /ercel--333
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ercel--333
fi
cd /ercel--333
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
