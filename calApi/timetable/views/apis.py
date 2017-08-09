from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse

from timetable.models import Course

def get_courses_by_code(request):
    school = request.GET.get('school')
    semester = request.GET.get('semester')
    codes_str = request.GET.get('code')
    codes = codes_str.split(' ')
    result = []
    try:
        for code in codes:
            c = Course.objects.get(code=code, semester=semester, school=school.upper())
            result.append({
                    "code": c.code,
                    "credits": c.credits,
                    "title": c.title,
                    "professor": c.professor,
                    "department": c.department,
                    "time": c.time,
                    "location": c.location,
                    "note": c.note,
                    "discipline": c.discipline,
                }
            )
        return JsonResponse(result, safe=False)
    except Exception as e:
        raise Http404("Page does not exist")
    return HttpResponse(str(codes))
