from django.http import JsonResponse
from .models import Project, Sector
from django.db.models import Count, Sum

def project_summary(request):
    # Get the total count of projects
    project_count = Project.objects.count()

    # Get the total budget of all projects
    total_budget = Project.objects.aggregate(Sum('budget'))['budget__sum']

    # Get the count and total budget for each sector
    sectors = Sector.objects.annotate(project_count=Count('project'), budget=Sum('project__budget'))

    # Build the response data
    response_data = {
        'project_count': project_count,
        'total_budget': total_budget,
        'sectors': []
    }

    for sector in sectors:
        response_data['sectors'].append({
            'id': sector.id,
            'name': sector.name,
            'project_count': sector.project_count,
            'budget': sector.budget
        })

    return JsonResponse(response_data)
