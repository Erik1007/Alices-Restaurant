# General notes

# Extending base

Looks like have a couple of pages that work correctly, for example the [login](./templates/account/login.html) page but, the [registration](./templates/account/signup.html) page doesn't quite work. You normally only want to have ONE base.html file. So if you change something there it changes EVERYWHERE. Check the difference in the `extends` block between login and registration. Also, check out the `Templates` section in the debug toolbar. It'll show you which templates are being included in the render. 

# Reserve a table

Based on what I've seen in the code the place where you are "stuck" is on the reserve a table view? The code in the view `reserve_table` looks correct but, obviously when you click on the link in the header you get a very unhelpful error `name 'queryset' is not defined` where there's nothing called `queryset` in that view. 

Let's take a look at the error a bit more in detail. The `Traceback`, although it looks scary is the secret to everything broken and it's helpful to understand a bit of what is going on. The `trackback` is a stack... It's the series of calls made which resulted in the error with the most RECENT at the top and the oldest at the bottom. Usually, you want to start at the bottom since that's what usually CAUSED the error. If we start at the bottom we will see the 

In the file `/workspace/Alices-Restaurant/blog/views.py` on  line `17` within the `get` function the following function was called

>  `post = get_object_or_404(queryset, slug=slug) `

Re-read that again if you don't spot it...

The file where the function is being called is
> `/workspace/Alices-Restaurant/blog/views.py`

....

> `/****/*****/blog/***`

You are trying to fetch a blog post... Not a reservation.

Let's look at the URL being called

`https://8000-erik1007-alicesrestaura-u8qspgnywzx.ws-eu77.gitpod.io/reserve_table/`

If we go reference our `urls.py` file we will see

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", include("blog.urls"), name="blog"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reserve_table/', include(
        'reservation.urls', namespace='reservation')),   
]
```

URLs in Django are are stored in `urlpatterns` which you'll see is just an array. When Django gets a request from the user (for example for the URL `/reserve_table/`) it starts at the top of the array and starts searching it's way down until it finds something that matches. It's tricky but, `""` (empty string) actually matches EVERYTHING, since a blog post can be called, well anything? Right? 

If we move the `blog` object to the bottom of the arrray, so it'll only match something if NOTHING else is matched, that will solve the issue. For example


```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reserve_table/', include(
        'reservation.urls', namespace='reservation')),   
    path("", include("blog.urls"), name="blog"),
]
```

Additionally, we could also make the URL for blog posts more specific, so it would have to match a URL only for blog posts, for example


```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("blog/", include("blog.urls"), name="blog"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reserve_table/', include(
        'reservation.urls', namespace='reservation')),   
]
```

Then blog posts would have to be `blog/my-first-post`.

Once we fix that, we get a new error

```
TemplateDoesNotExist at /reserve_table/

reservation/reservation.html
```

Templates in Django start at the `TEMPLATE_ROOT` and there's a file called `reservation.html` but, not directory called `reservation`. You can either change the `render` function or change where the template lives. 

# Testing

The way I think about testing is bumper pool, or gaurd rails on highway. They are there for your safety but, if you need them. You SHOULD be writing tests but, figuring out WHAT to test is actually more difficult that the testing part itself. 

What testing is REALLY good for is two things

1. Knowing when you are done, so you can do the next thing and not waste time
2. Keeping you from breaking things later on

For #1, when you write your user stores ([#5](https://github.com/Erik1007/Alices-Restaurant/issues/5)) it's helpful to have success criteria. Or a better way to think about it as a "definition of what done is". When is this user story done? What should occur? What would a user see on the screen? What error messages should appear if they do something wrong? What happens when they successfully do something? 

The answers to these questions are both elements of the "done when" part of the user story but, also are GREAT TESTS. 

So, a user should see the date picker on their screen.

I should write a test that sees if the date picker HTML element is returned by the view. 

```python

from django.test import TestCase

class TestReservationView(TestCase):
    def test_user_should_see_date_picker(self):
        response = self.client.get("/reserve_table")
        
        # note... you should use Django's reverse function where possible. It's much nicer

        #response = self.client.get( reverse('reserve_table') )

        self.assertContains(response, '<div class="date-picker">')
        self.assertTemplateUsed(response, 'reservation.html')
```


