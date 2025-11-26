
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

@api_view(['POST'])
def prestamos_multa(request):
    dias = request.data.get('diasRetraso', 0)
    multa_por_dia = request.data.get('multaPorDia', 0)

    if dias <= 0:
        multa = 0
        mensaje = "Sin retraso"
    else:
        multa = dias * multa_por_dia
        if multa <= 5:
            mensaje = "Retraso leve"
        elif 5 < multa <= 15:
            mensaje = "Retraso moderado"
        else:
            mensaje = "Retraso grave, revisar con administración"

    return Response({
        "diasRetraso": dias,
        "multa": multa,
        "mensaje": mensaje
    })
