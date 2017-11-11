from django.shortcuts import render
from .forms import ImageForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Image
# Create your views here.]

from sightengine.client import SightengineClient


def result(request):
	pk=3
	data = Image.objects.get(id=pk)

	def check_safety(input_url):
		client = SightengineClient('265033791', 'E8KsSkGNjT4Em8aaCUpF')
		checkNudity = client.check('nudity')
		output1 = checkNudity.set_url(input_url)
		safety_level = output1['nudity']['safe']
		if safety_level<0.5:
			return 1
		else :
			return 0

		# We set the url and pass it to the check_safety function
		# 1 is for sexual explicit content and 0 is for safe content

		#print(i)
	val1a = check_safety(data.img_1_a)
	val1b = check_safety(data.img_1_b)
	val2a = check_safety(data.img_2_a)
	val2b = check_safety(data.img_2_b)
	val3a = check_safety(data.img_3_a)
	val3b = check_safety(data.img_3_b)

	return render(request, 'app/result.html', {'objectdata':data,
	'val1a':val1a,
	'val1b':val1b,
	'val2a':val2a,
	'val2b':val2b,
	'val3a':val3a,
	'val3b':val3b})

#'objectData': data

def home(request):
    form_class = ImageForm

    # if request is not post, initialize an empty form

    form = form_class(request.POST or None)
    if request.method == 'POST':

        # form = ImageForm(request.POST)

        if form.is_valid():
            post = form.save(commit=True)
            post.save()
 		    # 	template = loader.get_template("app/result.html")
			# context = {'form': form}
			# return HttpResponse(template.render(context, request))
            return HttpResponseRedirect(reverse('app:result'))
        else:
            form = ImageForm()
    return render(request, 'app/base.html', {'form': form})



			


			
			

#, kwargs={"pk": form.pk } 