import django_filters

from Job.models import Film

class JobFilter(django_filters.FilterSet):
	experience_gt = django_filters.NumberFilter(name='experience', lookup_expr='gt')
	experience_lt = django_filters.NumberFilter(name='experience', lookup_expr='lt')
	class Meta:
		model = Job
