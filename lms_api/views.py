from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(APIView):
    def get(self, request, id=None):
        if id:
            try:
                todo = Todo.objects.get(id=id)  # Retrieve Todo by id instead of slug
            except Todo.DoesNotExist:
                raise NotFound(detail="Todo not found")
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
