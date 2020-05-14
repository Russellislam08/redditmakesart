sudo cp -r ~/redditmakesart/client/* /opt/front-end/
cd /opt/front-end
sudo npm install
sudo npm run build
sudo systemctl restart nginx
