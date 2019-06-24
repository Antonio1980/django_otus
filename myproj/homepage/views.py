from datetime import datetime, timedelta
from random import randint
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse


class ArticleView(TemplateView):
    template_name = 'homepage/index.html'

    def get_dates_list(self, count=10):
        result = []
        today = datetime.today()
        for i in range(count):
            date_ = today - timedelta(days=i)
            for j in range(randint(1, 4)):
                result.append(
                    date_.replace(hour=randint(0, 23))
                )
        return result

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        print(context)
        my_obj = MyClass()
        my_obj.data = {'spam': 'eggs'}
        my_obj.list = list(range(10, 20))
        my_obj.baz = list(range(7))
        args = {
            'articles': list(range(1, 6)),
            # 'articles': [],
            'val0': '1hi',
            'val1': 'Otus',
            'val2': False,
            'obj': my_obj,
            'a_title': "my django project",
            'string': ("First \n"
                       "Second \n"
                       "Third \n"
                       ),
            'current': datetime.today(),
            'dates': self.get_dates_list(),
            'items': list(range(4)),
        }
        context.update(args)
        return context


def article_year(request, year):
    return HttpResponse(f'<h1>Year is {year} ({type(year)})</h1>')


class MyClass:
    foo = 42
    bar = 60

    def __repr__(self):
        return f"<MyClass {self.foo} {self.bar}>"
