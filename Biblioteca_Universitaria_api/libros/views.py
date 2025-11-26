
from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
@api_view(['POST'])
def prestamos_semana(request):
    prestamos = request.data.get('prestamosPorDia', [])
    if len(prestamos) != 7:
        return Response({"error": "Debe enviar 7 valores (uno por día)"}, status=400)

    total = sum(prestamos)
    promedio = total / 7

    if total < 10:
        mensaje = "Poca actividad de préstamo"
    elif 10 <= total <= 30:
        mensaje = "Actividad normal"
    else:
        mensaje = "Alta demanda de libros"

    return Response({
        "totalPrestamos": total,
        "promedioDiario": promedio,
        "mensaje": mensaje
    })


