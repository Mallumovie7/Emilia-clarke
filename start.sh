if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tanujairam123/emilia-extra-features.git /emilia-extra-features
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /emilia-extra-features
fi
cd /emilia-extra-features
pip3 install -U -r requirements.txt
echo "𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐄𝐦𝐢𝐥𝐢𝐚 𝐜𝐥𝐚𝐫𝐤𝐞 🔥🔥🔥..."
python3 bot.py
