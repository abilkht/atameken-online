import uuid
from collections import Counter

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from slugify import slugify

from taggit.managers import TaggableManager
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Vote(models.Model):
    """Model class to host every vote, made with ContentType framework to
    allow a single model connected to Questions and Answers."""
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType,
                                     blank=True, null=True, related_name="votes_on", on_delete=models.CASCADE)
    object_id = models.CharField(
        max_length=50, blank=True, null=True)
    vote = GenericForeignKey(
        "content_type", "object_id")

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
        index_together = ("content_type", "object_id")
        unique_together = ("user", "content_type", "object_id")


class QuestionQuerySet(models.query.QuerySet):
    """Personalized queryset created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question2QuerySet(models.query.QuerySet):
    """Personalized queryset [2] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question3QuerySet(models.query.QuerySet):
    """Personalized queryset [3] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question4QuerySet(models.query.QuerySet):
    """Personalized queryset [4] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question5QuerySet(models.query.QuerySet):
    """Personalized queryset [5] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question6QuerySet(models.query.QuerySet):
    """Personalized queryset [6] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question7QuerySet(models.query.QuerySet):
    """Personalized queryset [7] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question8QuerySet(models.query.QuerySet):
    """Personalized queryset [8] created to improve model usability"""

    def get_answered(self):
        """Returns only items which has been marked as answered in the current
        queryset"""
        return self.filter(has_answer=True)

    def get_unanswered(self):
        """Returns only items which has not been marked as answered in the
        current queryset"""
        return self.filter(has_answer=False)

    def get_counted_tags(self):
        """Returns a dict element with tags and its count to show on the UI."""
        tag_dict = {}
        query = self.all().annotate(tagged=Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Question(models.Model):
    """Model class to contain every question in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = QuestionQuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question2(models.Model):
    """Model class to contain every question [2] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question2QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question2")
        verbose_name_plural = _("Questions2")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer2.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question2.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer2.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer2.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question3(models.Model):
    """Model class to contain every question [3] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question3QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question3")
        verbose_name_plural = _("Questions3")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer3.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question3.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer3.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer3.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question4(models.Model):
    """Model class to contain every question [4] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question4QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question4")
        verbose_name_plural = _("Questions4")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer4.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question3.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer4.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer4.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question5(models.Model):
    """Model class to contain every question [5] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question5QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question5")
        verbose_name_plural = _("Questions5")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer5.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question5.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer5.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer5.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question6(models.Model):
    """Model class to contain every question [6] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question6QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question6")
        verbose_name_plural = _("Questions6")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer6.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question6.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer6.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer6.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question7(models.Model):
    """Model class to contain every question [7] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question7QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question7")
        verbose_name_plural = _("Questions7")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer7.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question7.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer7.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer7.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Question8(models.Model):
    """Model class to contain every question [8] in the forum."""
    OPEN = "O"
    CLOSED = "C"
    DRAFT = "D"
    STATUS = (
        (OPEN, _("Open")),
        (CLOSED, _("Closed")),
        (DRAFT, _("Draft")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    content = MarkdownxField(verbose_name='Контент')
    has_answer = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    votes = GenericRelation(Vote)
    tags = TaggableManager(verbose_name='Тэги')
    file = models.FileField(verbose_name='Загрузить файл', upload_to='forum_files/%Y/%m/%d/', default='')
    objects = Question8QuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Question8")
        verbose_name_plural = _("Questions8")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}",
                                to_lower=True, max_length=80)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def count_answers(self):
        return Answer8.objects.filter(question=self).count()

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Question8.objects.filter(id=self.id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def get_answers(self):
        return Answer8.objects.filter(question=self)

    def get_accepted_answer(self):
        return Answer8.objects.get(question=self, is_answer=True)

    def get_markdown(self):
        return markdownify(self.content)


class Answer(models.Model):
    """Model class to contain every answer in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer2(models.Model):
    """Model class to contain every answer [2] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question2, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer2")
        verbose_name_plural = _("Answers2")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer2.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer2.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer3(models.Model):
    """Model class to contain every answer [3] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question3, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer3")
        verbose_name_plural = _("Answers3")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer3.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer3.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer4(models.Model):
    """Model class to contain every answer [4] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question4, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer4")
        verbose_name_plural = _("Answers4")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer4.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer4.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer5(models.Model):
    """Model class to contain every answer [5] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question5, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer5")
        verbose_name_plural = _("Answers5")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer5.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer5.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer6(models.Model):
    """Model class to contain every answer [6] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question6, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer6")
        verbose_name_plural = _("Answers6")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer6.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer6.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer7(models.Model):
    """Model class to contain every answer [7] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question7, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer7")
        verbose_name_plural = _("Answers7")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer7.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer7.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()


class Answer8(models.Model):
    """Model class to contain every answer [8] in the forum and to link it
    to its respective question."""
    question = models.ForeignKey(Question8, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = MarkdownxField()
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    total_votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ["-is_answer", "-timestamp"]
        verbose_name = _("Answer8")
        verbose_name_plural = _("Answers8")

    def __str__(self):  # pragma: no cover
        return self.content

    def get_markdown(self):
        return markdownify(self.content)

    def count_votes(self):
        """Method to update the sum of the total votes. Uses this complex query
        to avoid race conditions at database level."""
        dic = Counter(self.votes.values_list("value", flat=True))
        Answer8.objects.filter(uuid_id=self.uuid_id).update(total_votes=dic[True] - dic[False])
        self.refresh_from_db()

    def get_upvoters(self):
        """Returns a list containing the users who upvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=True)]

    def get_downvoters(self):
        """Returns a list containing the users who downvoted the instance."""
        return [vote.user for vote in self.votes.filter(value=False)]

    def accept_answer(self):
        answer_set = Answer8.objects.filter(question=self.question)
        answer_set.update(is_answer=False)
        self.is_answer = True
        self.save()
        self.question.has_answer = True
        self.question.save()