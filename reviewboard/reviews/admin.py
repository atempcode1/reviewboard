from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from reviewboard.reviews.forms import DefaultReviewerForm
from reviewboard.reviews.models import Comment, DefaultReviewer, Group, \
                                       Review, ReviewRequest, \
                                       ReviewRequestDraft, Screenshot, \
                                       ScreenshotComment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('truncate_text', 'filediff', 'first_line',
                    'num_lines', 'timestamp')
    list_filter = ('timestamp',)
    raw_id_fields = ('filediff', 'interfilediff', 'reply_to')


class DefaultReviewerAdmin(admin.ModelAdmin):
    form = DefaultReviewerForm
    filter_horizontal = ('repository', 'groups', 'people',)
    fieldsets = (
        (_('General Information'), {
            'fields': ('name', 'file_regex'),
            'classes': ['wide'],
        }),
        (_('Reviewers'), {
            'fields': ('groups', 'people'),
        }),
        (_('Repositories'), {
            'description': _('<p>A default reviewer will cover all '
                             'repositories, unless assigned one or more '
                             'specific repositories below.</p>'),
            'fields': ('repository',),
        })
    )
    list_display = ('name', 'file_regex')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'mailing_list')
    filter_horizontal = ('users',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_request', 'user', 'public', 'ship_it',
                    'is_reply', 'timestamp')
    list_filter = ('public', 'timestamp')
    raw_id_fields = ('review_request', 'user', 'base_reply_to',
                     'body_top_reply_to', 'body_bottom_reply_to',
                     'comments', 'screenshot_comments',
                     'reviewed_diffset')


class ReviewRequestAdmin(admin.ModelAdmin):
    list_display = ('summary', 'submitter', 'status', 'public', 'last_updated')
    list_filter = ('public', 'status', 'time_added', 'last_updated')
    raw_id_fields = ('submitter', 'diffset_history', 'screenshots',
                     'inactive_screenshots')
    filter_horizontal = ('target_people',)


class ReviewRequestDraftAdmin(admin.ModelAdmin):
    list_display = ('summary', 'submitter', 'last_updated')
    list_filter = ('last_updated',)
    raw_id_fields = ('review_request', 'diffset', 'screenshots',
                     'inactive_screenshots')
    filter_horizontal = ('target_people',)


class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'caption', 'image')
    list_display_links = ('thumb', 'caption')


class ScreenshotCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'screenshot', 'timestamp')
    list_filter = ('timestamp',)
    raw_id_fields = ('screenshot', 'reply_to')


admin.site.register(Comment, CommentAdmin)
admin.site.register(DefaultReviewer, DefaultReviewerAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewRequest, ReviewRequestAdmin)
admin.site.register(ReviewRequestDraft, ReviewRequestDraftAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(ScreenshotComment, ScreenshotCommentAdmin)
