# Stock Prediction with News Input
Code base for stock prediction project for Computational Data Science SUTD ISTD Term 6

Project Report: https://github.com/junqingchang/stockPredict/blob/master/CDS_Report.pdf

## Code Description
Sentiment - sentiment analyzer test

GoogleScrape - Scrapper tool

dataAugment - Data arranging tool for processedSelected

bowSentiment - Mine data cleaning plus appending sentiment score

Pairing - Combining mined data with selected data and calculates sentiment and individual credibility score

FinalFrameProduction - Produces finaldata, combines all credibility score to get a general credibility score, and concat all data

## Scrapper Support
* [MotleyFool](fool.com)
* [Investopedia](investopedia.com)
* [Reuters](reuters.com)
* [CNBC](cnbc.com)
* [MarketWatchNewsViewer](marketwatch.com)

## Datasets
selectedData - Data from [Huge Stock Market Dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)

mined - Data obtained from mining news articles

processedSelected - Selected Data arranged in running order, aligned with mined data

scoredSelected - Scored selected data with sentiment and credibility score

finaldata.csv(inside modellingfiles) - Final dataset used for modelling

## Authors
* **Vincent**
* **Zenger**
* **Jun Qing**

## Acknowledgements
Dataset from [Huge Stock Market Dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs) from kaggle
