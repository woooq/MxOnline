# _*_ coding:utf-8 _*_

import xadmin

from .models import Courses, Lesson, Video, CourseResource


class CoursesAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class LessonAdmin(object):
    list_display = ['courses', 'name', 'add_time']
    search_fields = ['courses', 'name']
    list_filter = ['courses__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['courses', 'name', 'download', 'add_time']
    search_fields = ['courses', 'name', 'download']
    list_filter = ['courses', 'name', 'download', 'add_time']


xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
