import picSpider;

pageLoader = picSpider.PageLoader("http://tieba.baidu.com/p/4732283532");
pageLoader.loadHtml();
pageLoader.saveImgs("D:/tmp/temp/");

print("完成");
