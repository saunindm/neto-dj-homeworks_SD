from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.serializers import DetailedSensorSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.response import Response
from measurement.models import Sensor


class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        data = request.data
        ser = SensorSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)


class UpdateViewSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DetailedSensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        data = request.data
        ser = SensorSerializer(sensor, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)


class CreateMeasurement(CreateAPIView):

    def post(self, request):
        data = request.data
        ser = MeasurementSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
