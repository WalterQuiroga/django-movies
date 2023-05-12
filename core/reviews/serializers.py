from rest_framework import serializers

from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    """
        Serializer para POST/PUT
        json POST:

        {
            "user": 1,
            "movie": 6,
            "content": "muy buena pelicula"
        }
    
    """
    class Meta:
        model = Review
        fields = '__all__' 
        
        
        

class ReviewDetailSerializer(serializers.ModelSerializer):
    """
        Serializer para GET (detalles)

        ejemplo json response:

        {
            "id": 2,
            "user": "wquiroga",
            "content": "Excelente película sobre el juicio a las juntas militares",
            "created_at": "2023-05-10T15:16:45.691115-03:00",
            "last_updated": "2023-05-10T15:16:45.691115-03:00",
            "movie": {
            "id": 2,
            "name": "1985",
            "year": 2022,
            "synopsis": "Durante la década de 1980, un grupo de abogados investiga y lleva a juicio a los responsables de la dictadura cívico-militar argentina."
        }
        },
    """
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1



