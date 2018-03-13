
from django import template
from higherguidanceforum.models import Subject

register = template.Library()


@register.inclusion_tag('higherguidanceforum/cats.html')
def get_Subject_list(cat=None):
	return {'cats': Subject.objects.all(),
		'act_cat': cat}