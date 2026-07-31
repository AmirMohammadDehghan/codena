from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import RoadMapDetails, RoadMaps
from blog.models import Post
from blog.views import jalalidate
from .forms import ConsultationRequestForm


# Create your views here.


class RoadMapListView(ListView):

    def articles_jalalidate(self):
        for item in self.articles:
            item.date = jalalidate(item.date)

    # context_object_name = "book_list"
    # queryset = Book.objects.filter(publisher__name="ACME Publishing")

    def get_context_data(self, **kwargs):
        self.mapdata = get_object_or_404(RoadMaps, id=self.kwargs["roadmap_id"])
        self.articles = Post.objects.all()
        self.articles_jalalidate()

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["map"] = self.mapdata
        context["questions"] = self.mapdata.questions.all()
        context["articles"] = self.articles
        context['contact_form'] = ConsultationRequestForm()
        return context

    def get_queryset(self):
        self.map = get_object_or_404(RoadMaps, id=self.kwargs["roadmap_id"])
        self.roadmapdetails = RoadMapDetails.objects.filter(roadmap=self.map).order_by("course_number")
        # for i in range(len(self.roadmapdetails)):
        #     if i % 2 == 0:
        #         self.roadmapdetails[i].is_right = True
        #     else:
        #         self.roadmapdetails[i].is_right = False
        return self.roadmapdetails

    template_name = "road-map.html"
