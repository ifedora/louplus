#!/usr/bin/env python3

import scrapy
class ShiyanlouCoursesSpider(scrapy.Spider):
    name = "shiyanlou-courses"

    def start_requests(self):
        url_tmp="https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}"
        urls = (url_tmp.format(i) for i in range(1,25))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        for course in response.css('div.course-body'):
            yield{
                    "name":course.css("div.course-name::text").extract_first(),
                    "description":course.css("div.course-desc::text").extract_first()
                    }
