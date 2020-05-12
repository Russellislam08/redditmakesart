# in scraper directory, you do:
pip3 install -r requirements.txt --target ./package
cd package && zip -r9 ../function.zip ./package/ && cd ../
zip -g function.zip scraper.py
zip -g function.zip dal.py

# from here, you can either upload manually to lambda, use terraform
# or use awscli
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
