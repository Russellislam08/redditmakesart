sudo cp ~/redditmakesart/client/* /opt/front-end/
cd /opt/front-end
sudo npm run build
sudo systemctl restart nginx
