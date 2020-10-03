from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Lead Viewsets
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_class = [
        permissions.IsAuthenticated
    ]
  
    serializer_class = LeadSerializer
    
    def get_queryset(self):
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  

    

