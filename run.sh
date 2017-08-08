git clone https://github.com/Stufinite/CampassCrawler.git;
pip install -r CampassCrawler/requirements.txt
cd CampassCrawler/UCrawler; scrapy crawl NSYSU -o ../../calApi/NSYSU.json -t json; cd -
cd calApi; pwd; python manage.py migrate; python manage.py buildCourse  NSYSU.json NSYSU 1061