from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class HomeScreen(View):
    def get(self, request, *args, **kwargs):
        """
        Render the home screen view.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - A rendered HTML response for the home screen view.
        """
        return render(request, "index.html")


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "reviews.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """
        Get the context data for the post list view.

        Parameters:
        - kwargs: Additional keyword arguments.

        Returns:
        - The context data for the post list view.
        """
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class AddComment(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Handle the HTTP POST request to add a comment.

        Parameters:
        - request: The HTTP request object.
        - kwargs: Additional keyword arguments.

        Returns:
        - A redirect response to the reviews page.
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            messages.success(request, 'Thank you for your comment.')
            return redirect(reverse('reviews'))
        return redirect(reverse('reviews'))
