# Scrapy settings for yahooFinance project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yahooFinance'

SPIDER_MODULES = ['yahooFinance.spiders']
NEWSPIDER_MODULE = 'yahooFinance.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yahooFinance (+http://www.yourdomain.com)'
