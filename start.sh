if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tanujairam-TG/Emilia-clarke.git /Emilia-clarke
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Emilia-clarke
fi
cd /Emilia-clarke
pip3 install -U -r requirements.txt
echo "𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐄𝐦𝐢𝐥𝐢𝐚 𝐜𝐥𝐚𝐫𝐤𝐞 🔥🔥🔥..."
python3 bot.py
