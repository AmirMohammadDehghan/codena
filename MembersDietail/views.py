from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Our_Member, Member_Cantact_Way  # import کنید
from home.models import Course
from home.views import jalalidate

class MembersListView(ListView):
    template_name = "our-teacher.html"
    model = Our_Member  # مدل خود را مشخص کنید

    def get_queryset(self):
        return Our_Member.objects.all()  # همه اعضا را برگردانید


class MemberDetailView(DetailView):
    model = Our_Member
    template_name = "single-teacher.html"
    context_object_name = "member"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.memberdata = get_object_or_404(Our_Member, slug=self.kwargs["slug"])

        context["memberdata"] = self.memberdata
        # اطلاعات راه‌های ارتباطی برای اعضا را دریافت کنید
        courses = Course.objects.filter(teacher=self.memberdata.user)
        for item in courses:
            item.creat_at = jalalidate(item.creat_at)
        contact_ways = Member_Cantact_Way.objects.filter(user=self.memberdata.user)
        context['contact_ways'] = contact_ways
        context['courses'] = courses


        return context

