# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author : strangestring
# github : https://github.com/strangestring


import time


class ZhiHu:
    def __init__(self):
        """
        Core of zhihu API
        """
        self.members = self._Members()
        self.articles = self._Articles()
        self.answers = self._Answers()
        self.questions = self._Questions()
        self.pins = self._Pins()
        self.topics = self._Topics()

    class _Members:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/members'

        def info(self, url_token, query_args=None):
            """
            用户信息
            :param url_token:
            :param query_args:'allow_message','is_followed','is_following','description','is_org','is_blocking','employments','answer_count','follower_count','articles_count','gender','thanked_count','favorited_count','badge[?(type=best_answerer)].topics' ,etc.
            :return:
            """
            # global member_url_prefix
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{url_token}'

        def followees(self, url_token, offset=0, limit=20, query_args=None):
            """
            用户关注的人
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/followees?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/followees?offset={offset}&limit={limit}'

        def followers(self, url_token, offset=0, limit=20, query_args=None):
            """
            用户的关注者
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/followers?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/followers?offset={offset}&limit={limit}'

        def activities(self, url_token, after_id=int(time.time()), limit=7,
                       session_id=<YOUR SESSION_ID>, query_args=None):
            """
            Because of the high cost of obtaining full dynamics
            asynchronously, it is recommended to use this method
            only to determine the active state of the user in
            a certain period of time

            If you replace 'after_id with 'before_id'here
            the effect is the same as after_id=int(time.time)
            desktop=True seems have no effect
            :param url_token:
            :param after_id: another form of offset
            :param session_id: each logged-in user has a unique session_id,please fill in your own uid above,you may construct your own session_id pool
            :param limit:
            :return:
            """
            return f'{self.url_prefix}/{url_token}/activities?limit={limit}&session_id={session_id}&after_id={after_id}&desktop=True'

        def pins(self, url_token, offset=0, limit=20, query_args=None):
            """
            想法
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/pins?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/pins?offset={offset}&limit={limit}'

        def answers(self, url_token, offset=0, limit=20, sort_by='voteups',
                    query_args=None):
            """
            回答
            :param url_token:
            :param offset:
            :param limit:
            :param sort_by:'voteups'/'created'
            :param query_args:'is_normal','admin_closed_comment','reward_info',
            'is_collapsed','annotation_action','annotation_detail','collapse_reason',
            'collapsed_by','suggest_edit','comment_count','can_comment','content',
            'voteup_count','reshipment_settings','comment_permission','mark_infos',
            'created_time','updated_time','review_info','question','excerpt',
            'is_labeled','label_info','relationship.is_authorized','voting',
            'is_author','is_thanked','is_nothelp',
            'is_recognized;data[*].author.badge[?(type=best_answerer)].topics'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/answers?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{url_token}/answers?offset={offset}&limit={limit}&sort_by={sort_by}'

        def articles(self, url_token, offset=0, limit=20, sort_by='voteups',
                     query_args=None):
            """
            文章
            :param url_token:
            :param offset:
            :param limit:
            :param sort_by:'voteups'/'created'
            :param query_args:'comment_count','suggest_edit','is_normal',
            'thumbnail_extra_info','thumbnail','can_comment','comment_permission',
            'admin_closed_comment','content','voteup_count','created','updated',
            'upvoted_followees','voting','review_info','is_labeled',
            'label_info;data[*].author.badge[?(type=best_answerer)].topics'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/articles?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{url_token}/articles?offset={offset}&limit={limit}&sort_by={sort_by}'

        def questions(self, url_token, offset=0, limit=20, query_args=None):
            """
            提问
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:'created','answer_count','follower_count','author',
            'admin_closed_comment'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/questions?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/questions?offset={offset}&limit={limit}'

        def column_contributions(self, url_token, offset=0, limit=20,
                                 query_args=None):
            """
            专栏
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:'column.intro','followers','articles_count'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/column-contributions?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/column-contributions?offset={offset}&limit={limit}'

        def favlists(self, url_token, offset=0, limit=20, query_args=None):
            """
            收藏夹
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:'updated_time','answer_count','follower_count','is_public'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/favlists?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/favlists?offset={offset}&limit={limit}'

        def following_columns(self, url_token, offset=0, limit=20,
                              query_args=None):
            """
            关注的专栏
            :param url_token:
            :param offset:
            :param limit:
            :param query_args:'intro','followers','articles_count'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/following-columns?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/following-columns?offset={offset}&limit={limit}'

        def following_topic_contributions(self, url_token, offset=0, limit=20,
                                          query_args=None, ):
            """
            关注的话题(及在该话题下的回答数量(?))
            :param url_token:
            :param offset:
            :param limit:
            :param query_args: 'topic','introduction'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/following-topic-contributions?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/following-topic-contributions?offset={offset}&limit={limit}'

        def following_questions(self, url_token, offset=0, limit=20,
                                query_args=None):
            """
            关注的问题
            :param url_token:
            :param offset:
            :param limit:
            :param query_args: 'created','answer_count','follower_count','author'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/following-questions?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/following-questions?offset={offset}&limit={limit}'

        def following_favlists(self, url_token, offset=0, limit=20,
                               query_args=None):
            """
            关注的收藏夹
            :param url_token:
            :param offset:
            :param limit:
            :param query_args: 'updated_time','answer_count','follower_count'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/following-favlists?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{url_token}/following-favlists?offset={offset}&limit={limit}'

        def marked_answers(self, url_token, offset=0, limit=20,
                           sort_by='voteups', query_args=None):
            """
            被收录回答
            :param url_token:
            :param offset:
            :param limit:
            :param sort_by:
            :param query_args:'is_normal','admin_closed_comment','reward_info',
            'is_collapsed','annotation_action','annotation_detail','collapse_reason',
            'collapsed_by','suggest_edit','comment_count','can_comment','content',
            'voteup_count','reshipment_settings','comment_permission','mark_infos',
            'created_time','updated_time','review_info','question','excerpt',
            'is_labeled','label_info','relationship.is_authorized','voting',
            'is_author','is_thanked','is_nothelp',
            'is_recognized;data[*].author.badge[?(type=best_answerer)].topics'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/marked-answers?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{url_token}/marked-answers?offset={offset}&limit={limit}&sort_by={sort_by}'

        def included_articles(self, url_token, offset=0, limit=20,
                              sort_by='voteups', query_args=None):
            """
            被收录文章
            :param url_token:
            :param offset:
            :param limit:
            :param sort_by:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/included-articles?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{url_token}/included-articles?offset={offset}&limit={limit}&sort_by={sort_by}'

        def mutuals(self, url_token, offset=0, limit=10, sort_by='voteups',
                    query_args=None):
            """
            我的关注中也关注TA的人
            :param url_token:
            :param offset:
            :param limit:
            :param sort_by:
            :param query_args:'answer_count','articles_count','gender','follower_count',
            'is_followed','is_following','badge[?(type=best_answerer)].topics'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}/relations/mutuals?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{url_token}/relations/mutuals?offset={offset}&limit={limit}&sort_by={sort_by}'

    class _Articles:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/articles'

        def info(self, url_token, query_args=None):
            """

            :param url_token:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{url_token}'

        def likers(self, article_id, offset=0, limit=20, query_args=None):
            """
            up_voters
            :param article_id:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{article_id}/likers?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{article_id}/likers?offset={offset}&limit={limit}'

        def concerned_upvoters(self, article_id, query_args=None):
            """
            我的关注中的点赞者
            :param article_id:
            :return:
            """
            return f'{self.url_prefix}/{article_id}/concerned_upvoters'

        def root_comments(
                self,
                article_id,
                offset=0,
                limit=20,
                order='normal', query_args=None):
            """
            结构化评论,建议仅在需要完整评论时使用.结果处理较麻烦
            :param article_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{article_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

        def comments(self, article_id, offset=0, limit=20, order='reverse',
                     query_args=None):
            """
            非结构化评论,'reverse'即'按时间排序'
            :param article_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{article_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

    class _Answers:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/answers'

        def info(self, url_token, query_args=None):
            """

            :param url_token:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{url_token}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{url_token}'

        def voters(self, answer_id, offset=0, limit=10, query_args=None):
            """
            点赞者
            :param answer_id:
            :param offset:
            :param limit:
            :param query_args: 'answer_count','articles_count','follower_count',
            'gender','is_followed','is_following','badge'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{answer_id}/voters?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{answer_id}/voters?offset={offset}&limit={limit}'

        def concerned_upvoters(self, answer_id, offset=0, limit=20,
                               query_args=None):
            """
            我的关注中的点赞者
            :param answer_id:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{answer_id}/concerned_upvoters?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{answer_id}/concerned_upvoters?offset={offset}&limit={limit}'

        def favlists(self, answer_id, offset=0, limit=20, query_args=None):
            """
            收录该回答的收藏夹
            :param answer_id:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{answer_id}/favlists?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{answer_id}/favlists?offset={offset}&limit={limit}'

        def root_comments(
                self,
                answer_id,
                offset=0,
                limit=20,
                order='normal',
                query_args=None):
            """
            结构化评论,建议仅在需要完整评论时使用.结果处理较麻烦
            :param answer_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{answer_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

        def comments(self, answer_id, offset=0, limit=20, order='reverse',
                     query_args=None):
            """
            非结构化评论,'reverse'即'按时间排序'
            :param answer_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{answer_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

    class _Questions:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/questions'

        def info(self, question_id, query_args=None):
            """
            信息
            :param question_id:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{question_id}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{question_id}'

        def log(self, question_id, query_args=None):
            """
            return json
            :param question_id:
            :param query_args: unused
            :return:
            """
            return f'https://www.zhihu.com/question/{question_id}/log'

        def followers(self, question_id, offset=0, limit=20, query_args=None):
            """
            问题的关注者
            :param question_id:
            :param offset:x
            :param limit:
            :param query_args:'gender','answer_count','articles_count',
            'follower_count','is_following','is_followed'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{question_id}/followers?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{question_id}/followers?offset={offset}&limit={limit}'

        def concerned_followers(self, question_id, offset=0, limit=20,
                                query_args=None):
            """
            我的关注中的关注者
            :param question_id:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{question_id}/concerned_followers?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{question_id}/concerned_followers?offset={offset}&limit={limit}'

        def answers(self, question_id, offset=0, limit=20, sort_by='default',
                    query_args=None):
            """
            问题下的回答
            :param question_id:
            :param offset:
            :param limit:
            :param sort_by: 'default','updated'
            :param query_args: 'is_normal','admin_closed_comment','reward_info',
            'is_collapsed','annotation_action','annotation_detail',
            'collapse_reason','is_sticky','collapsed_by','suggest_edit',
            'comment_count','can_comment','content','editable_content',
            'voteup_count','reshipment_settings','comment_permission',
            'created_time','updated_time','review_info','relevant_info',
            'question','excerpt','relationship.is_authorized','is_author',
            'voting','is_thanked','is_nothelp','is_labeled','is_recognized',
            'paid_info','paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count','badge[*].topics'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{question_id}/answers?{additional_query_items}&offset={offset}&limit={limit}&sort_by={sort_by}'
            else:
                return f'{self.url_prefix}/{question_id}/answers?offset={offset}&limit={limit}&sort_by={sort_by}'

        def collapsed_answers(self, question_id, offset=0, limit=20,
                              sort_by='default', query_args=None):
            """

            :param question_id:
            :param offset:
            :param limit:
            :param sort_by:
            :param query_args:
            :return:
            """
            return f'{self.url_prefix}/{question_id}/collapsed-answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&offset={offset}&limit={limit}&sort_by={sort_by}'

        def root_comments(self, question_id, offset=0, limit=20,
                          order='normal', query_args=None):
            """
            结构化评论,建议仅在需要完整评论时使用.结果处理较麻烦
            :param question_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{question_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

        def comments(
                self,
                question_id,
                offset=0,
                limit=20,
                order='reverse',
                query_args=None):
            """
            非结构化评论,'reverse'即'按时间排序'
            :param question_id:
            :param offset:
            :param limit:
            :param order:
            :return:
            """
            return f'{self.url_prefix}/{question_id}/root_comments?limit={limit}&offset={offset}&order={order}&status=open'

        def similar_questions(self, question_id, offset=0, limit=5,
                              query_args=None):
            """
            相似问题
            :param question_id:
            :param offset:
            :param limit: 5
            :param query_args: 'answer_count','author','follower_count'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{question_id}/similar-questions?{additional_query_items}&offset={offset}&limit={limit}'
            else:
                return f'{self.url_prefix}/{question_id}/similar-questions?offset={offset}&limit={limit}'

    class _Pins:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/pins'

        def info(self, pin_id, query_args=None):
            """

            :param pin_id:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{pin_id}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{pin_id}'

        def actions(self, pin_id, offset=0, limit=20, query_args=None):
            """
            想法转发及鼓掌名单
            :param pin_id:
            :param offset:
            :param limit:
            :param query_args:
            :return:
            """
            return f'{self.url_prefix}/{pin_id}/actions?limit={limit}&offset={offset}'

        def comments(
                self,
                pin_id,
                offset=0,
                limit=20,
                order='reverse',
                query_args=None):
            """
            非结构化评论
            :param pin_id:
            :param offset:
            :param limit:
            :param order: 'normal','reverse'
            :return:
            """
            return f'{self.url_prefix}/{pin_id}/comments?order={order}&limit={limit}&offset={offset}&status=open'

    class _Topics:
        def __init__(self):
            self.url_prefix = 'https://www.zhihu.com/api/v4/topics'

        def info(self, topic_id, query_args=None):
            """

            :param topic_id:
            :param query_args:
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{topic_id}?{additional_query_items}'
            else:
                return f'{self.url_prefix}/{topic_id}'

        def followers(self, topic_id, offset=0, limit=20, query_args=None):
            """
            关注者
            :param topic_id:
            :param offset:
            :param limit:
            :param query_args:'gender','answer_count','articles_count',
            'follower_count','is_following','is_followed'
            :return:
            """
            if query_args:
                additional_query_items = f'include=data[*].{",".join(query_args)}'
                return f'{self.url_prefix}/{topic_id}/followers?{additional_query_items}&offset={offset}&limit={limit}'

            else:
                return f'{self.url_prefix}/{topic_id}/followers?offset={offset}&limit={limit}'

        def timeline_question(self, topic_id, offset=0, limit=10,
                              query_args=None):
            """

            :param topic_id:
            :param offset:
            :param limit:
            :param query_args:'visit_count'
            :return:
            """

            '''
            {self.url_prefix}/20009759/feeds/timeline_question
?include=
.target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;

.target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;

.target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;

.target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;

data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;

data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;

data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;

data[?(target.type=question)].target.annotation_detail,comment_count;

&limit=10&offset=35
            '''
            # The customization of this thing is very complex, suggest to
            # modify here directly
            return f'{self.url_prefix}/{topic_id}/feeds/timeline_question?limit={limit}&offset={offset}'

    class _Report:
        def reports(self, page=1):
            return f'https://www.zhihu.com/api/v4/reports?page={page}'


if __name__ == '__main__':
    """
    这是封装好的知乎API.
    创建一个ZhiHu实例,将方法作为参数传入data_getter.get_data
    """
    zhi = ZhiHu()
    print(zhi.members.followees('zhang-jia-wei', 0, 20,
                                query_args=['following_count']))
    print(zhi.pins.info(1109795657325490176))
    print(zhi.pins.actions(1109795657325490176))
