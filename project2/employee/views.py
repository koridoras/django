from django.views import generic
from .forms import SearchForm
from .models import Employee


class IndexView(generic.ListView):
    model = Employee
    paginate_by = 5

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)   # 基の辞書に、formを追加
        return context

    def get_queryset(self):
        """テンプレートへ渡す「employee_list」を作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid()  # これをしないと、cleaned_dataができない!!!

        # まず、全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        # サークルの選択があれば、サークルで絞り込み(filter)
        status = form.cleaned_data['status']
        if status:
            queryset = queryset.filter(status=status)
        return queryset